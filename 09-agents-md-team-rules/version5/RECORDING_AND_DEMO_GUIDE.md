# Recording & Demo Guide: Team Rules for OpenAI Codex with AGENTS.md (Codex app on Windows)

This guide covers when to switch between slides and the demo, how to record the pieces, and the exact demo steps. The demo was rehearsed in your Codex app on 27 Sep 2026; `demo_reference_storyboard.mp4` shows the real screens with callouts.

---

## 1. The flow

```
 SLIDES 1–12           DEMO in Codex app            SLIDES 13–15
 0:00 ─────── 3:00 ──► 3:00 ─────────── 6:30 ──► 6:30 ─── 7:15
```

- **Slides → demo:** end of slide 12, on *"Let's open Maliha's repo."*
- **Demo → slides:** after *"So how did Friday end?"* Then show slide 13 (Friday).

## 2. How to record: three clips plus a voice track

| Clip | What | How |
|------|------|-----|
| **A** | Slides 1–12 in PowerPoint Slide Show | Screen recorder, full screen, 1920×1080 |
| **B** | The demo in the Codex app (section 4) | Same recorder and resolution |
| **C** | Slides 13–15 | Same as A |
| **Voice** | The narration script | USB mic on its own audio track |

Join A → B → C in Camtasia, Clipchamp or DaVinci Resolve with straight cuts. Recording the demo screen first and adding your voice afterwards usually sounds best, because the waits are long.

## 3. One-time setup (already done on your PC)

- The project folder **`agents-take`** is in `G:\ReplitProjects\pluralsight-openai-codex-auditions`, with Git history. It has already been added and trusted in the Codex app.
- The ready-made file you'll copy in during the demo is in **`agents-kit\AGENTS.md`**, next to it.
- After the rehearsal, `agents-take` was reset to its clean state with **no AGENTS.md**, ready to record.

**Codex app basics (verified)**

| Thing | Where / how |
|-------|-------------|
| New thread in the project | Hover the project name in the sidebar and click the **new chat** icon beside it. The screen says "What should we build in agents-take?" |
| Permission control | **Approve for me**, under the composer (the default worked) |
| Integrated terminal | **Ctrl + J** (PowerShell). **Type single commands only; never paste several lines**, because each line runs |
| Codex's commands | Click **Worked for …** to expand what it ran |
| Result card | **Edited &lt;file&gt; +N −M**, with **Undo** and **Review** |
| Review panel | **Review** → **Last Turn** → expand button (top right) for full width |

**Screen hygiene**
- [ ] Focus Assist on; close Slack, email and the browser.
- [ ] **Move the Claude app window off the recording screen.** During the rehearsal it kept appearing over the Codex app.
- [ ] Zoom the app (Ctrl + =), record one monitor, and cover or activate the "Activate Windows" watermark.
- [ ] Prompts from `CODEX_PROMPTS.txt` ready in Notepad, off-screen.

**Waiting:** requests took **3–8 minutes each** during the rehearsal. The first one also hit a Git "dubious ownership" warning, which Codex worked around by itself. Record everything and cut the waits, labelling each cut "Agent wait shortened".

---

## 4. Demo steps (clip B, 3:00–6:30)

### Step 1 · Without rules (3:00–3:45)
New thread in **agents-take**. Paste the task prompt from `CODEX_PROMPTS.txt`:
`Add apply_coupon(total, code) to shop/pricing.py. SAVE10 takes 10% off the total; any other code is invalid.`
Callout: "Same prompt both times". Cut the wait.

### Step 2 · Spot the gaps (3:45–4:15)
**Review** → expand. See the rehearsal results table in `README.md` for what Codex produced. Put callouts on each missing team rule (the rehearsal run raised `ValueError` and left `CHANGELOG.md` untouched).

### Step 3 · Add AGENTS.md (4:15–4:40)
**Undo** on the result card. Ctrl+J, type (one line): `Copy-Item ..\agents-kit\AGENTS.md .` Then show the file (`Get-Content AGENTS.md`). Callout: "Repo root".

### Step 4 · Same task again (4:40–5:05)
**New thread** (rules load when a task starts). Paste the identical prompt. Cut the wait.

### Step 5 · Compare (5:05–6:05)
**Review** → expand. Callouts on `AppError("INVALID_COUPON", …)`, the docstring `Example:` line, the new tests, and `CHANGELOG.md` in the changed-files list. Expand **Worked for …** to show `python -m unittest discover -s tests -v`.

### Step 6 · Close (6:05–6:30)
Show AGENTS.md beside the changed files and say the closing line. Stop the recording.

---

## 5. Resetting between takes

```powershell
cd G:\ReplitProjects\pluralsight-openai-codex-auditions\agents-take
git checkout -- .
Remove-Item AGENTS.md -ErrorAction SilentlyContinue
git clean -n    # lists leftover new files; run git clean -f to remove them
```

Always start a **new thread** for each take.

---

## 6. Editing checklist

- [ ] Order: A → B → C; straight cuts.
- [ ] Noise reduction on the voice; remove clicks and typing.
- [ ] Add each callout listed above for 3–5 seconds. Pink = key fact, yellow = attention.
- [ ] Label every cut wait "Agent wait shortened".
- [ ] Zoom 1.5–2× on the diff when the text is small.
- [ ] Final length **5–8 minutes** (target 7:15). Export 1080p MP4 and watch it once before submitting.
