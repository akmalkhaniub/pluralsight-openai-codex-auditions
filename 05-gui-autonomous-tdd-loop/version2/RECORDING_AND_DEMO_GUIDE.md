# Recording & Demo Guide — TDD with OpenAI Codex (Codex app on Windows)

This guide covers when to switch between slides and the demo, how to record the pieces, and the exact demo steps.

---

## 1. The flow

```
 SLIDES 1–6            DEMO in Codex app              SLIDES 7–8
 0:00 ─────── 3:00 ──► 3:00 ─────────── 6:30 ──► 6:30 ─── 7:15
 Title → Overview →    Red → read tests → prompt →   Summary →
 Boundary → Cycle →    review diff → Green →         Practice
 Prompt → Demo roadmap Refactor → close ticket
```

- **Slides → demo:** at the end of slide 6, on the line *"Let's open the editor."*
- **Demo → slides:** after the demo's last line, *"…Let's step back and sum up."* Then show slide 7.
- Only these two switches happen. The demo is one continuous block.

---

## 2. How to record: yes, in separate pieces, then merge

Record three video clips and one voice track, then join them in a video editor (Camtasia, DaVinci Resolve, Clipchamp or similar).

| Clip | What you record | How |
|------|-----------------|-----|
| **A: Slides 1–6** | PowerPoint Slide Show, clicking through the builds | Screen recorder at full screen, 1920×1080 |
| **B: Demo** | The Codex app on Windows, following section 4 | Screen recorder, same resolution |
| **C: Slides 7–8** | Slide Show starting at slide 7 | Same as A |
| **Voice** | Your narration (the script) | USB mic into its own audio track |

**Why separate pieces:**
- A mistake in the demo means redoing only clip B, not the whole video.
- Pluralsight wants clean audio on its own track, so you can remove noise and typing sounds.
- Waiting for Codex can be cut or sped up in clip B without affecting your voice.
- In the editor, join the clips with a straight cut or a 0.3-second crossfade. Don't use flashy transitions.

**Two ways to handle the voice:**
1. **Talk while recording** (easiest). Speak the script as you click, but record the mic as a separate track, not mixed into the screen audio. Afterwards, cut long waits from both tracks together.
2. **Voice-over afterwards** (cleanest). Record the screen silently, then record narration while watching the clip, and line them up. This is better for the demo because typing and waiting don't sound awkward.

A common mix is option 1 for the slides and option 2 for the demo.

---

## 3. One-time setup (checked in a real run on your PC, 27 Sep 2026)

**Project folder: already prepared.** `G:\ReplitProjects\pluralsight-openai-codex-auditions\audition-take` contains the starting code, a `.gitignore` and two Git commits. It is at the red state (8 errors) and has already been added and trusted in the Codex app as the **audition-take** project.

To make a fresh one yourself later:
```powershell
Copy-Item "G:\ReplitProjects\pluralsight-openai-codex-auditions\05-gui-autonomous-tdd-loop\version2\demo-code" "G:\audition-take2" -Recurse
cd G:\audition-take2; git init; git add .; git commit -m "Red: starting point"
```
Then, in the Codex app: **Ctrl + O** → the "Select Project Root" dialog → select the folder → **Select Folder** → "Trust this folder?" → **Trust folder**.

**What the app looks like (verified)**
| Thing | Where / how |
|-------|-------------|
| New thread | Click the project name (**audition-take**) in the left sidebar, then type in the **Do anything** box |
| Permission control | **Approve for me**, under the composer. The default worked: Codex ran the tests with no approval prompt |
| Model picker | Bottom right of the composer (it showed "GPT-6 Astra Medium") |
| Integrated terminal | **Ctrl + J**, opens PowerShell at the bottom, already in the project folder |
| Codex's commands | Click **Worked for …** above an answer to expand what it ran |
| While Codex edits | A **1 file changed +5 −2** chip appears above the composer |
| Result card | **Edited discount_service.py +5 −2**, with **Undo** and **Review** buttons |
| Review panel | Click **Review** to open a **Review** tab with a **Last Turn** menu and a side-by-side diff. The expand button (top right) widens it |

**Speed:** each Codex request took **about 2 minutes** on your PC. Keep recording and cut the waits in editing, labelling each cut "Agent wait shortened".

**⚠ Terminal warning:** don't paste multi-line text into the integrated terminal. PowerShell runs every pasted line as a command. Type single commands, or let Codex run the tests; that is what the steps below do.

**Screen hygiene checklist**
- [ ] Focus Assist / Do Not Disturb on; close Slack, email and the browser.
- [ ] Record the app on **one** monitor (it opened on the laptop screen, 1366×768). For a sharper video, move the app to the Samsung monitor and record at 1920×1080.
- [ ] Zoom in (Ctrl + =) so the thread and diff text is readable.
- [ ] Only the **audition-take** thread visible. Start a new thread for each take and delete or archive the practice ones.
- [ ] The Windows "Activate Windows" watermark shows in the bottom-right corner. Activate Windows, or crop or cover it in editing.
- [ ] Prompts ready in Notepad, off-screen, to copy.

