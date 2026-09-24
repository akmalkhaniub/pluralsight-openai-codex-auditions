# Timed Narration Script: Governing OpenAI Codex with AGENTS.md

* **Target Video Length:** 7 minutes 15 seconds
* **Audio Track Standard:** Studio clarity, 48kHz / 24-bit, separate vocal track, zero mouse/keyboard noise.
* **Screen Resolution:** 1920x1080 at 125% IDE scale.

---

### [0:00 - 0:25] Slide 1: Title Slide
* **Visual:** Slide 1 displayed.
* **Speaker Tone:** Authoritative, professional, welcoming.
* **Narration:**
> "Hello everyone, and welcome! My name is [Your Name]. In this session, we’re learning how to **Govern OpenAI Codex by Enforcing Architecture Rules with `AGENTS.md`**."
> 
> *[1-second pause]*
> 
> "As engineering teams adopt AI coding agents, one of the biggest challenges isn’t whether the AI can write code—it’s whether that code actually follows team architecture standards."

---

### [0:25 - 1:10] Slide 2: Overview / WIIFM
* **Visual:** Slide 2 displayed. Click bullets in sync.
* **Speaker Tone:** Pragmatic, engaging.
* **Narration:**
> *[Click Bullet 1]*  
> "When you let an AI write code without guardrails, you get what I call the 'AI Wild West': code that compiles, but introduces deprecated libraries, ignores error hierarchies, and creates technical debt.  
> 
> *[Click Bullet 2]*  
> Asking individual developers to manually re-type your team’s coding checklist into every single prompt is unrealistic and leads to prompt fatigue.  
> 
> *[Click Bullet 3]*  
> In this audition, you’ll learn how to anchor OpenAI Codex permanently to your team’s standards using a declarative repository configuration file: `AGENTS.md`."

---

### [1:10 - 1:40] Slide 3: The Spec Drift Problem
* **Visual:** Slide 3 displayed.
* **Speaker Tone:** Problem-focused, relatable.
* **Narration:**
> "Consider Maya, a lead engineer whose team is using Codex. A developer asks Codex to build an 'OrderNotificationService'.  
> 
> Because Codex doesn't know the team's internal conventions, it falls back to internet defaults: it uses synchronous, blocking `requests` instead of asynchronous `httpx`, it catches all errors with a silent `pass`, and it drops the file straight into the root directory.  
> 
> The code works in isolation, but fails code review completely."

---

### [1:40 - 2:10] Slide 4: How Codex Ingests AGENTS.md
* **Visual:** Slide 4 displayed. Animate columns.
* **Speaker Tone:** Educational, clear.
* **Narration:**
> "OpenAI Codex has native support for repository configuration via `AGENTS.md`.  
> 
> When Codex initializes a workspace, it automatically scans the root for `AGENTS.md`.  
> These instructions take precedence over default model behaviors.  
> And crucially, Codex evaluates every generated diff against these rules before showing it to the developer."

---

### [2:10 - 2:45] Slide 5: The 4 Pillars of a Production AGENTS.md
* **Visual:** Slide 5 displayed. Animate boxes.
* **Speaker Tone:** Systematic, instructional.
* **Narration:**
> "A production-grade `AGENTS.md` rests on four critical pillars:  
> First: **Architectural Boundaries**—defining which layer is allowed to talk to which.  
> Second: **Dependency Whitelists**—specifying approved packages like `httpx` and explicitly banning legacy libraries.  
> Third: **Error Handling**—mandating our custom `AppError` exception hierarchy.  
> And Fourth: **Test Requirements**—enforcing that every new service comes with a companion unit test in the `tests/` directory."

---

### [2:45 - 3:30] Slide 6: Important Statement
* **Visual:** Slide 6 displayed (Teal accent).
* **Speaker Tone:** Deliberate, impactful.
* **Narration:**
> "Remember this principle:  
> 
> *[1-second pause]*  
> 
> *'If a coding standard isn't in your repository configuration, it doesn't exist for the AI.'*  
> 
> Treat `AGENTS.md` with the exact same rigor you treat your linter rules, your TypeScript configs, or your CI pipeline. It is the architectural contract for your AI pair programmer.  
> 
> Let's see the dramatic difference this makes in practice."

