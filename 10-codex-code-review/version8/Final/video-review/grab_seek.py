"""Save frames at chosen timestamps, plus the bottom-left of the title frame.

Usage: python grab_seek.py VIDEO.mp4 --out REVIEW_DIR/close --times 0,40,80
With no --times, saves a frame every 20 seconds.
"""
import argparse
from pathlib import Path

import av
import cv2

parser = argparse.ArgumentParser()
parser.add_argument("video")
parser.add_argument("--out", required=True)
parser.add_argument("--times", default="")
args = parser.parse_args()
SRC = args.video
OUT = Path(args.out)
OUT.mkdir(parents=True, exist_ok=True)

container = av.open(SRC)
stream = container.streams.video[0]
duration = float(container.duration) / 1e6 if container.duration else 0
if args.times.strip():
    times = [float(part) for part in args.times.split(",") if part.strip()]
else:
    times = []
    cursor = 0.0
    while cursor < max(duration - 1, 0):
        times.append(round(cursor, 1))
        cursor += 20.0
    if duration:
        times.append(round(duration - 1, 1))

for t in times:
    # seek a bit early so we land on a keyframe before t
    container.seek(int((t - 0.8) * 1_000_000))
    got = False
    for frame in container.decode(stream):
        if frame.time is None:
            continue
        if frame.time + 0.05 < t:
            continue
        img = frame.to_ndarray(format="bgr24")
        hh, ww = img.shape[:2]
        vis = cv2.resize(img, (1100, int(hh * 1100 / ww)))
        path = OUT / f"t_{t:06.1f}.jpg"
        cv2.imwrite(str(path), vis, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
        print(f"saved {path.name} actual {frame.time:.2f}", flush=True)
        got = True
        break
    if not got:
        print("MISS", t, flush=True)
container.close()
first = next(OUT.glob("t_*.jpg"), None)
if first is not None:
    src_img = cv2.imread(str(first))
    if src_img is not None:
        h, w = src_img.shape[:2]
        cv2.imwrite(str(OUT / "crop_bottom.jpg"), src_img[h - 70 : h, :])
        cv2.imwrite(str(OUT / "crop_bl.jpg"), src_img[h - 70 : h, 0:360])
print("SEEK_DONE")
