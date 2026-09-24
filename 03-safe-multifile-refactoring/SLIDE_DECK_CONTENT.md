# Slide Deck Content: Safe Multi-File Refactoring and Verification with OpenAI Codex

> **Template Note:** Use the official Pluralsight Audition PowerPoint Template (`.pptx`). 
> **Pacing Rule:** Slide/visual updates every 20–30 seconds. All bullets animated to appear on-click.

---

### Slide 1: Title Slide
* **Layout:** `Title Slide`
* **Title:** Safe Multi-File Refactoring with OpenAI Codex
* **Subtitle:** Orchestrating Code Modernization and Sandboxed Verification
* **Author:** [Your Name]
* **Credentials/Handle:** Staff Software Engineer | @YourHandle
* **Duration:** 0:00 – 0:25 (25 seconds)

---

### Slide 2: Overview / WIIFM
* **Layout:** `Overview/Summary`
* **Header:** What's In It For You?
* **Subheader:** Conquering the Fear of Refactoring
* **Bullets (Animate On Click):**
  1. *The Refactoring Trap:* Changing one core interface usually breaks 3 downstream files.
  2. *Single-File AI Fails:* Asking an AI to edit one file in isolation leaves caller sites broken.
  3. *Today's Goal:* Master OpenAI Codex’s multi-file planning and sandboxed test execution to modernize code with zero regressions.
* **Duration:** 0:25 – 1:15 (50 seconds)

---

### Slide 3: The Danger of Single-File AI Edits
* **Layout:** `Two Text Chunking`
* **Header:** The Problem: The Ripple Effect
* **Left Column:**
  * **The Root Change**
  * Changing `def process()` to `async def process()`.
  * Returns an async generator instead of a list.
* **Right Column:**
  * **The Downstream Breakage**
  * Controllers fail with `TypeError: unawaited coroutine`.
  * Batch runners crash.
  * Unit tests fail assertions.
* **Duration:** 1:15 – 1:45 (30 seconds)

---

### Slide 4: The 3-Stage Refactoring Cycle in Codex
* **Layout:** `Three Text Chunking`
* **Header:** The Codex Refactoring Architecture
* **Column 1:**
  * **1. Multi-File Plan**
  * Codex builds a dependency graph of all caller sites before touching code.
* **Column 2:**
  * **2. Worktree Isolation**
  * Edits are applied cleanly across all interdependent files in an isolated branch.
* **Column 3:**
  * **3. Sandbox Verification**
  * Runs unit tests in a containerized environment to verify zero regression.
* **Duration:** 1:45 – 2:15 (30 seconds)

---

### Slide 5: The Refactoring Prompt Pattern
* **Layout:** `Code Notes Dark`
* **Header:** Framing Multi-File Refactoring Prompts
* **Code / Text Box:**
  ```text
  [Objective] Refactor CsvIngestionEngine in engine.py from sync list returns to async stream generator.
  [Scope]     Identify all caller sites in controller.py and update them to use 'async for'.
  [Verify]    Execute 'pytest test_pipeline.py' in the sandbox and iterate until green.
  ```
* **Duration:** 2:15 – 2:45 (30 seconds)

---

### Slide 6: Important Statement
* **Layout:** `Important Statement` (Solid teal accent background)
* **Statement:** "Refactoring without automated test execution isn't modernizing—it's gambling."
* **Supporting Note:** 
  * OpenAI Codex pairs code generation with automated execution loops to catch regressions before you ever see the diff.
* **Duration:** 2:45 – 3:30 (45 seconds)

---

### Slide 7: Demo Transition Slide
* **Layout:** `Demo (Optional)`
* **Title:** Hands-On Demo
* **Subtitle:** Modernizing a Data Pipeline Live in OpenAI Codex
* **Duration:** 3:30 – 3:45 (15 seconds)

---

### [LIVE DEMO SCREENCAST: 3:45 – 6:45 (3 minutes)]
* **Environment:** VS Code with Codex agent panel. Clean screen, terminal zoom at 125%, post-production callouts.

---

### Slide 8: Summary & Key Takeaways
* **Layout:** `Overview/Summary`
* **Header:** Summary: Practical Takeaways
* **Bullets (Animate On Click):**
  1. *Think in Dependency Graphs:* Never prompt an AI to refactor an interface without scoping its callers.
  2. *Leverage Multi-File Edits:* Allow Codex to modify both the service, the controller, and the test suite simultaneously.
  3. *Trust, but Sandboxed Verify:* Always let Codex run the test suite to catch edge cases and self-heal discrepancies.
* **Duration:** 6:45 – 7:15 (30 seconds)
