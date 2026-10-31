# Demo script v4 (revised): full sentences

**Video:** `demo_v4_silent.mp4` (2:36). Steady view, no zoom; each callout sits on its target.
**Rehearsal video:** `demo_v4_CUES.mp4` shows each sentence in large text at the lower middle, with the next sentence underneath.

**Markers:**
- **‖** = pause about half a second; let the screen land.
- ***Bold italic*** = stress this word (shown in yellow in the cue video).

**Tips:** rehearse 2–3 times until it feels like explaining to a colleague. Speak a little quicker than last time, and keep going through small slips; I'll tidy the pauses.

### 0:00.0 · The Feature Developer
Here's a small bookshop app called ***photo-take***. ‖ It has users, a profile page, and a couple of tests.

### 0:10.1 · The Feature Developer
Let's ask Codex for a new feature, in plain English. ‖ Let users upload a profile photo, save it under avatars, and add tests.

### 0:22.4 · The Feature Developer
Codex reads the project, writes the code, and runs the tests. ‖ I've shortened the wait here.

### 0:31.7 · The Feature Developer
And there it is. ‖ All ***nine*** tests pass, and two files changed. ‖ Most of us would ship this right now. ‖ But are we ready to commit? ‖ ***Not yet.***

### 0:48.3 · The Senior Reviewer
Let's switch hats, to the ***Senior Reviewer***. ‖ I type slash review, and choose ***Review uncommitted changes***.

### 0:57.5 · The Senior Reviewer
Now Codex is in review mode. ‖ It ***reads*** the code, but it ***changes nothing***.

### 1:05.9 · The Senior Reviewer
And look what it found. ‖ ***One issue***, even though all nine tests are still green.

### 1:14.7 · The Senior Reviewer
Here's the comment, right on the lines that save the file. ‖ If the disk fills up while a photo is saving, we're left with a ***half-saved, broken file***. ‖ Codex even reproduced it. ‖ The Feature Developer tested the sunny day. ‖ The Senior Reviewer asked, ***what could go wrong?***

### 1:39.6 · Point At The Line
I agree, so I'll point at that exact line. ‖ Click the ***plus***, and write one sentence. ‖ If saving fails, delete the half-saved file, and add a test for it.

### 1:55.2 · Point At The Line
Then one short message. ‖ Address the inline comments, and ***keep the scope minimal***.

### 2:03.1 · The Surgical Fix
Codex fixes the cleanup, and adds a test that ***failed before the fix***. ‖ Now ten tests pass.

### 2:12.8 · The Surgical Fix
Switch the view to ***Last Turn***, and you see just this change. ‖ Six lines in, six lines out. ‖ Nothing else touched.

### 2:24.9 · Clean Re-Review
One last check. ‖ Slash review again, and, ***no actionable issues***. ‖ Now, and only now, we're ready to commit.
