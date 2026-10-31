# Recording & Demo Guide: Code Review with Codex (Codex app on Windows)

## 1. The flow

```
 SLIDES 1–8            DEMO in Codex app            SLIDES 9–11
 0:00 ─────── 3:25 ──► 3:25 ─────────── 6:40 ──► 6:40 ─── 7:35
```

- **Slides → demo:** end of slide 8, on *"Let's open the app."*
- **Demo → slides:** after *"Let's compare the two versions."* Then show slide 9.

## 2. How to record: three clips plus a voice track

| Clip | What | How |
|------|------|-----|
| **A** | Slides 1–8 in PowerPoint Slide Show | Screen recorder, full screen, 1920×1080 |
| **B** | The demo in the Codex app (section 4) | Same recorder and resolution |
| **C** | Slides 9–11 | Same as A |
| **Voice** | The narration script | USB mic on its own track |

Join A → B → C with straight cuts. Add callouts in editing and keep each on screen 3–5 s. Cut every Codex wait and label it "Agent wait shortened".

## 3. One-time setup

- The demo project **`photo-take`** is in `G:\ReplitProjects\pluralsight-openai-codex-auditions` (a Git repo: users, a profile rename function, 2 tests).
- In the Codex app: **Ctrl+O** → navigate to `photo-take` → **Select Folder** → **Trust folder**.
- Screen hygiene: Focus Assist on, one monitor, app zoomed in, no cursor pointing.

## 4. Demo steps (clip B, 3:25–6:40), verified in your Codex app on 28 Sep 2026

`demo_codex_review.mp4` shows every step with real screenshots and callouts.

1. **The writer.** Hover `photo-take` in the sidebar → new-chat icon. Paste PROMPT 1 into the composer and send. It took about 9.5 minutes (cut it). Result: "Edited 2 files", "All 9 tests pass".
2. **The editor.** Type `/review` and press Enter → pick **Review uncommitted changes**. It took about 2.5 minutes (cut it). Result: "One issue found. All 9 tests pass, but a simulated disk-full failure leaves an orphaned upload file." The Review pane opens; the **P2** comment sits on lines 26–32.
   - If the Review pane shows "No file changes yet", its scope switched to **Branch**: open the scope menu (top left of the pane), hover **Unstaged**, press Enter.
3. **Point at the line.** In the Review pane, hover line 26 (`with destination.open(...)`) → click **+** → type the comment → **Comment**. In the composer ("1 comment" shows), send: "Address the inline comments and keep the scope minimal."
4. **The small fix.** About 3 minutes (cut). Result: cleanup fixed, a regression test that failed before the fix, 10 tests pass. Set the Review scope to **Last Turn** to show only the fix (+6 −6 in profile.py).
5. **Review again.** `/review` → **Review uncommitted changes**. About 1.5 minutes (cut). Result: "No actionable issues found."

## 5. If the finding is different on your take

Codex's wording varies between runs. If it reports something else first (file type, file name, size), use that: say what could go wrong in one sentence, comment on that line, and change slide 9's red row. If there are no findings, say so, add your own comment, and continue.

## 6. Reset between takes

In the Codex app, **Undo** the changes (or in a terminal outside the demo: `git checkout -- .` and `git clean -fd` (this also removes the avatars/ folder) in `photo-take`), then start a new thread.

## 7. Editing checklist

- [ ] Clips A, B, C join cleanly; total 7–8 minutes
- [ ] Every wait cut and labelled
- [ ] Callouts on: tests pass, the finding, the + comment, the size check and test, the clean re-review
- [ ] No cursor pointing; no notifications; "Activate Windows" covered
