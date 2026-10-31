# Recording, Editing & Voice Dubbing Guide: Audition v3

## 1. Master Structure & Timing

```
 CLIP A (Slides 1–8)         CLIP B (Codex App Screencast)         CLIP C (Slides 9–11)
 0:00 ──────────────── 3:25 ──► 3:25 ──────────────────────── 6:17 ──► 6:17 ─────────────── 7:12
 (205 seconds)                 (172 seconds / 2:52)                 (55 seconds)
```

- **Total Runtime:** Exactly **7:12** (432 seconds).
- **Format:** 1920×1080 (16:9), 30.00 FPS.

---

## 2. Voice Dubbing Workflow

You have a ready-to-dub master video file: `audition_master_video.mp4` (assembled from Slide Clips A & C and Demo Clip B).

### Option 1: Live Teleprompter Dubbing (Fastest)
1. Open `audition_master_video.mp4` in a media player (e.g. VLC, Windows Media Player) on one screen.
2. Open `TIMED_NARRATION_SCRIPT.md` on your second screen or side-by-side.
3. Open your favorite audio recorder (Audacity, OBS, Adobe Audition, or your DAW).
4. Hit Record on your mic, press Play on the video, and speak along with the visual slide builds and demo cues.
5. In your video editor, drop the recorded audio on track 1, align the start with 0:00, and export.

### Option 2: Multi-Track Video Editor (DaVinci Resolve / Premiere / CapCut / Camtasia)
1. Import `audition_master_video.mp4` onto the video timeline.
2. Arm an audio track for voice recording over the timeline.
3. Read the lines corresponding to the timestamps indicated in `TIMED_NARRATION_SCRIPT.md`.
4. If you misspeak on any sentence, pause, back up 5 seconds on the timeline, and re-record that clip.

---

## 3. Demo Screencast Details (`demo_codex_review.mp4`)

* **Source File:** `demo_codex_review.mp4` (Duration: 2:52, 172.03s, 1920x1080 @ 30fps).
* **Location in Master Video:** Starts at `3:25` and ends at `6:17`.
* **Visual Annotations Included in Demo:**
  - `3:25–4:10`: Prompt submission, shortened generation wait badge (`Agent wait shortened`), test suite completion (`All 9 tests pass ✅`).
  - `4:10–5:05`: `/review` trigger, scope selection (`Review uncommitted changes`), highlighting the P2 finding on lines 26–32 (`Orphaned file on disk-full failure`).
  - `5:05–5:40`: Hovering line 26, clicking `+`, adding inline comment, composer follow-up directive.
  - `5:40–6:00`: Minimal cleanup diff inspection (`+6 −6 lines`), regression test passing (10 tests).
  - `6:00–6:17`: Final verification `/review` showing `No actionable issues found`.

---

## 4. Resetting the Demo Project for Live Re-Recording

If you ever wish to re-record the live screencast demo yourself inside the Codex app:
1. Open PowerShell terminal in `photo-take`:
   ```powershell
   cd G:\ReplitProjects\pluralsight-openai-codex-auditions\photo-take
   git checkout -- .
   git clean -fd
   ```
2. Verify with `git status` that the working tree is clean.
3. In the Codex app, open `photo-take` and start a new thread.
4. Follow the exact prompts listed in `CODEX_PROMPTS.txt`.

---

## 5. Pluralsight Audio & Video Checklist

- [x] **Resolution:** 1920×1080 (16:9 full HD).
- [x] **Timing:** 7:12 (strictly inside the 5 to 8 minute window).
- [x] **Mouse Discipline:** No circling, dragging, or cursor highlighting; all focus guided by static bounding callouts.
- [x] **Audio Target:** 44.1kHz or 48kHz, mono or stereo, clear tone with no background fan/keyboard noise.
- [x] **Slide 4 Correction:** Displays pre-review code without cleanup logic, validating the "Ah-ha!" review moment.