---

## 4. Demo steps in the Codex app (clip B, 3:00–6:30)

See **demo_reference_storyboard.mp4** for the real screens from the practice run, with the callouts in place.

### Step 1 · Red (3:00–3:30)
| Do | You'll see (real run) | Callout |
|----|-----------------------|---------|
| New thread. Type: `Run python -m unittest -v test_discounts and show me the summary. Do not change any files yet.` and press Enter | After the wait: "8 tests ran in 0.301s; all 8 errored", "NotImplementedError… discount_service.py (line 6)", "Exit code: 1", "No files were edited." | "8 errors: expected, the code is missing" / "NotImplementedError, not a failed assertion" |
| Click **Worked for …** | The command Codex ran | — |

### Step 2 · Read two tests (3:30–4:00)
Ctrl + J, then type `Get-Content .\test_discounts.py` (a single line) and scroll to the two tests. Or open the file in your editor.
Callouts: `100.00 → 90.00` and `100.05 → 90.05`.

### Step 3 · Prompt Codex (4:00–4:45)
| Do | You'll see (real run) | Callout |
|----|-----------------------|---------|
| Paste the **IMPLEMENTATION PROMPT** (as one paragraph) and send | "Running Get-Content BUSINESS_RULES.md…", then "Editing files", then the **1 file changed +5 −2** chip | "SCOPE: one editable file", "PROOF: the test command" |
| Wait | "Changed only discount_service.py… The tests agree with the business rules… all 8 tests passed", plus the **Edited discount_service.py** card | "Claim: all 8 tests pass" |

### Step 4 · Review the diff (4:45–5:10)
| Do | You'll see (real run) | Callout |
|----|-----------------------|---------|
| Click **Review** on the card, then the expand button | Last Turn +5 −2; only `discount_service.py`; new lines `total = order_amount`, `if order_amount >= Decimal("100.00"):`, `total = order_amount * Decimal("0.90")`, `return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)` | ">= includes the $100 customer", "Round once, half up, at the end" |

### Step 5 · Green (5:10–5:30)
Show Codex's "all 8 tests passed" line. Optionally prove it yourself: Ctrl + J → `python -m unittest -v test_discounts` → `Ran 8 tests … OK`.

### Step 6 · Refactor decision (5:30–6:10)
| Do | You'll see (real run) | Callout |
|----|-----------------------|---------|
| Paste the **REFACTOR PROMPT** in the same thread | "No useful refactor is needed. calculate_total already computes the amount first and rounds once with ROUND_HALF_UP. No files were changed… all 8 tests passed" | "No useful refactor: already rounds once", "Same 8 tests still pass" |

If a different run produces code that rounds twice, Codex will refactor instead. Show that diff; the script has the matching lines.

### Step 7 · Close the ticket (6:10–6:30)
Show the thread with the green result. Callouts: "Covered: threshold, rounding", then "Not yet: negative amounts". Say *"…Let's step back and sum up."*, then **stop the demo recording**.

---

## 5. Resetting between takes

In PowerShell (or Ctrl + J in the app):
```powershell
cd G:\ReplitProjects\pluralsight-openai-codex-auditions\audition-take
git checkout -- discount_service.py
python -m unittest test_discounts     # confirm errors=8 again
```
Then start a **new thread**, so Codex doesn't remember the previous attempt.

---

## 6. If something goes differently

| Situation | What to do on camera |
|-----------|----------------------|
| A test still fails after Codex's first attempt | Keep recording. Read the failure, compare it with the rule and ask Codex to fix it. Real diagnosis is good teaching. |
| Codex edits `test_discounts.py` | The review panel lists it and the fingerprint check fails. Say so, **revert** that file in the review panel, restate the scope and rerun. Strong material, so keep it. |
| Codex can't run the tests itself (sandbox or approval) | Approve the command if asked, or run it in the integrated terminal yourself; the result is what counts. |
| A long wait | Keep recording; cut it in editing and add the "Agent wait shortened" label. |
| You stumble on words | Pause, repeat the sentence and cut the mistake later. Only the audio changes. |

---

## 7. Editing checklist

- [ ] Order: clip A → clip B → clip C, straight cuts or short crossfades.
- [ ] Noise reduction on the voice track; remove typing and clicking sounds.
- [ ] Add every callout marked above; keep each on screen 3–5 seconds, in the same colours as the slides (pink or yellow).
- [ ] Label every sped-up or cut wait "Agent wait shortened".
- [ ] Zoom in (1.5–2×) on code during the diff review if the text is small.
- [ ] Final length between **5 and 8 minutes** (target 7:15).
- [ ] Export as 1080p MP4 and watch it once end to end before submitting.

---

## 8. Rehearse first

Run `python verify_demo.py` in the `version2` folder. It confirms the red, green and refactored checkpoints behave as expected. Then do one full, timed dry run of steps 1–7 in a fresh take folder.

---

## References (Codex app)
- ChatGPT desktop app for Windows: https://learn.chatgpt.com/docs/windows/windows-app
- Code review / review panel: https://learn.chatgpt.com/docs/code-review?surface=app
