# Voice-over script: demo_codex_review.mp4 (28 Sep run)

**Video:** 2:52, silent. It opens with a 5-second title card and ends with a 5-second "Back to slides" card.
**For the audition:** cut both cards and use 0:05–2:47 (2:42), which fits your 3:25–6:17 slot.
Read each block when its time comes up, and pause for a beat at each `·`.

---

## The Feature Developer

**0:05–0:15 · empty project**
Here we are in a clean bookshop project, photo-take: users, a profile page, and a couple of tests.

**0:15–0:27 · prompt in the composer**
I'll paste our feature request: let users upload a profile photo, save it under avatars, update the avatar URL, and add tests.

**0:27–0:33 · Codex working (agent wait shortened)**
Codex reads the project, writes the function, and runs the tests.

**0:33–0:47 · "All 9 tests pass", "Edited 2 files"**
And there it is. · All nine tests pass. Two files changed. · The Feature Developer met the ticket. · But are we ready to commit? · Not yet.

## The Senior Reviewer

**0:47–0:59 · /review menu**
Let's put on the Senior Reviewer's hat. · Slash review, and I'll choose Review uncommitted changes.

**0:59–1:07 · review mode**
Codex is in review mode now. · It reads. It changes no code.

**1:07–1:21 · "One issue found"**
And look what it caught. · One issue, priority two. · All nine tests pass, but if the disk fills up while a photo is saving, a half-saved file is left behind.

**1:21–1:39 · the comment on lines 26–32**
Here's the comment, right on the lines that save the file. · Codex even says it reproduced the failure. · The Feature Developer tested the sunny day. · The Senior Reviewer asked what could go wrong.

## Point at the line

**1:39–1:53 · + on line 26, your comment**
I agree, so I'll point at the line: plus, and one sentence. · If saving fails, delete the half-saved file, and add a test for it.

**1:53–2:05 · follow-up message**
Then in the composer: address the inline comments, and keep the scope minimal. · Send.

## The surgical fix

**2:05–2:19 · "10 tests now pass"**
Codex fixed the cleanup and added a test that failed before the fix. · Ten tests pass now.

**2:19–2:33 · Last Turn diff, +6 −6**
And Last Turn shows only this change. · Six lines in, six lines out. · No surprise rewrites.

## The clean re-review

**2:33–2:47 · "No actionable issues found"**
One final check: slash review again. · No actionable issues found. · Now, and only now, we're ready to commit. · Let's see the side-by-side.
