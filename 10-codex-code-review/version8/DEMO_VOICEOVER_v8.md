# Demo voice-over v8 (live recording, 24 Oct)

**Video:** `demo_v8_silent.mp4`, 2:20. It's your live run, with the waits cut (each one labelled), smooth transitions, and animated callouts.

**How to read it:**
- One line = one breath.
- Start each block at its time. If you finish early, just pause; the screen keeps moving.
- ***Bold italic*** marks the word to stress.
- `demo_v8_CUES.mp4` shows each block on screen at the right moment, so you can read along in CapCut.

---

### 0:00–0:15 · The Feature Developer
Here's our little bookshop app, photo-take.  
I'll ask Codex for a feature, in plain English: let users upload a profile photo.  
A quick first version, with a test.  

### 0:15–0:29
Codex reads the project, writes the code, and runs the test.  
And there it is. All ***three*** tests pass, and two files changed.  
So, can we commit?  
***Not yet.***  

### 0:29–0:37 · The Senior Reviewer
Time to switch hats.  
***Slash review***, plus the senior reviewer's questions.  

### 0:37–0:54
And look at that.  
***Three*** findings, even though every test was green.  
Two of them are priority one.  
And notice: the partial-file case is already handled. Codex checked it.  

### 0:54–1:14
Here's the first one, right on the line.  
There's no size limit, so a huge upload could fill the disk.  
And another: an empty file would replace a working photo.  
That's our Saturday, two am.  

### 1:14–1:26 · The Small Fix
Now, ***I*** decide.  
Fix the findings, with a test for each, and keep the scope minimal.  
Authorization needs a real login system, so that becomes a follow-up ticket.  

### 1:26–1:40
Codex makes the fixes.  
Here's the diff: the size is checked while the file is copied.  
It looks right, so I accept it.  

### 1:40–1:48
All ***eight*** tests pass, and authorization is on a ticket.  

### 1:48–1:55 · Review Again
One last check.  
Slash review, again, with the same questions.  

### 1:55–2:15
***No new findings.***  
Halfway failures are cleaned up.  
Empty and huge uploads are rejected.  
And authorization is still flagged, just as we planned.  

### 2:15–2:20
And the tests agree.  
Now, and only now, we're ready to commit.  

---

**About 238 words in 2:20.** That's a relaxed pace, about 102 words a minute, with room to breathe.
