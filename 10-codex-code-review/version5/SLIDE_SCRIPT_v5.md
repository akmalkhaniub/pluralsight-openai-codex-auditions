# Slide script v5 (Parts A and C)

Text before the first ▸ is said as the slide appears. **▸ = click** (next animation). Extra space = short pause. ***Bold italic*** = stress.
Total about 630 words, roughly 4:15 at a natural pace. With the 3:06 demo, the audition comes to about 7:20.

Same as the demo: talk at your own pace in one take. I'll fit the slide timing to your voice afterwards. Or record live in PowerPoint Slide Show using the speaker notes (they now hold this script, with [CLICK] markers).

## Part A: before the demo

### Slide 1
AI can write code in a minute.      So who reviews the AI?      Hi, I'm Akmal Khan, a Senior Full Stack AI Architect.      In the next few minutes, I'll show you one simple habit that makes code from OpenAI Codex much safer to ship: ***code review***.

### Slide 2
First, let's meet Codex, OpenAI's coding agent. ▸ You give it a task in plain English, and it does the work of a teammate. It reads your repository, ▸ it writes the change, ▸ it runs your tests, ▸ and it hands you a diff to review. ▸ You can use it in the terminal, in your IDE, or, as we will today, in the Codex app on Windows.

### Slide 3
But here's the catch. ▸ Writing code with Codex now takes about ***five minutes***. ▸ Reviewing that code still takes around ***thirty***. ▸ So the slow part isn't writing anymore. ▸ ***Review is the new bottleneck.*** ▸ By the end of this video, you'll let Codex do the first review for you, so you only spend your time on the risks that really matter. ▸ We'll do it in three steps: the Feature Developer, the Senior Reviewer, and the proof.

### Slide 4
Here's our scenario. ▸ We need a profile photo upload for a small bookshop app. ▸ Codex writes the code for us. ▸ All ***nine*** unit tests pass. ▸ It even handles errors. ▸ So, would you approve this pull request? ▸ Take a second and think about it. ▸ Hold that thought. ▸ Because tests only check what someone ***remembered*** to test. They never check what we ***forgot***.

### Slide 5
So why do teams never let developers approve their own pull requests? ▸ Because the Feature Developer asks one question: did I meet the ticket? ▸ A Senior Reviewer asks a different one: ***what could break this in production?*** ▸ Codex can wear both hats.      Just never in the same prompt.

### Slide 6
In the Codex app, switching hats takes a single command. ▸ You type ***slash review*** in the composer. ▸ You choose what to review. Here, it's the uncommitted changes Codex just made. ▸ Codex puts its findings right on the lines of code, with the most serious ones first. ▸ And it ***doesn't change anything***. You decide what gets fixed. ▸ You can review your uncommitted changes, or compare against a branch. ▸ Today, we'll review the uncommitted changes.

### Slide 7
When a finding matters, don't ask Codex to rewrite everything. ▸ Instead, hover over the exact line, ▸ and click the ***plus***. ▸ Then write one clear sentence about what to fix. ▸ Send a short message: address the inline comments, and ***keep the scope minimal***. ▸ You get one small fix and one new test, and nothing else changes. ▸ That's the habit: ***Build. Review. Commit.*** Never jump straight from build to commit.

### Slide 8
So here's our plan for the demo. ▸ First, Codex builds the photo upload as the Feature Developer. ▸ Then we switch hats with slash review. ▸ We comment on the risky line. ▸ And finally, we check the small fix, and review again.      Let's open the Codex app.

---
## Part C: after the demo

### Slide 9
Let's compare the two versions side by side. ▸ With only the Feature Developer, the upload worked ▸ and nine tests passed. ▸ But a full disk could leave a broken file behind. ▸ With the Senior Reviewer as well, we have the same feature, plus one new test, ▸ and failed uploads are cleaned up.      The tests were green both times. ***The review made the difference.***

### Slide 10
So here's the one habit to take away. ▸ Run ***slash review*** after every Codex task, and before every commit. ▸ And when you read the findings, ask the three questions a senior reviewer always asks. ▸ First, what if it fails halfway? ▸ Second, who is allowed to call this? ▸ And third, what happens if the input is empty, or huge?

### Slide 11
To wrap up. ▸ Review is the new bottleneck. ▸ Switch hats with slash review before you commit. ▸ Point at the line, and keep the fix small. ▸ And remember: ***Codex finds. You decide.***      I'm Akmal Khan. Thanks for watching.

