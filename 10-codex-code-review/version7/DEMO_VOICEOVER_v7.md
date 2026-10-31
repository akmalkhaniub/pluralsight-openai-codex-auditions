# Demo voice-over v7 (live recording)

**Video:** `demo_v7_silent.mp4`, 1:58, edited from your live run on 24 Oct, with the waits cut and callouts added.

**How to read it:**
- One line = one breath.
- Start each block when its time comes up. If you finish early, just pause; the screen holds.
- ***Bold italic*** marks the word to stress.
- You can record it in 2 or 3 takes (for example 0:00–0:58 and 0:58–end), and I'll join them.

---

### 0:00 · The Feature Developer *(new thread, prompt sent)*
Here's our little bookshop app, photo-take.  
I'll ask Codex for a feature, in plain English.  
Let users upload a profile photo.  
A quick first version, with a test.  

### 0:12 · *(Agent wait shortened)*
Codex reads the project, writes the code, and runs the test.  

### 0:15 · *(All 3 tests pass, 2 files edited)*
And there it is.  
All ***three*** tests pass, and two files changed.  
So, can we commit?  
***Not yet.***  
Remember Friday afternoon?  

### 0:25 · The Senior Reviewer *(typing /review)*
Time to switch hats.  
I type ***slash review***,  
and add the senior reviewer's questions.  
What if it fails halfway? Who can call this? Empty or huge input?  

### 0:34 · *(Agent wait shortened)*
Codex hands this to a separate reviewer.  

### 0:37 · *(the findings)*
And look at that.  
***Four*** findings, even though every test was green.  
Two of them are priority one.  
Here's one, right on the line.  
Any caller can change ***anyone's*** photo.  
Another one: a failed upload leaves a half-saved file behind.  
That's our Saturday, two am.  

### 0:58 · The Small Fix *(typing the fix message)*
Now, ***I*** decide.  
Fix the findings, with a test for each, and keep the scope minimal.  
Authorization needs a real login system, so that becomes a follow-up ticket.  

### 1:12 · *(Agent wait shortened)*
Codex makes the fixes.  

### 1:16 · *(3 fixed, 6 tests pass)*
Partial files are cleaned up.  
Empty uploads are rejected.  
Huge ones are capped.  
A new test for each, and all ***six*** tests pass.  

### 1:24 · Review Again *(running /review)*
One last check.  
Slash review, again.  

### 1:36 · *(Agent wait shortened)*
Same reviewer, fresh eyes.  

### 1:40 · *(Clean re-review)*
***No actionable issues.***  
The cleanup, the empty check, and the size limit all look right.  
Authorization is safely on a ticket.  
Now, and only now, we're ready to commit.  
Let's compare the two versions.  

---

**About 210 words, so roughly 1:40 of speech in a 1:58 video. That leaves room to breathe.**
