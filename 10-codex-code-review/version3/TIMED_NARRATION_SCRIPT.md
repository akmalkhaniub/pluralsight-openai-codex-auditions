# Timed Narration Script: Who Reviews the AI? Code Review with OpenAI Codex (v3)

**Author:** Akmal Khan · **Role:** Senior Full Stack AI Architect  
**Target Duration:** ~7:15 (Audition Sweet Spot: 5–8 minutes)  
**Tone:** Dynamic, authoritative, conversational, senior engineering focus  
**Core Analogy:** The Feature Developer vs. The Senior PR Reviewer. When AI writes code, it optimizes for the happy path. `/review` forces Codex into adversarial review mode to catch production failures before you commit.

> **Delivery Legend:**  
> `[CLICK]` = Advance slide animation / element build in PowerPoint.  
> `[CALLOUT: "..."]` = Visual bounding box / graphic banner added in editing.  
> `(Beat)` = Brief dramatic pause (1 second).  
> *Bracketed text is directional; do not speak.*

---

## Act I: The Bottleneck & The Pull Request Dilemma (0:00 – 1:40)

### 0:00 – 0:15 · Slide 1 — Title Hook
*(Visual: Clean title slide, "Who Reviews the AI?", author badge. No in-slide clicks.)*

AI can write code in sixty seconds. But who reviews the AI?

When nobody audits the edge cases, bugs don't just slip into production—they multiply.

Hi, I'm Akmal Khan, Senior Full Stack AI Architect. Today, we're unlocking the single most critical habit for working with OpenAI Codex: code review.

`[CLICK → Advance to Slide 2]`

---

### 0:15 – 0:40 · Slide 2 — Meet Your New Autonomous Teammate
*(Visual: 4 animated circular pillars: Reads repo → Writes change → Runs tests → Hands you the diff)*

First, let's meet our player. OpenAI Codex isn't just a code autocomplete engine.

You give it a task in plain English, and it:
`[CLICK]` Reads your entire repository context,
`[CLICK]` Plans and writes the changes across files,
`[CLICK]` Runs your test suite autonomously,
`[CLICK]` And hands you a clean diff.

`[CLICK]` Whether in your terminal, IDE, or the standalone Codex app on Windows—it acts like an eager junior engineer on your team.

---

### 0:40 – 1:05 · Slide 3 — The Inconvenient Truth: Review is the New Bottleneck
*(Visual: Split comparison bar chart: Writing 5 min vs. Reviewing 30 min, WIIFM banner, 3-Act roadmap)*

`[CLICK]` But here's the reality check of working with AI.

`[CLICK]` Writing code used to take hours; now Codex knocks it out in five minutes flat.

`[CLICK]` But reviewing that generated code? That still takes thirty minutes!

`[CLICK]` Code review is officially the new bottleneck in software development.

`[CLICK]` Today's mission: you'll learn how to let Codex perform its own first-pass code review, so you only spend your brainpower on the risks that truly matter.

`[CLICK]` Three quick acts: The Feature Developer, The Senior Reviewer, and The Proof.

---

### 1:05 – 1:45 · Slide 4 — The PR Looks Green. Would You Approve It?
*(Visual: Code panel showing clean upload_avatar function, 9 green checks, quiz pulse box)*

`[CLICK]` Here's our real-world scenario: we need a profile photo upload feature for our bookshop application.

`[CLICK]` Codex tackles it instantly.

`[CLICK]` It writes thirty lines of Python. Nine automated unit tests run and pass with flying colors!

`[CLICK]` It even includes error handling for invalid image formats.

`[CLICK]` So... would you hit Approve on this Pull Request and ship it straight to production on a Friday afternoon?

`[CLICK]` Take a second.

`[CLICK]` Hold that thought!

`[CLICK]` Because unit tests only verify what you remembered to test. They never test what you completely forgot!

---

## Act II: Switching Hats & The Power of `/review` (1:45 – 3:20)

