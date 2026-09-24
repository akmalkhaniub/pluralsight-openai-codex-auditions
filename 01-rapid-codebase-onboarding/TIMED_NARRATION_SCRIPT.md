# Timed Narration Script: Rapid Codebase Onboarding Using OpenAI Codex

* **Target Video Length:** 7 minutes 15 seconds
* **Audio Track Standard:** Clean voice recording, 48kHz / 24-bit, separate audio track, zero keyboard/mouse clicks.
* **Camera / Screen:** Crisp 1920x1080 resolution, 125% IDE scaling.

---

### [0:00 - 0:25] Slide 1: Title Slide
* **Visual:** Slide 1 displayed.
* **Speaker Tone:** Warm, confident, authoritative.
* **Narration:**
> "Hello everyone, and welcome! My name is [Your Name]. In this session, we’re exploring **Rapid Codebase Onboarding Using OpenAI Codex**."
> 
> *[1-second pause]*
> 
> "Every developer knows that feeling of landing on a new team, opening a massive repository for the first time, and staring at thousands of lines of unfamiliar code with almost zero documentation."

---

### [0:25 - 1:15] Slide 2: Overview / WIIFM
* **Visual:** Slide 2 displayed. Click bullets in sync with speech.
* **Speaker Tone:** Empathetic, energetic.
* **Narration:**
> *[Click Bullet 1]*  
> "Traditionally, onboarding onto a legacy service takes days—sometimes even weeks—of manual code reading, blind grepping, and outdated wiki articles.  
> 
> *[Click Bullet 2]*  
> But with OpenAI Codex, we have an AI agent that understands entire repository structures, call hierarchies, and architectural conventions.  
> 
> *[Click Bullet 3]*  
> By the end of this audition, you’ll have the exact skills and prompt patterns needed to direct OpenAI Codex to trace complex request flows, uncover hidden middleware, and ramp up on any codebase in a fraction of the time."

---

### [1:15 - 1:45] Slide 3: The Developer Dilemma
* **Visual:** Slide 3 displayed.
* **Speaker Tone:** Problem-driven, serious.
* **Narration:**
> "Let’s set the scene. Imagine you’re Jordan, a software engineer who just joined the team. You have a ticket to fix an authentication bottleneck within 48 hours.  
> 
> If you start searching keywords like 'authenticate' or 'token' in your editor, you’ll get hundreds of search results across tests, mocks, and models. You end up juggling 15 open tabs and guessing how the request actually moves through the system. Human memory quickly gets overwhelmed."

---

### [1:45 - 2:15] Slide 4: How Codex Sees Your Codebase
* **Visual:** Slide 4 displayed. Animate columns.
* **Speaker Tone:** Clear, educational.
* **Narration:**
> "OpenAI Codex approaches your codebase differently. It doesn’t just perform naive text matches.  
> 
> First, it builds an abstract syntax tree of your files.  
> Second, it maps the call hierarchy—connecting routes to middleware, services, and database entities.  
> And third, it understands modern framework conventions, whether you’re working with FastAPI, Express, or Spring Boot."

---

### [2:15 - 2:45] Slide 5: The Formula for Scoped Exploration
* **Visual:** Slide 5 displayed (Solid accent).
* **Speaker Tone:** Emphatic, guiding.
* **Narration:**
> "However, the single biggest mistake developers make is asking open-ended questions like: *'How does this project work?'*  
> 
> *[1-second pause]*  
> 
> That guarantees vague, generic summaries. To get high-precision insights, you must anchor your request to a specific **entry point**, filter by **layer**, and specify the **output format** you need."

---

### [2:45 - 3:30] Slide 6: The 3-Part Scoping Anatomy
* **Visual:** Slide 6 displayed with code note styling.
* **Speaker Tone:** Prescriptive, practical.
* **Narration:**
> "Here is our 3-part formula:  
> 
> One: Define the **Entry Point**. In our case, starting from `/api/v1/users/register` in `routes/auth.py`.  
> Two: Specify the **Scope Filter**. We explicitly instruct Codex to trace through validation middleware and service layers.  
> And Three: Set the **Target Output**. We ask for a chronological execution call graph and any database side-effects.  
> 
> Let's jump into the code and see this in action."

---

### [3:30 - 3:45] Slide 7: Demo Transition
* **Visual:** Slide 7 displayed.
* **Narration:**
> "Let's switch over to VS Code and watch OpenAI Codex analyze our service in real time."

---

### [3:45 - 6:45] LIVE DEMO SCREENCAST (3:00)

#### Segment 1: The Codebase Problem [3:45 - 4:15]
* **Screen:** VS Code showing file explorer with `demo-code/` (`routes/`, `middleware/`, `services/`, `models/`).
* **Visual Cue:** `[CALLOUT BOX: Highlight file tree]` *(DO NOT circle with cursor)*.
* **Narration:**
> "Here we are inside our user service. In the file tree on the left, you can see multiple directories: `routes`, `middleware`, `services`, and `models`. Without documentation, we don't know the exact order of execution or what middleware runs before the database is touched."

#### Segment 2: Issuing the Scoped Prompt [4:15 - 4:55]
* **Screen:** Open Codex chat / prompt panel in the IDE.
* **Action:** Paste the pre-formatted 3-part prompt from `codex_prompts.txt`.
* **Visual Cue:** `[CALLOUT BOX: Highlight the prompt text]`
* **Narration:**
> "Instead of manually clicking through files, let's open Codex. We paste our 3-part prompt:  
> *'Starting from routes/auth.py at the register endpoint, trace the entire execution flow down to the persistence layer. Identify every middleware invoked and list any database writes.'*  
> Let's run this."

#### Segment 3: Codex Processing & Analysis [4:55 - 5:50]
* **Screen:** Codex traces the files, showing file inspection indicators.
* **Visual Cue:** `[CALLOUT BOX: Highlight routes/auth.py -> middleware/rate_limiter.py -> middleware/token_validator.py]`
* **Narration:**
> "Notice what Codex is doing: it starts at `routes/auth.py`. It immediately identifies that the route is decorated with `@rate_limiter` and `@token_validator`.  
> 
> It opens both middleware files, inspects their logic, and then steps down into `services/user_service.py`. It flags that the password hash is salted using Argon2, and finally navigates to `models/user.py` where the database transaction commits."

#### Segment 4: Reviewing the Architectural Output [5:50 - 6:45]
* **Screen:** Codex renders the final markdown summary with a clean step-by-step trace and sequence breakdown.
* **Visual Cue:** `[CALLOUT BOX: Highlight the 4-step execution summary]`
* **Narration:**
> "Look at the generated result. In less than 30 seconds, Codex has provided:  
> First: The exact chronological sequence of middleware.  
> Second: The data transformation occurring in the user service.  
> And Third: The database write operations and potential latency points.  
> 
> Jordan now has a verified mental model of the registration flow, without ever having to guess or grep through unrelated files."

---

### [6:45 - 7:15] Slide 8: Summary & Key Takeaways
* **Visual:** Slide 8 displayed. Click bullets in sync.
* **Speaker Tone:** Energized, concluding.
* **Narration:**
> *[Click Bullet 1]*  
> "To summarize: never start with open-ended questions when exploring a new codebase.  
> 
> *[Click Bullet 2]*  
> Always anchor Codex to a specific entry point and specify the layers you care about.  
> 
> *[Click Bullet 3]*  
> By leveraging OpenAI Codex's repository-level awareness, you can cut onboarding time from days to minutes.  
> 
> Thank you so much for watching, and I look forward to seeing you in the next lesson!"