---

### [3:30 - 3:45] Slide 7: Demo Transition
* **Visual:** Slide 7 displayed.
* **Narration:**
> "Let's switch to VS Code and test Codex before and after introducing our `AGENTS.md` file."

---

### [3:45 - 6:45] LIVE DEMO SCREENCAST (3:00)

#### Segment 1: The Ungoverned Prompt [3:45 - 4:25]
* **Screen:** Clean VS Code window. Note that `AGENTS.md` is temporarily disabled or renamed.
* **Action:** Prompt Codex: *"Create an OrderNotificationService that sends a JSON order payload to an external webhook URL."*
* **Visual Cue:** `[CALLOUT BOX: Highlight generated imports and exception handling]` *(Hand off mouse)*.
* **Narration:**
> "First, let's run the prompt with no repository governance. We ask Codex to create our notification service.  
> 
> Look at what it generates: it imports the synchronous `requests` library, which blocks our event loop. It uses raw `print` statements for debugging. And when an HTTP error occurs, it swallows the exception. This would never pass a senior pull request review."

#### Segment 2: Introducing AGENTS.md [4:25 - 5:15]
* **Screen:** Open `AGENTS.md` in the editor.
* **Visual Cue:** `[CALLOUT BOX: Highlight Section 2: Dependencies and Section 3: Error Handling]`
* **Narration:**
> "Now, let’s enable our `AGENTS.md` file at the root of the project.  
> 
> Notice how clean and declarative this is:  
> Under dependencies, we state: *'Always use async httpx. Do not use requests.'*  
> Under error handling, we mandate: *'Import and raise NotificationDeliveryError from src/errors/app_error.py.'*  
> And under testing: *'Every service must have a companion test file in tests/services/.'*"

#### Segment 3: The Governed Prompt Execution [5:15 - 6:05]
* **Screen:** Re-run the exact same prompt in Codex.
* **Action:** Run prompt: *"Create an OrderNotificationService that sends a JSON order payload to an external webhook URL."*
* **Visual Cue:** `[CALLOUT BOX: Highlight citation of AGENTS.md in Codex reasoning, then highlight httpx import and AppError raise]`
* **Narration:**
> "Let's run the exact same prompt again. Watch what happens.  
> 
> Codex immediately flags that it has detected `AGENTS.md`.  
> Look at the generated code now: it uses asynchronous `httpx.AsyncClient`. It imports our custom `NotificationDeliveryError`. And notice the file path: it places the service inside `src/services/order_notification.py`."

#### Segment 4: Automatic Companion Test Generation [6:05 - 6:45]
* **Screen:** Codex opens the second generated file: `tests/services/test_order_notification.py`.
* **Visual Cue:** `[CALLOUT BOX: Highlight pytest test file with mock httpx]`
* **Narration:**
> "Even better: without us asking, Codex recognized rule four and generated `tests/services/test_order_notification.py` with mocked HTTP responses ready to run with pytest.  
> 
> Maya’s team has just gone from manual prompt micromanagement to automated, repeatable architectural compliance."

---

### [6:45 - 7:15] Slide 8: Summary & Key Takeaways
* **Visual:** Slide 8 displayed. Click bullets in sync.
* **Speaker Tone:** Enthusiastic, summarizing.
* **Narration:**
> *[Click Bullet 1]*  
> "To recap: stop re-prompting the same coding rules in every conversation.  
> 
> *[Click Bullet 2]*  
> Centralize your standards in an `AGENTS.md` file right alongside your code in version control.  
> 
> *[Click Bullet 3]*  
> Enforce approved libraries, error types, and automatic test generation so your team can move fast without compromising quality.  
> 
> Thank you for watching, and start governing your AI tools today!"