### 1:45 – 2:10 · Slide 5 — Every Pull Request Needs a Second Pair of Eyes
*(Visual: Side-by-side comparison: 💻 The Feature Developer vs. 🔍 The Senior PR Reviewer)*

`[CLICK]` Think about why engineering teams have strict code review policies. Why don't we let developers approve their own Pull Requests?

`[CLICK]` Because when you build a feature, your brain is in Implementation Mode:
"Did I satisfy the ticket? Are my tests green?"

`[CLICK]` But a Senior PR Reviewer looks at that same code in Failure Mode:
"What breaks this when storage fills up or the network drops?"

`[CLICK]` OpenAI Codex can wear both hats.
But here is the golden rule: Never both in the same prompt.

---

### 2:10 – 2:45 · Slide 6 — Flip the Switch with `/review`
*(Visual: 4 numbered workflow cards with interactive options callout)*

In the Codex app, turning Codex into your Senior Reviewer takes exactly one command.

`[CLICK]` You type slash review right into the composer.

`[CLICK]` Pick your scope: here, we choose Review uncommitted changes—the exact edits Codex just produced.

`[CLICK]` Codex immediately re-analyzes the codebase, pinpointing findings directly on the offending lines, sorted by severity.

`[CLICK]` And best of all: it doesn't touch a single line of your code yet. You remain the senior engineer in the driver's seat.

`[CLICK]` You can review uncommitted changes or diff against a base branch. Today, we inspect our fresh uncommitted changes.

---

### 2:45 – 3:15 · Slide 7 — Point at the Line. Keep the Scope Surgical.
*(Visual: Mini code diff with red bounding box on file open, blue '+' icon, minimal comment callout)*

`[CLICK]` When Codex flags a real architectural finding, don't let it rewrite the entire file.

`[CLICK]` Simply hover over the exact line, click the blue plus icon,

`[CLICK]` And drop a punchy, one-sentence directive.

`[CLICK]` Then tell Codex: "Address the inline comments and keep the scope minimal."

`[CLICK]` You get exactly one targeted fix, one focused regression test, and zero unwanted side effects.

`[CLICK]` This is the new elite engineering habit: Build. Review. Commit.
Never jump straight from Build to Commit!

---

### 3:15 – 3:25 · Slide 8 — The Action Roadmap
*(Visual: 4-step execution flow ready to switch)*

`[CLICK]` Here is our live flight plan:

`[CLICK]` First, Codex wears the Feature Dev hat to build the upload.

`[CLICK]` Second, we switch hats with /review.

`[CLICK]` Third, we pin an inline comment on the danger zone.

`[CLICK]` And fourth, we verify the surgical fix. Let's fire up the Codex app!

> **⏹ SWITCH → LIVE DEMO (Clip B starts at 3:25)**

---

## Act III: The Live Screencast Demo (3:25 – 6:17)

### 3:25 – 4:10 · Scene 1: The Eager Feature Developer
*(Screen: Codex App on Windows in photo-take workspace. Clean UI, dark mode, terminal ready)*  
`[CALLOUT: "Agent wait shortened"]`  
`[CALLOUT: "All 9 tests pass ✅"]`

Here we are in our clean bookshop repository. In the composer, I'll paste our task: *"Let users upload a profile photo. Add upload_avatar in app/profile.py, save under avatars/, update avatar_url, and run tests."*  
Codex immediately inspects the repo, sets up UUID-based naming, and runs the tests.  
And right there—nine tests passing, clean assertions. The Feature Developer satisfied the ticket requirements and thinks the job is done. But are we ready to commit? Absolutely not.

---

### 4:10 – 5:05 · Scene 2: The Senior PR Reviewer (The "Ah-ha!" Moment)
*(Screen: Typing /review → selecting "Review uncommitted changes" → findings generated)*  
`[CALLOUT: "Agent wait shortened"]`  
`[CALLOUT: "P2 Finding: Orphaned file on disk-full failure"]`

