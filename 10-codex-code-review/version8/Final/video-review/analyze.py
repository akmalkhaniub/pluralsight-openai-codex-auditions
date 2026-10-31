"""Loudness, silence, and scene frames for an audition recording.

Usage: python analyze.py VIDEO.mp4 --out REVIEW_DIR
"""
import argparse
import json
from pathlib import Path

import av
import cv2
import numpy as np
from scipy import signal

parser = argparse.ArgumentParser()
parser.add_argument("video")
parser.add_argument("--out", required=True)
args = parser.parse_args()
SRC = args.video
OUT = Path(args.out)
OUT.mkdir(parents=True, exist_ok=True)
FRAMES = OUT / "frames"
FRAMES.mkdir(parents=True, exist_ok=True)

# --- audio ---
container = av.open(SRC)
astream = next(s for s in container.streams if s.type == "audio")
sr = astream.codec_context.sample_rate
chunks = []
for frame in container.decode(astream):
    arr = frame.to_ndarray()
    # planar float or packed int
    if arr.ndim == 2 and arr.shape[0] <= 8 and arr.shape[0] < arr.shape[1]:
        # planar (channels, samples)
        chunks.append(arr.astype(np.float32))
    elif arr.ndim == 2:
        # packed (samples, channels) -> planar
        chunks.append(arr.T.astype(np.float32))
    else:
        chunks.append(arr.astype(np.float32)[None, :])
container.close()

# normalize integer ranges
audio = np.concatenate(chunks, axis=1)
if audio.dtype != np.float32:
    audio = audio.astype(np.float32)
peak_abs = float(np.max(np.abs(audio)))
if peak_abs > 2.0:  # integer PCM
    if peak_abs > 40000:
        audio = audio / 32768.0
    elif peak_abs > 2:
        audio = audio / np.iinfo(np.int16).max
audio = np.clip(audio, -1.5, 1.5)
n_ch, n = audio.shape
mono = audio.mean(axis=0)

def rms(x):
    return float(np.sqrt(np.mean(np.square(x)) + 1e-20))

def db(x):
    return 20 * np.log10(max(x, 1e-12))

# 100ms windows
win = int(sr * 0.1)
hop = win
nwin = n // hop
windows = mono[: nwin * hop].reshape(nwin, hop)
wrms = np.sqrt(np.mean(windows ** 2, axis=1) + 1e-20)
wdb = 20 * np.log10(wrms)
times = np.arange(nwin) * 0.1

peak = float(np.max(np.abs(mono)))
peak_db = db(peak)
clip_samples = int(np.sum(np.abs(mono) >= 0.98))
# per channel
ch_rms_db = [db(rms(audio[c])) for c in range(n_ch)]
ch_peak_db = [db(float(np.max(np.abs(audio[c])))) for c in range(n_ch)]

# silence: below -42 dBFS for >= 0.4s
silent = wdb < -42
silences = []
i = 0
while i < len(silent):
    if silent[i]:
        j = i
        while j < len(silent) and silent[j]:
            j += 1
        dur = (j - i) * 0.1
        if dur >= 0.4:
            silences.append({"start": round(i * 0.1, 2), "end": round(j * 0.1, 2), "dur": round(dur, 2), "floor_db": round(float(np.median(wdb[i:j])), 1)})
        i = j
    else:
        i += 1

# speech windows
speech = wdb >= -38
speech_db = wdb[speech]
noise_db = wdb[~speech] if np.any(~speech) else wdb

# approximate integrated LUFS (BS.1770, 48 kHz coefficients), stereo mean then gate
def k_weight(x, fs):
    # high shelf
    b1 = np.array([1.53512485958697, -2.69169618940638, 1.19839281085285])
    a1 = np.array([1.0, -1.69065929318241, 0.73248077421585])
    # high pass
    b2 = np.array([1.0, -2.0, 1.0])
    a2 = np.array([1.0, -1.99004745483398, 0.99007225036621])
    if fs != 48000:
        # fall back: resample-less simple highpass only
        y = signal.lfilter(b2, a2, x)
        return y
    y = signal.lfilter(b1, a1, x)
    y = signal.lfilter(b2, a2, y)
    return y

