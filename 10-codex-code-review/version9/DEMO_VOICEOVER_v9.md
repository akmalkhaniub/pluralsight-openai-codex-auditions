# Demo voice-over v9 (fuller script for the same demo video)

**Video:** the same `demo_v8_silent.mp4` (2:20). Only the script is longer, so there's less silence.

**Pace:** in your last take you spoke at about 190 words a minute and then waited. Start each block at its time and speak slowly, about 120 a minute; the blocks are sized to fill most of their slot.

**How to read it:**
- One line = one breath.
- Start each block at its time. If you finish early, just pause; the screen keeps moving.
- ***Bold italic*** marks the word to stress.
- `demo_v9_CUES.mp4` shows each block on screen at the right moment, so you can read along in CapCut.

---

### 0:00–0:15 · The Feature Developer
Here's the Codex app, with our bookshop project, photo-take.  
I'll start a fresh thread, and ask in plain English for a profile photo upload.  
A quick first version, with a test.  

### 0:15–0:29
Codex reads the project, writes the code, and runs the test. I've shortened the wait.  
And there it is: ***three*** tests pass, and two files changed.  
So, can we commit?  
***Not yet.***  

### 0:29–0:37 · The Senior Reviewer
Let's switch hats.  
I type ***slash review***, and add the senior reviewer's three questions.  

### 0:37–0:54
This time, a separate reviewer reads the changes.  
And look: ***three*** findings, even though every test was green.  
Two of them are priority one.  
The partial-file case is already handled, so it isn't flagged.  

### 0:54–1:14
Let's open the first one.  
It sits right on the line that copies the upload.  
There's no size limit, so one huge file could fill the disk.  
And here's another: an empty file would replace a working photo.  
That's our Saturday, two am.  

### 1:14–1:26 · The Small Fix
Now, ***I*** decide.  
Fix the findings, a test for each, and keep the scope minimal.  
Authorization needs a real login system, so it becomes a follow-up ticket.  

### 1:26–1:40
Before I accept anything, I check the diff.  
The file is now copied in chunks, and the size is checked as it goes.  
That's exactly what I asked for, so I accept it.  

### 1:40–1:48
All ***eight*** tests pass now,  
and authorization is safely on a ticket.  

### 1:48–1:55 · Review Again
One last check.  
Slash review again, with the same questions.  

### 1:55–2:15
And this time: ***no new findings.***  
Halfway failures are cleaned up.  
Empty and huge uploads are rejected.  
Authorization is still flagged, just as we planned.  
The reviewer agrees with the fix.  

### 2:15–2:20
And the tests agree.  
Now we're ready to commit.  

---

**About 276 words in 2:20.** That's a relaxed pace, about 118 words a minute, with room to breathe.
