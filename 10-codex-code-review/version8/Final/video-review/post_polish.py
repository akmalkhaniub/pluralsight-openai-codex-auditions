"""Polish an audition recording without a new voice take.

Does four things:
- high-pass at 80 Hz and a small presence lift
- raises loudness toward -16 LUFS, limited so peaks stay at -1.5 dBFS
- replaces digital silence with low room tone
- shortens one still hold and adds a one-second tail on the last frame

Usage:
  python post_polish.py INPUT.mp4 OUTPUT.mp4
  python post_polish.py INPUT.mp4 OUTPUT.mp4 --max-seconds 3
"""

from __future__ import annotations

import argparse
import sys
from fractions import Fraction

import av
import numpy as np
from scipy import ndimage, signal

# Still hold on the finished re-review card, after the box is on screen
# and before the cut to the terminal.
CUT_START = 372.3
CUT_END = 375.9
TAIL_S = 1.0
TARGET_LUFS = -16.0
CEILING_DB = -1.5


def decode_audio(path: str) -> tuple[np.ndarray, int]:
    container = av.open(path)
    stream = next(s for s in container.streams if s.type == "audio")
    rate = stream.codec_context.sample_rate
    chunks = []
    for frame in container.decode(stream):
        arr = frame.to_ndarray().astype(np.float32)
        if arr.ndim == 1:
            chunks.append(arr)
        elif arr.shape[0] <= 8 and arr.shape[0] < arr.shape[1]:
            chunks.append(arr.mean(axis=0))
        else:
            chunks.append(arr.mean(axis=1))
    container.close()
    audio = np.concatenate(chunks)
    if float(np.max(np.abs(audio))) > 2:
        audio = audio / 32768.0
    return np.clip(audio, -1.5, 1.5), rate


def high_shelf(samples: np.ndarray, rate: int, freq: float, gain_db: float) -> np.ndarray:
    amp = 10 ** (gain_db / 40)
    omega = 2 * np.pi * freq / rate
    alpha = np.sin(omega) / (2 * 0.707)
    cosine = np.cos(omega)
    beta = 2 * np.sqrt(amp) * alpha
    b0 = amp * ((amp + 1) + (amp - 1) * cosine + beta)
    b1 = -2 * amp * ((amp - 1) + (amp + 1) * cosine)
    b2 = amp * ((amp + 1) + (amp - 1) * cosine - beta)
    a0 = (amp + 1) - (amp - 1) * cosine + beta
    a1 = 2 * ((amp - 1) - (amp + 1) * cosine)
    a2 = (amp + 1) - (amp - 1) * cosine - beta
    return signal.filtfilt([b0 / a0, b1 / a0, b2 / a0], [1, a1 / a0, a2 / a0], samples).astype(np.float32)