kw = np.mean([k_weight(audio[c], sr) for c in range(n_ch)], axis=0)
# 400ms blocks, 75% overlap
bl = int(0.4 * sr)
hop_l = int(0.1 * sr)
nblocks = 1 + (len(kw) - bl) // hop_l
block_ms = []
block_t = []
for i in range(nblocks):
    seg = kw[i * hop_l : i * hop_l + bl]
    ms = float(np.mean(seg * seg))
    block_ms.append(ms)
    block_t.append(i * 0.1)
block_ms = np.array(block_ms)
block_t = np.array(block_t)
abs_gate = 10 ** ((-70 + 0.691) / 10)
loud_blocks = block_ms[block_ms >= abs_gate]
if len(loud_blocks):
    ungated = -0.691 + 10 * np.log10(np.mean(loud_blocks) + 1e-20)
    rel = 10 ** (((ungated - 10) + 0.691) / 10)
    gated = block_ms[block_ms >= max(abs_gate, rel)]
    lufs = float(-0.691 + 10 * np.log10(np.mean(gated) + 1e-20))
else:
    lufs = None

# loudness over time (1s, no relative gate) for consistency
sec = int(sr)
nsec = len(kw) // sec
sec_lufs = []
for i in range(nsec):
    seg = kw[i * sec : (i + 1) * sec]
    ms = float(np.mean(seg * seg))
    if ms < abs_gate:
        sec_lufs.append(None)
    else:
        sec_lufs.append(round(float(-0.691 + 10 * np.log10(ms)), 1))
speech_lufs = [v for v in sec_lufs if v is not None and v > -50]
# variation: std of speech seconds
lufs_std = float(np.std(speech_lufs)) if speech_lufs else None
lufs_p10 = float(np.percentile(speech_lufs, 10)) if speech_lufs else None
lufs_p90 = float(np.percentile(speech_lufs, 90)) if speech_lufs else None

# abrupt level jumps: consecutive 0.5s RMS differ by > 12 dB while both are speech-like
half = int(sr * 0.5)
nh = n // half
hr = np.sqrt(np.mean(mono[: nh * half].reshape(nh, half) ** 2, axis=1) + 1e-20)
hdb = 20 * np.log10(hr)
jumps = []
for i in range(1, nh):
    if hdb[i] > -40 and hdb[i - 1] > -40 and abs(hdb[i] - hdb[i - 1]) >= 10:
        jumps.append({"t": round(i * 0.5, 2), "from_db": round(float(hdb[i - 1]), 1), "to_db": round(float(hdb[i]), 1), "delta": round(float(hdb[i] - hdb[i - 1]), 1)})

# noise floor estimate: quietest 10% of windows that are not digital silence
digital = wdb < -70
ambient = wdb[~digital]
noise_floor = float(np.percentile(ambient, 8)) if len(ambient) else None

# spectrum of quietest 2 seconds vs speech for noise character
order = np.argsort(wrms)
quiet_idx = [i for i in order if wdb[i] > -65][:20]
# take median spectrum of those windows
def spec_db(idxs):
    specs = []
    for i in idxs:
        seg = mono[i * hop : (i + 1) * hop]
        if len(seg) < hop:
            continue
        spec = np.abs(np.fft.rfft(seg * np.hanning(len(seg))))
        specs.append(spec)
    if not specs:
        return None
    m = np.median(np.stack(specs), axis=0)
    freqs = np.fft.rfftfreq(hop, 1 / sr)
    # band energy
    bands = [(80, 250, "rumble"), (250, 500, "low_mud"), (500, 2000, "mid"), (2000, 5000, "presence"), (5000, 10000, "sibilance_air"), (10000, 16000, "hiss")]
    out = {}
    for a, b, name in bands:
        msk = (freqs >= a) & (freqs < b)
        out[name] = round(float(20 * np.log10(np.mean(m[msk]) + 1e-12)), 1)
    return out

speech_idx = np.where(wdb > np.percentile(wdb, 70))[0][:40]
noise_bands = spec_db(quiet_idx)
speech_bands = spec_db(speech_idx)

