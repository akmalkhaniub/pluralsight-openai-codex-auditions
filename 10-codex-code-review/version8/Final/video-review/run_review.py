"""Run the audition-recording measurements on one video.

Usage:
  C:\\Python314\\python.exe video-review\\run_review.py "VIDEO.mp4"
  C:\\Python314\\python.exe video-review\\run_review.py "VIDEO.mp4" --out "some-folder"

Writes audio.json, frames/, transcript.json, transcript.txt, and close/ frames.
Needs the Python that has av, cv2, numpy, scipy, and faster-whisper.
"""

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("video")
    parser.add_argument("--out", default="")
    parser.add_argument("--times", default="", help="Comma-separated extra frame times, in seconds")
    args = parser.parse_args()

    video = Path(args.video).resolve()
    if not video.exists():
        print(f"missing file: {video}", file=sys.stderr)
        return 1
    out = Path(args.out).resolve() if args.out else video.with_name(video.stem + "-review")
    out.mkdir(parents=True, exist_ok=True)

    steps = [
        [sys.executable, str(HERE / "analyze.py"), str(video), "--out", str(out)],
        [sys.executable, str(HERE / "transcribe.py"), str(video), "--out", str(out)],
        [sys.executable, str(HERE / "speech_stats.py"), str(out / "transcript.json")],
        [
            sys.executable,
            str(HERE / "grab_seek.py"),
            str(video),
            "--out",
            str(out / "close"),
            "--times",
            args.times,
        ],
    ]
    for cmd in steps:
        print("RUN", " ".join(cmd), flush=True)
        result = subprocess.run(cmd)
        if result.returncode != 0:
            return result.returncode
    print("REVIEW_DONE", out, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