def integrated_lufs(samples: np.ndarray, rate: int) -> float:
    if rate == 48000:
        shelf_b = [1.53512485958697, -2.69169618940638, 1.19839281085285]
        shelf_a = [1.0, -1.69065929318241, 0.73248077421585]
        weighted = signal.lfilter(shelf_b, shelf_a, samples)
    else:
        weighted = samples
    hp_b, hp_a = signal.butter(2, 100 / (rate / 2), btype="high")
    weighted = signal.lfilter(hp_b, hp_a, weighted)
    block = int(0.4 * rate)
    hop = int(0.1 * rate)
    count = 1 + max(0, (len(weighted) - block) // hop)
    powers = np.array([float(np.mean(weighted[i * hop : i * hop + block] ** 2)) for i in range(count)])
    absolute = 10 ** ((-70 + 0.691) / 10)
    loud = powers[powers >= absolute]
    if len(loud) == 0:
        return -70.0
    ungated = -0.691 + 10 * np.log10(float(np.mean(loud)) + 1e-20)
    relative = 10 ** (((ungated - 10) + 0.691) / 10)
    gated = powers[powers >= max(absolute, relative)]
    return float(-0.691 + 10 * np.log10(float(np.mean(gated)) + 1e-20))


def limit(samples: np.ndarray, rate: int, ceiling: float) -> np.ndarray:
    envelope = ndimage.maximum_filter1d(np.abs(samples), size=max(3, int(0.008 * rate)), mode="nearest")
    gain = np.minimum(1.0, ceiling / (envelope + 1e-12)).astype(np.float32)
    step = 64
    coarse = gain[::step]
    smoothed = np.empty_like(coarse)
    smoothed[0] = coarse[0]
    release = np.exp(-step / (rate * 0.08))
    for i in range(1, len(coarse)):
        if coarse[i] < smoothed[i - 1]:
            smoothed[i] = coarse[i]
        else:
            smoothed[i] = smoothed[i - 1] * release + coarse[i] * (1 - release)
    full = np.interp(np.arange(len(gain)), np.arange(len(coarse)) * step, smoothed).astype(np.float32)
    return samples * full


def fill_silence(samples: np.ndarray, rate: int, tone: np.ndarray) -> np.ndarray:
    out = samples.copy()
    win = int(0.05 * rate)
    hop = win
    count = len(out) // hop
    if count == 0:
        return out
    rms = np.sqrt(np.mean(out[: count * hop].reshape(count, hop) ** 2, axis=1) + 1e-20)
    level = 20 * np.log10(rms)
    quiet = level < -68
    edge = int(0.05 * rate)
    i = 0
    while i < len(quiet):
        if not quiet[i]:
            i += 1
            continue
        j = i
        while j < len(quiet) and quiet[j]:
            j += 1
        start = i * hop + edge
        end = j * hop - edge
        if end - start > int(0.2 * rate):
            need = end - start
            loop = np.resize(tone, need + len(tone))
            bed = loop[:need]
            fade = min(edge, need // 4)
            if fade > 8:
                ramp = np.linspace(0, 1, fade, dtype=np.float32)
                bed[:fade] *= ramp
                bed[-fade:] *= ramp[::-1]
                mixed = out[start:end]
                mixed[:fade] = mixed[:fade] * (1 - ramp) + bed[:fade]
                mixed[-fade:] = mixed[-fade:] * ramp + bed[-fade:] * (1 - ramp)
                mixed[fade:-fade] = bed[fade:-fade]
                out[start:end] = mixed
            else:
                out[start:end] = bed
        i = j
    return out


def polish_audio(samples: np.ndarray, rate: int) -> np.ndarray:
    cut_a = int(CUT_START * rate)
    cut_b = int(CUT_END * rate)
    tone_a = int(39.2 * rate)
    tone_b = int(41.0 * rate)
    tone = samples[tone_a:tone_b].copy()
    edited = np.concatenate(
        [samples[:cut_a], samples[cut_b:], np.zeros(int(TAIL_S * rate), dtype=np.float32)]
    ).astype(np.float32)

    hp_b, hp_a = signal.butter(2, 80 / (rate / 2), btype="high")
    edited = signal.filtfilt(hp_b, hp_a, edited).astype(np.float32)
    tone = signal.filtfilt(hp_b, hp_a, tone).astype(np.float32)
    edited = high_shelf(edited, rate, 3500, 2.5)
    tone = high_shelf(tone, rate, 3500, 2.5)

    tone_rms = float(np.sqrt(np.mean(tone ** 2) + 1e-20))
    target_rms = 10 ** (-54 / 20)
    tone *= target_rms / tone_rms
    edited = fill_silence(edited, rate, tone)

    loudness = integrated_lufs(edited, rate)
    gain = 10 ** ((TARGET_LUFS - loudness) / 20)
    edited *= gain
    ceiling = 10 ** (CEILING_DB / 20)
    edited = limit(edited, rate, ceiling)
    peak = 20 * np.log10(float(np.max(np.abs(edited))) + 1e-12)
    done = integrated_lufs(edited, rate)
    print(f"audio: source-edit loudness {loudness:.1f} LUFS, gain {20*np.log10(gain):.1f} dB, result {done:.1f} LUFS, peak {peak:.2f} dBFS", flush=True)
    return np.clip(edited, -1, 1)


def encode(src: str, dst: str, audio: np.ndarray, rate: int, max_seconds: float | None) -> None:
    inbound = av.open(src)
    video_in = inbound.streams.video[0]
    output = av.open(dst, "w")
    video = output.add_stream("libx264", rate=30)
    video.width = video_in.codec_context.width
    video.height = video_in.codec_context.height
    video.pix_fmt = "yuv420p"
    video.options = {"crf": "17", "preset": "veryfast", "profile": "high"}
    audio_stream = output.add_stream("aac", rate=rate)
    audio_stream.layout = "stereo"
    audio_stream.bit_rate = 192000

    index = 0
    last = None
    limit_frames = None if max_seconds is None else int(max_seconds * 30)
    for frame in inbound.decode(video_in):
        if frame.time is None:
            continue
        t = float(frame.time)
        if CUT_START <= t < CUT_END:
            continue
        image = frame.to_ndarray(format="bgr24")
        last = image
        video_frame = av.VideoFrame.from_ndarray(image, format="bgr24")
        video_frame.pts = index
        for packet in video.encode(video_frame):
            output.mux(packet)
        index += 1
        if index % 300 == 0:
            print(f"video: {index} frames", flush=True)
        if limit_frames is not None and index >= limit_frames:
            break
    inbound.close()

    if limit_frames is None and last is not None:
        for _ in range(int(TAIL_S * 30)):
            video_frame = av.VideoFrame.from_ndarray(last, format="bgr24")
            video_frame.pts = index
            for packet in video.encode(video_frame):
                output.mux(packet)
            index += 1
    for packet in video.encode():
        output.mux(packet)
    print(f"video: {index} frames encoded", flush=True)

    target_samples = int(round(index / 30 * rate))
    if len(audio) < target_samples:
        audio = np.pad(audio, (0, target_samples - len(audio)))
    audio = audio[:target_samples]
    stereo = np.vstack([audio, audio]).astype(np.float32)
    frame_size = 1024
    cursor = 0
    for start in range(0, stereo.shape[1], frame_size):
        chunk = stereo[:, start : start + frame_size]
        if chunk.shape[1] < frame_size:
            chunk = np.pad(chunk, ((0, 0), (0, frame_size - chunk.shape[1])))
        audio_frame = av.AudioFrame.from_ndarray(chunk, format="fltp", layout="stereo")
        audio_frame.sample_rate = rate
        audio_frame.pts = cursor
        cursor += frame_size
        for packet in audio_stream.encode(audio_frame):
            output.mux(packet)
        if limit_frames is not None and cursor >= target_samples:
            break
    for packet in audio_stream.encode():
        output.mux(packet)
    output.close()
    print("ENCODE_DONE", dst, flush=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("src")
    parser.add_argument("dst")
    parser.add_argument("--max-seconds", type=float, default=0)
    args = parser.parse_args()
    print("audio: decoding", flush=True)
    samples, rate = decode_audio(args.src)
    print("audio: polishing", flush=True)
    polished = polish_audio(samples, rate)
    if args.max_seconds > 0:
        polished = polished[: int(args.max_seconds * rate)]
    encode(args.src, args.dst, polished, rate, args.max_seconds or None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
