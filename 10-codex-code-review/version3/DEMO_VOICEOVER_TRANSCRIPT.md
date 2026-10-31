# Demo voice-over transcript: demo_codex_review_v3.mp4

**Length:** 2:52 (fits your clip B slot, 3:25–6:17).
**Recorded:** a real run in your Codex app on 5 Oct 2026 (GPT-6.1 Sol Light).
**How to use:** play the video, read each block when its time comes up, and pause for a beat at each `·`. The left time is inside this clip; the bracketed time is the full audition.

This run differs from the earlier script in a few places. The narration below matches what is on screen:

- **6 tests pass** (not 9).
- **The finding** is that an unusual file name crashes a valid upload (not the disk-full one).
- **The fix** is 2 lines (not +6 −6), and 7 tests pass after it.
- **No + comment box:** in this app version the **+** only highlights the line, so the fix request is typed in the composer.

---

## SCENE 1 · The Feature Developer · 0:00–0:45 (3:25–4:10)

**0:00–0:06 · clean project**
Here we are in a clean bookshop project, photo-take.

**0:06–0:16 · prompt in the composer**
I'll paste our feature request: let users upload a profile photo, save it under avatars, update the avatar URL, and add unit tests.

**0:16–0:23 · "Thinking" (agent wait shortened)**
Codex reads the project, writes the function, and runs the tests.

**0:23–0:45 · "All 6 tests passed", "Edited 2 files"**
And there it is. · All six unit tests pass, and two files changed. · The Feature Developer met the ticket and thinks the job is done. · But are we ready to commit? · Not yet.

---

## SCENE 2 · The Senior Reviewer · 0:45–1:40 (4:10–5:05)

**0:45–0:55 · /review menu**
Let's put on the Senior Reviewer's hat. · I'll type slash review, and pick Code review.

**0:55–1:03 · review mode (agent wait shortened)**
Codex switches to review mode. · It only reads. It changes no code.

**1:03–1:18 · "one actionable issue", P2 on line 20**
And look what it caught. · One actionable issue, priority two, on line twenty. · All six tests were green, and the bug was still there.

**1:18–1:40 · the comment on the line**
Here's the comment, right on the line. · Some uploads arrive with a number instead of a text file name. · When that happens, this line crashes, and a perfectly valid photo upload fails. · The Feature Developer tested the sunny day. · The Senior Reviewer asked what could go wrong.

---

## SCENE 3 · Point at the line · 1:40–2:15 (5:05–5:40)

**1:40–1:53 · + on line 20**
We won't re-prompt from scratch. · I'll point at the exact line. Hovering here shows the plus, and it marks line twenty.

**1:53–2:15 · the follow-up message**
Then one targeted request: fix the review comment on line twenty. If the name isn't text, fall back to PNG. · Add a test for it, and keep the scope minimal. · Send.

---

## SCENE 4 · The surgical fix · 2:15–2:35 (5:40–6:00)

**2:15–2:22 · "Fixed", "All 7 tests passed"**
Codex fixed it, and added a regression test. · Seven tests pass now.

**2:22–2:29 · the two-line fix**
The whole fix is two lines: if the name is text, use it. Otherwise, use PNG.

**2:29–2:35 · Last Turn**
And Last Turn shows only this change. · Nothing else touched.

---

## SCENE 5 · The clean re-review · 2:35–2:52 (6:00–6:17)

**2:35–2:52 · "No actionable issues"**
One final check: slash review again. · No actionable issues found. · Now, and only now, we're ready to commit. · Let's see the side-by-side.

---

## Recording tips

- **Pace:** about 110–130 words a minute. Every block fits its time with room to breathe.
- **One block at a time:** record each block as a separate take. It's easier to sync, and a flub only costs one block.
- **Syncing:** in your editor, place each take where its block starts on the video. If a take runs short, leave the silence; the frame holds.
- **Slide 9:** it still says "9 tests pass" and "Disk full? A broken file is left behind". To match this run, change those rows to "6 tests pass" and "Odd file name? Valid upload crashes", and the right column to "Odd names fall back to .png". Or keep the slides and use the earlier demo video, which matches them.
