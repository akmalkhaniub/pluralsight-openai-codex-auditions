"""Pace, long gaps, and low-confidence words from a transcript.json.

Usage: python speech_stats.py REVIEW_DIR/transcript.json
"""
import json
import sys
from pathlib import Path

p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("transcript.json")
data = json.loads(p.read_text(encoding="utf-8"))
words = data["words"]
print("words", len(words))
# low confidence words
low = [w for w in words if w["p"] < 0.55]
print("LOW", len(low))
for w in low:
    print(f"{w['start']:7.2f} {w['p']:.2f} {w['word']}")
print("--- lowest-confidence stretches ---")
spots = sorted({round(w["start"], 1) for w in low})
for t in spots:
    chunk = [w for w in words if t - 0.2 <= w["start"] <= t + 4.5]
    print(f"\n@{t}")
    print(" ".join(f"{w['word']}({w['p']:.2f})" for w in chunk))

# pace by minute
print("\n--- wpm by minute ---")
last = words[-1]["end"] if words else 0
minutes = int(last // 60) + 1
for m in range(minutes):
    ww = [w for w in words if m*60 <= w["start"] < (m+1)*60]
    dur = 60 if (m + 1) * 60 < last else max(1, last - m * 60)
    print(m, len(ww), "wpm", round(len(ww)/dur*60, 1))

# gaps between words > 2.0s
print("\n--- word gaps >= 2.0s ---")
for a, b in zip(words, words[1:]):
    gap = b["start"] - a["end"]
    if gap >= 2.0:
        print(f"{a['end']:.2f}-{b['start']:.2f} ({gap:.2f}s) after '{a['word'].strip()}' before '{b['word'].strip()}'")