Let's put on the Senior Reviewer's hat. I'll type `/review` and select **Review uncommitted changes**.  
Codex shifts into inspection mode: it reads, analyzes edge cases, and changes nothing.  
And look at what it just caught! `(Beat)`  
A **Priority 2** finding right on lines 26 through 32.  
All nine unit tests passed, but Codex realized that if the server disk fills up or the client connection terminates mid-transfer, a half-written, corrupted file is permanently abandoned in the avatars directory!  
The Feature Developer proved it worked under sunny-day conditions. The Senior Reviewer proved what happens during a production failure.

---

### 5:05 – 5:40 · Scene 3: Point at the Line
*(Screen: Hovering line 26, clicking '+', entering comment, sending follow-up)*  
`[CALLOUT: "Targeted directive: one sentence"]`

We're not going to re-prompt from scratch or let Codex guess. I'll hover right over line 26 where the file handle is opened, click the plus icon, and leave our directive:  
*"Agreed: if saving fails, delete the half-saved file. Add a test for it."*  
Now in the composer, I reinforce the scope:  
*"Address the inline comments and keep the scope minimal."*  
Hit send.

---

### 5:40 – 6:00 · Scene 4: The Surgical Fix
*(Screen: Codex applies fix, runs new regression test suite, switches Review scope to Last Turn)*  
`[CALLOUT: "Regression test added"]`  
`[CALLOUT: "+6 −6 lines: Clean surgical diff"]`

Codex gets right to work. Notice how disciplined this is: it wraps the stream in a clean `try...except`, triggers `destination.unlink()`, and adds a dedicated mock test that simulates a broken stream.  
Ten tests are now passing! Switching the diff view to **Last Turn** confirms the beauty of this workflow: exactly six lines added, six lines modified. No hallucinations, no unwanted refactoring.

---

### 6:00 – 6:17 · Scene 5: The Clean Re-Review
*(Screen: Triggering /review again → "No actionable issues")*  
`[CALLOUT: "Zero actionable issues ✅"]`

One final check to be certain: `/review` → **Review uncommitted changes**.  
And there it is: *"No actionable issues found."*  
Now—and only now—are we confident to git commit and open our PR. Let's see the side-by-side contrast.

> **⏹ SWITCH → SLIDES RECAP (Clip C starts at 6:17)**

---

## Act IV: The Takeaway & Wrap-Up (6:17 – 7:12)

### 6:17 – 6:40 · Slide 9 — The Proof: One Review, One Real Bug Defused
*(Visual: Clear split table: Feature Dev Only vs. Feature Dev + Senior Reviewer)*

`[CLICK]` Look at this side-by-side verdict.

`[CLICK]` With only the Feature Developer, our upload functioned and nine tests were green—

`[CLICK]` But an unhandled disk-full condition was lurking to corrupt user storage.

`[CLICK]` With the Feature Developer and the Senior Reviewer, we have the exact same feature, plus one robust regression test,

`[CLICK]` And zero orphaned files.

`[CLICK]` The tests were green both times. The code review made all the difference.

---

### 6:40 – 6:58 · Slide 10 — Your Takeaway: The Reviewer's 3 Questions
*(Visual: Big /review keyboard key, 3 core question cards: Halfway failure, Authorization, Boundary limits)*

`[CLICK]` Here is the one career habit to cement from this audition:

`[CLICK]` Run /review after every Codex task, and before every single commit.

`[CLICK]` Whenever you evaluate Codex's findings, ensure you test the three questions a Senior Reviewer always asks:
1. What if the operation fails halfway?
2. Who is authorized to call this?
3. What happens when input is empty or gigantic?

---

### 6:58 – 7:12 · Slide 11 — The Final Rule: Codex Finds. You Decide.
*(Visual: Elegant Pluralsight summary slide with 4 punchy key takeaways)*

`[CLICK]` To wrap it all up:

1. Review is your new competitive bottleneck.

`[CLICK]` 2. Switch hats with /review before every commit.

`[CLICK]` 3. Point at the line, and demand surgical fixes.

`[CLICK]` And above all: Codex finds the risks, but you decide what ships to production.

I'm Akmal Khan—thank you for watching.

---