# DC offset
dc = [float(np.mean(audio[c])) for c in range(n_ch)]

audio_summary = {
    "duration_s": round(n / sr, 3),
    "sample_rate": sr,
    "channels": n_ch,
    "integrated_lufs": None if lufs is None else round(lufs, 1),
    "speech_lufs_p10": None if lufs_p10 is None else round(lufs_p10, 1),
    "speech_lufs_p90": None if lufs_p90 is None else round(lufs_p90, 1),
    "speech_lufs_std": None if lufs_std is None else round(lufs_std, 2),
    "peak_dbfs": round(peak_db, 2),
    "rms_dbfs": round(db(rms(mono)), 2),
    "crest_db": round(peak_db - db(rms(mono)), 1),
    "clip_samples_ge_0.98": clip_samples,
    "channel_rms_dbfs": [round(x, 2) for x in ch_rms_db],
    "channel_peak_dbfs": [round(x, 2) for x in ch_peak_db],
    "dc_offset": [round(x, 6) for x in dc],
    "noise_floor_dbfs_p8": None if noise_floor is None else round(noise_floor, 1),
    "speech_window_median_dbfs": round(float(np.median(speech_db)), 1),
    "silence_count_ge_0.4s": len(silences),
    "silence_total_s": round(sum(s["dur"] for s in silences), 2),
    "longest_silences": sorted(silences, key=lambda s: -s["dur"])[:12],
    "level_jumps_ge_10db": jumps[:30],
    "jump_count": len(jumps),
    "noise_bands_quiet": noise_bands,
    "speech_bands": speech_bands,
    "sec_lufs_head": sec_lufs[:30],
}

# per-minute loudness
per_min = []
for m in range((nsec + 59) // 60):
    vals = [v for v in sec_lufs[m * 60 : (m + 1) * 60] if v is not None]
    per_min.append({
        "minute": m,
        "speech_seconds": len(vals),
        "median_lufs": None if not vals else round(float(np.median(vals)), 1),
        "min_lufs": None if not vals else round(float(np.min(vals)), 1),
        "max_lufs": None if not vals else round(float(np.max(vals)), 1),
    })
audio_summary["per_minute"] = per_min

(OUT / "audio.json").write_text(json.dumps(audio_summary, indent=2), encoding="utf-8")
print("AUDIO_DONE", json.dumps({k: audio_summary[k] for k in ["duration_s", "integrated_lufs", "peak_dbfs", "rms_dbfs", "noise_floor_dbfs_p8", "silence_total_s", "jump_count", "clip_samples_ge_0.98"]}))

# --- frames: scene changes ---
cap = cv2.VideoCapture(SRC)
fps = cap.get(cv2.CAP_PROP_FPS) or 30
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
step = max(1, int(round(fps / 2)))  # 2 samples/sec
prev = None
saved = []
last_save_t = -10
idx = 0
while True:
    ok, frame = cap.read()
    if not ok:
        break
    if idx % step == 0:
        t = idx / fps
        small = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), (160, 90))
        if prev is None:
            score = 999
        else:
            score = float(np.mean(np.abs(small.astype(np.int16) - prev.astype(np.int16))))
        prev = small
        # also periodic safety every 25s
        periodic = (t - last_save_t) >= 25
        if (score > 12 and (t - last_save_t) >= 2.0) or periodic or t < 0.2:
            name = f"f_{len(saved):02d}_{t:07.2f}_d{score:.0f}.jpg"
            path = FRAMES / name
            # save a readable 1280-wide jpeg
            h, w = frame.shape[:2]
            scale = 1280 / w
            vis = cv2.resize(frame, (1280, int(h * scale)))
            cv2.imwrite(str(path), vis, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
            saved.append({"t": round(t, 2), "score": round(score, 1), "file": str(path)})
            last_save_t = t
            if len(saved) >= 48:
                # still continue but only big cuts
                pass
        if len(saved) > 60 and score < 25 and not periodic:
            pass
    idx += 1
    if len(saved) >= 55:
        break
cap.release()
(OUT / "frames.json").write_text(json.dumps(saved, indent=2), encoding="utf-8")
print("FRAMES", len(saved))
