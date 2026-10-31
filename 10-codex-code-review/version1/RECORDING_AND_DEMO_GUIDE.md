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

## 4. Demo steps (clip B, 3:25–6:40)

1. **The writer.** Hover `photo-take` in the sidebar → new-chat icon. Paste PROMPT 1 from `CODEX_PROMPTS.txt` (paste into the composer, never into the terminal). Send. Wait (cut). Callout on "tests pass".
2. **The editor.** Type `/review` → choose **Last turn**. Wait (cut). The review pane shows findings as comments on the lines. Box the one about the upload.
3. **Point at the line.** Hover the line that writes the file → **+** → "Reject files over 5 MB here." Send: "Address the inline comments and keep the scope minimal."
4. **The small fix.** Open the result card → **Review**. Callouts on the size check and the new test. Show the changed-file count.
5. **Review again.** `/review` → **Last turn**. The upload finding is gone.

## 5. Which finding to use

Codex's wording varies. Likely findings on an upload, in order of preference for the story:

| Finding | What to say |
|---|---|
| No limit on file size | "Someone can upload a 2 GB file and fill the disk." (matches the slides) |
| Any file type accepted | "Someone can upload a script instead of a photo." Change the payoff row to "Only images are accepted." |
| Unsafe file name or path | "A crafted name could write outside the avatars folder." |
| No findings | Say so honestly; add your own comment on the write line and continue. The lesson still holds: you decide. |

## 6. Reset between takes

In the Codex app, **Undo** the changes (or in a terminal outside the demo: `git checkout -- .` and `git clean -fd` in `photo-take`), then start a new thread.

## 7. Editing checklist

- [ ] Clips A, B, C join cleanly; total 7–8 minutes
- [ ] Every wait cut and labelled
- [ ] Callouts on: tests pass, the finding, the + comment, the size check and test, the clean re-review
- [ ] No cursor pointing; no notifications; "Activate Windows" covered
