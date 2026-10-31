import os
import sys
import cv2
import numpy as np

def build_master_video():
    output_path = "version3/audition_master_video.mp4"
    demo_path = "version3/demo_codex_review.mp4"
    slides_dir = "version3/slides_png"

    fps = 30.0
    width = 1920
    height = 1080

    # Timing in seconds mapped to TIMED_NARRATION_SCRIPT.md
    slide_durations = {
        1: 18.0,  # 0:00 - 0:18 (Title Hook)
        2: 24.0,  # 0:18 - 0:42 (Meet Codex)
        3: 23.0,  # 0:42 - 1:05 (Review is the Bottleneck)
        4: 40.0,  # 1:05 - 1:45 (Tests Pass. Ship It?)
        5: 25.0,  # 1:45 - 2:10 (Writer vs Editor)
        6: 35.0,  # 2:10 - 2:45 (Switch hats with /review)
        7: 30.0,  # 2:45 - 3:15 (Point at the line, surgical fix)
        8: 10.0,  # 3:15 - 3:25 (Demo flight plan -> switch)
    }

    recap_durations = {
        9:  23.0, # 6:17 - 6:40 (The Proof: One review, one risk caught)
        10: 18.0, # 6:40 - 6:58 (The 3 Editor questions)
        11: 14.0  # 6:58 - 7:12 (Summary & Wrap up)
    }

    total_clip_a_sec = sum(slide_durations.values())
    total_clip_c_sec = sum(recap_durations.values())

    cap_demo = cv2.VideoCapture(demo_path)
    if not cap_demo.isOpened():
        raise RuntimeError(f"Could not open demo video at {demo_path}")
    demo_frames_count = int(cap_demo.get(cv2.CAP_PROP_FRAME_COUNT))
    demo_sec = demo_frames_count / fps
    total_sec = total_clip_a_sec + demo_sec + total_clip_c_sec

    print(f"=== AUDITION MASTER VIDEO ASSEMBLY ===")
    print(f"Resolution: {width}x{height} @ {fps} FPS")
    print(f"Clip A (Slides 1-8):  {total_clip_a_sec:.1f}s ({total_clip_a_sec/60:.2f} min)")
    print(f"Clip B (Codex Demo):  {demo_sec:.1f}s ({demo_sec/60:.2f} min, {demo_frames_count} frames)")
    print(f"Clip C (Slides 9-11): {total_clip_c_sec:.1f}s ({total_clip_c_sec/60:.2f} min)")
    print(f"Total Video Duration: {total_sec:.1f}s ({total_sec/60:.2f} min, ~{int(total_sec*fps)} total frames)")

    # Video Writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    if not writer.isOpened():
        raise RuntimeError(f"Could not create video writer for {output_path}")

    written_frames = 0
    total_expected = int(total_sec * fps)

    # 1. Write Clip A (Slides 1 to 8)
    print("\n--- Writing Clip A: Concept Slides 1 to 8 ---")
    for s_idx in range(1, 9):
        dur = slide_durations[s_idx]
        n_frames = int(round(dur * fps))
        slide_file = os.path.join(slides_dir, f"slide_{s_idx:02d}.png")
        frame = cv2.imread(slide_file)
        if frame is None:
            raise FileNotFoundError(f"Missing slide image {slide_file}")
        if frame.shape[1] != width or frame.shape[0] != height:
            frame = cv2.resize(frame, (width, height))
        for _ in range(n_frames):
            writer.write(frame)
            written_frames += 1
        print(f"  Slide {s_idx:02d} written: {dur}s ({n_frames} frames). Total: {written_frames} frames")

    # 2. Write Clip B (Demo Screencast)
    print("\n--- Splicing Clip B: Live Screencast Demo ---")
    demo_read = 0
    while True:
        ret, frame = cap_demo.read()
        if not ret:
            break
        if frame.shape[1] != width or frame.shape[0] != height:
            frame = cv2.resize(frame, (width, height))
        writer.write(frame)
        written_frames += 1
        demo_read += 1
        if demo_read % 1000 == 0:
            print(f"  Demo frames processed: {demo_read}/{demo_frames_count} ({demo_read/demo_frames_count*100:.1f}%)")
    cap_demo.release()
    print(f"  Clip B complete: {demo_read} demo frames spliced. Total: {written_frames} frames")

    # 3. Write Clip C (Slides 9 to 11)
    print("\n--- Writing Clip C: Conclusion Slides 9 to 11 ---")
    for s_idx in range(9, 12):
        dur = recap_durations[s_idx]
        n_frames = int(round(dur * fps))
        slide_file = os.path.join(slides_dir, f"slide_{s_idx:02d}.png")
        frame = cv2.imread(slide_file)
        if frame is None:
            raise FileNotFoundError(f"Missing slide image {slide_file}")
        if frame.shape[1] != width or frame.shape[0] != height:
            frame = cv2.resize(frame, (width, height))
        for _ in range(n_frames):
            writer.write(frame)
            written_frames += 1
        print(f"  Slide {s_idx:02d} written: {dur}s ({n_frames} frames). Total: {written_frames} frames")

    writer.release()
    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    final_dur_sec = written_frames / fps
    print(f"\n=======================================================")
    print(f"SUCCESS: Audition Master Video Generated!")
    print(f"File: {output_path}")
    print(f"Size: {file_size_mb:.2f} MB")
    print(f"Frames: {written_frames} frames")
    print(f"Duration: {int(final_dur_sec//60)}m {int(final_dur_sec%60):02d}s ({final_dur_sec:.1f}s)")
    print(f"=======================================================\n")

if __name__ == "__main__":
    build_master_video()
