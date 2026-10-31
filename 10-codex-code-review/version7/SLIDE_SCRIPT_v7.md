# Slide script v7 (Parts A and C), matched to the live demo

**What changed from v5:**
- **Slower and more relaxed.** Aim for about 130–140 words a minute (v4 ran at about 180).
- **Conversational wording.** Linking words, questions to the viewer, and "you" and "we" instead of "teams".
- **A longer scenario.** There's a new slide 5, "What Happens If We Ship It?".
- **Slide 2.** It now shows the real Codex app.

**How to read it:**
- **One line = one breath.** Each new line is a natural pause; take a beat and let the idea land.
- **▸ *click*** means click to the next animation. Lines before the first click are said as the slide appears.
- ***Bold italic*** marks the word to stress.

**Length:** about 720 words, so roughly 5:45 for the slides at a relaxed pace. With a live demo of about 2:30–3:00, the audition comes to about 8½ minutes, well under the 10-minute limit.

**Recording in parts:**
- A1 = slides 1–3, A2 = slides 4–5, A3 = slides 6–9, C = slides 10–12.
- Stay quiet for 2 seconds at the start and end of each part.

**How to sound conversational:**
- **Learn it, don't read it.** Know each slide's one idea, then say it in your own words. Small changes in wording are fine.
- **Talk to one person.** Imagine a colleague sitting next to you.
- **Smile on the first line.** Start after a silent breath, not with one.
- **Click, then talk.** Let each animation appear, then explain it.

---

## Part A: before the demo

### Slide 1 · Title  *(A1)*
You know, Codex can build a feature for you in minutes.  
And that's great.  
But it raises a question: ***who reviews the AI?***  
Hi, I'm Akmal Khan, a Senior Full Stack AI Architect.  
And in this video, I'll show you one simple habit for shipping Codex code with confidence.  

### Slide 2 · Meet Codex
So first, let's meet Codex, OpenAI's coding agent.  
You describe a task in plain English, and it works just like a teammate.  
▸ *click*  
It reads your repository.  
▸ *click*  
It writes the change.  
▸ *click*  
It runs your tests.  
▸ *click*  
And then it hands the result back to ***you***, to review.  
▸ *click*  
Now, today we'll use the Codex app on Windows.  

### Slide 3 · Overview
But here's the catch.  
▸ *click*  
Writing code with Codex takes about ***five minutes***.  
▸ *click*  
But reviewing that code?  
Still about ***thirty***.  
▸ *click*  
So the slow part isn't writing anymore.  
▸ *click*  
It's ***review***.  
▸ *click*  
So what's in it for you?  
By the end of this video, Codex will do the first review for you.  
And you'll only spend your time on the risks that really matter.  
▸ *click*  
We'll get there in three steps: the Feature Developer, the Senior Reviewer, and the proof.  

### Slide 4 · The PR looks green  *(A2)*
Okay, let's make this real.  
▸ *click*  
Imagine it's Friday afternoon.  
You need a profile photo upload for a small bookshop app.  
▸ *click*  
Codex writes the code.  
▸ *click*  
All the tests pass.  
▸ *click*  
And it even handles errors.  
▸ *click*  
So, would you approve this pull request?  
▸ *click*  
Take a second.  
Honestly, most of us would.  
▸ *click*  
But hold that thought.  
▸ *click*  
Because tests only check what someone ***remembered*** to test.  
Not what we ***forgot***.  

### Slide 5 · What happens if we ship it?
So, let's say we approve it.  
What happens next?  
▸ *click*  
Friday, five pm.  
Tests green, PR approved.  
Everyone goes home happy.  
▸ *click*  
Saturday, two am.  
Something rare happens during an upload.  
And nobody tested for it.  
▸ *click*  
Monday morning.  
Broken profile photos.  
And the support tickets start piling up.  
▸ *click*  
And then comes the question nobody wants to hear: ***who approved this PR?***  
Sound familiar?  
▸ *click*  
Here's the thing.  
The fix takes minutes.  
But a bug in production costs your users, and your weekend.  
▸ *click*  
So today, I'll show you how to catch it ***before*** you click Approve.  

### Slide 6 · Second pair of eyes  *(A3)*
And that's exactly why good teams never approve their own pull requests.  
▸ *click*  
The Feature Developer asks: did I meet the ticket?  
▸ *click*  
But a Senior Reviewer asks something very different: ***what could break this in production?***  
▸ *click*  
Now, here's the nice part.  
Codex can wear both hats.  
Just never in the same prompt.  

### Slide 7 · Switch hats with /review
So how do we switch hats?  
In the Codex app, it's just one command.  
▸ *click*  
You type ***slash review***.  
▸ *click*  
And here's the trick: add the senior reviewer's questions.  
What if it fails halfway? Who can call this? What about empty or huge input?  
▸ *click*  
Codex reads the changes, and puts its findings right on the lines.  
▸ *click*  
And it ***doesn't change a thing***.  
You decide.  
▸ *click*  
A plain slash review is a quick general check.  
Add your questions, and it becomes a deep check.  
▸ *click*  
And that's what we'll do today.  

### Slide 8 · Decide, then fix small
Now, when the findings come in, ***you*** decide what to fix.  
▸ *click*  
Here's the code Codex wrote.  
▸ *click*  
And here's the risky line: it writes the file, with no cleanup if something fails.  
▸ *click*  
Codex flags it, right on that line: remove partial files when copying fails.  
▸ *click*  
Then you send one short message: fix the findings, with a test for each, and ***keep the scope minimal***.  
Anything bigger, like authorization, becomes a follow-up ticket.  
▸ *click*  
That way, you get small fixes, and nothing else changes.  
▸ *click*  
So that's the habit: ***build, review, commit***.  

### Slide 9 · Demo plan
Alright, here's our plan for the demo.  
▸ *click*  
First, Codex builds the photo upload as the Feature Developer.  
▸ *click*  
Then we switch hats: slash review, plus the reviewer's questions.  
▸ *click*  
We decide what to fix now, and what to defer.  
▸ *click*  
And finally, a small fix, and one more review.  
So let's open the Codex app.  

> **⏹ SWITCH → DEMO.** Stop recording here.

---

## Part C: after the demo

### Slide 10 · Side by side  *(C)*
Okay, let's put the two versions side by side.  
▸ *click*  
With only the Feature Developer, the upload worked,  
▸ *click*  
and all three tests passed.  
▸ *click*  
But four real risks were hiding in there.  
▸ *click*  
With the Senior Reviewer as well, it's the same feature, now with six tests,  
▸ *click*  
and three risks fixed, with authorization on a ticket.  
See?  
The tests were green both times.  
But ***the review made the difference***.  

### Slide 11 · Your turn
So here's the one habit I'd love you to take away.  
▸ *click*  
***Slash review.***  
▸ *click*  
After every Codex task, and before every commit.  
▸ *click*  
And when you read the findings, ask yourself three questions.  
▸ *click*  
What if it fails halfway?  
▸ *click*  
Who's allowed to call this?  
▸ *click*  
And what if the input is empty, or huge?  

### Slide 12 · Summary
Alright, let's wrap up.  
▸ *click*  
Review is the new bottleneck.  
▸ *click*  
So switch hats with slash review, and ask the senior reviewer's questions.  
▸ *click*  
Decide what to fix, and keep the fix small.  
▸ *click*  
And always remember: ***Codex finds. You decide.***  
I'm Akmal Khan.  
Thanks for watching, and happy reviewing!  
