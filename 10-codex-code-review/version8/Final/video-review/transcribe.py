"""Transcribe an audition recording with faster-whisper.

Usage: python transcribe.py VIDEO.mp4 --out REVIEW_DIR
"""
import argparse
import json
from pathlib import Path

from faster_whisper import WhisperModel

parser = argparse.ArgumentParser()
parser.add_argument("video")
parser.add_argument("--out", required=True)
args = parser.parse_args()
SRC = args.video
OUT = Path(args.out)
OUT.mkdir(parents=True, exist_ok=True)

model = WhisperModel("small.en", device="cpu", compute_type="int8")
segments, info = model.transcribe(
    SRC,
    language="en",
    vad_filter=True,
    beam_size=5,
    word_timestamps=True,
    condition_on_previous_text=True,
)
rows = []
words = []
for seg in segments:
    rows.append({
        "start": round(seg.start, 2),
        "end": round(seg.end, 2),
        "text": seg.text.strip(),
    })
    if seg.words:
        for w in seg.words:
            words.append({
                "start": round(w.start, 2),
                "end": round(w.end, 2),
                "word": w.word,
                "p": round(w.probability, 3),
            })
    print(f"{seg.start:7.2f} {seg.text.strip()}", flush=True)

(OUT / "transcript.json").write_text(json.dumps({"segments": rows, "words": words}, indent=2), encoding="utf-8")
text = " ".join(r["text"] for r in rows)
(OUT / "transcript.txt").write_text(text, encoding="utf-8")
print("TRANSCRIPT_DONE", len(rows), "segments", len(words), "words", "chars", len(text))
