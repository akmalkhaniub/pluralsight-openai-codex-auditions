# Demo script v5

Pauses are shown as extra space between phrases. ***Bold italic*** = stress this word.

### 0:00.0 · The Feature Developer
Here's a small bookshop app called ***photo-take***.      It already has users, a profile page, and a couple of unit tests.      It's a typical project you might hand to Codex for a quick feature.

### 0:14.8 · The Feature Developer
Let's ask Codex for a new feature, in plain English.      Let users upload a profile photo, save it under avatars, update the avatar URL, and add tests.      That's all the instruction it needs.

### 0:29.6 · The Feature Developer
Codex now reads the project, works out where the change belongs, writes the code, and runs the tests on its own.      This normally takes a few minutes, so I've shortened the wait here.

### 0:44.0 · The Feature Developer
And there it is.      All ***nine*** tests pass, and two files changed.      Most of us would ship this right now.      But are we ready to commit?      ***Not yet.***

### 0:57.5 · The Senior Reviewer
This is where we switch hats, to the ***Senior Reviewer***.      I type slash review, and Codex asks what to review.      I choose ***Review uncommitted changes***, which is exactly what Codex just wrote.

### 1:12.0 · The Senior Reviewer
Codex is now in review mode.      It ***reads*** the code and looks for real risks, but it ***doesn't change anything***.      You stay in control of what gets fixed.

### 1:24.8 · The Senior Reviewer
And look what it found.      ***One issue***, even though all nine tests are still green.      Passing tests only prove the cases someone thought to test.

### 1:36.3 · The Senior Reviewer
Here's the comment, right on the lines that save the file.      If the disk fills up while a photo is being saved, the upload fails, but a ***half-saved, broken file*** stays behind in the avatars folder.      Codex even reproduced the failure to confirm it.      This is exactly the kind of production problem a good reviewer catches before it ships.

### 2:01.9 · Point At The Line
I agree with this finding, so I'll point at that exact line.      Hover over it, click the ***plus***, and write one clear sentence.      If saving fails, delete the half-saved file, and add a test for it.

### 2:17.9 · Point At The Line
Then I send one short message.      Address the inline comments, and ***keep the scope minimal***.      That tells Codex to fix this one problem, and nothing else.

### 2:29.9 · The Surgical Fix
Codex fixes the cleanup, and adds a new test that ***failed before the fix***.      Now all ten tests pass, so we know the bug is really covered.

### 2:41.9 · The Surgical Fix
Switch the view to ***Last Turn***, and you see only this change.      Six lines in, six lines out.      No surprise rewrites, and nothing else touched.

### 2:53.6 · Clean Re-Review
One last check.      Slash review again, and this time, ***no actionable issues***.      Now, and only now, we're ready to commit.      Let's compare the two versions side by side.
