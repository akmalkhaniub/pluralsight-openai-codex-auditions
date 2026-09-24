# Slide Deck Content: Governing OpenAI Codex with AGENTS.md

> **Template Note:** Use the official Pluralsight Audition PowerPoint Template (`.pptx`). 
> **Pacing Rule:** Slide/visual changes every 20–30 seconds. Every bullet point animated to appear on-click.

---

### Slide 1: Title Slide
* **Layout:** `Title Slide`
* **Title:** Governing OpenAI Codex with `AGENTS.md`
* **Subtitle:** Enforcing Architecture Standards and Eliminating Spec Drift
* **Author:** [Your Name]
* **Credentials/Handle:** Principal Engineer | @YourHandle
* **Duration:** 0:00 – 0:25 (25 seconds)

---

### Slide 2: Overview / WIIFM
* **Layout:** `Overview/Summary`
* **Header:** What's In It For You?
* **Subheader:** The Cost of Ungoverned AI Code
* **Bullets (Animate On Click):**
  1. *The AI "Wild West":* Without guardrails, Codex generates code that compiles but violates team standards.
  2. *The Prompt Fatigue Problem:* Developers cannot be expected to copy-paste a 20-point checklist into every chat prompt.
  3. *Today's Goal:* Anchor OpenAI Codex permanently to your team's architecture using a root `AGENTS.md` file.
* **Duration:** 0:25 – 1:10 (45 seconds)

---

### Slide 3: The Spec Drift Problem
* **Layout:** `Two Text Chunking`
* **Header:** The Problem: Spec Drift at Scale
* **Left Column:**
  * **What Developers Prompt**
  * "Create an OrderNotificationService"
  * Expecting enterprise patterns, clean error handling, and unit tests.
* **Right Column:**
  * **What Codex Defaults To**
  * Uses blocking libraries (`requests` instead of `httpx`).
  * Swallows exceptions with generic `except: pass`.
  * Drops the file wherever it feels like.
* **Duration:** 1:10 – 1:40 (30 seconds)

---

### Slide 4: How Codex Ingests `AGENTS.md`
* **Layout:** `Three Text Chunking`
* **Header:** The Governance Lifecycle
* **Column 1:**
  * **Automatic Discovery**
  * Codex automatically reads `AGENTS.md` on workspace initialization.
* **Column 2:**
  * **Precedence Anchoring**
  * Repository rules override general foundation model defaults.
* **Column 3:**
  * **Continuous Compliance**
  * Every generated file and diff is verified against the declared rules.
* **Duration:** 1:40 – 2:10 (30 seconds)

---

### Slide 5: The 4 Pillars of a Production `AGENTS.md`
* **Layout:** `Four Text Chunking`
* **Header:** Core Architecture of `AGENTS.md`
* **Box 1: Architecture Boundaries**
  * Layer rules (e.g. Services never call DB directly; must use Repositories).
* **Box 2: Dependency Whitelists**
  * Allowed: `httpx`, `pydantic v2`. Banned: `requests`, raw `print()`.
* **Box 3: Error Handling**
  * Must throw subclasses of `AppError`; no bare exceptions.
* **Box 4: Test Requirements**
  * Companion tests required in `tests/` mirroring the `src/` hierarchy.
* **Duration:** 2:10 – 2:45 (35 seconds)

---

### Slide 6: Important Statement
* **Layout:** `Important Statement` (Solid teal accent background)
* **Statement:** "If a coding standard isn't in your repository configuration, it doesn't exist for the AI."
* **Supporting Note:** 
  * Treat `AGENTS.md` with the same rigour as your linter config or CI pipeline.
* **Duration:** 2:45 – 3:30 (45 seconds)

---

### Slide 7: Demo Transition Slide
* **Layout:** `Demo (Optional)`
* **Title:** Hands-On Demo
* **Subtitle:** Taming Codex: Before and After `AGENTS.md`
* **Duration:** 3:30 – 3:45 (15 seconds)

---

### [LIVE DEMO SCREENCAST: 3:45 – 6:45 (3 minutes)]
* **Environment:** VS Code with Codex panel. Clean workspace, no mouse waving, post-production callout overlays.

---

### Slide 8: Summary & Key Takeaways
* **Layout:** `Overview/Summary`
* **Header:** Summary: Practical Takeaways
* **Bullets (Animate On Click):**
  1. *Stop Re-prompting Standards:* Commit team conventions to `AGENTS.md` at the root of your repo.
  2. *Declare Hard Boundaries:* Explicitly blacklist obsolete packages and enforce custom error classes.
  3. *Enforce Automatic Testing:* Mandate that Codex generate companion tests in matching directories.
* **Duration:** 6:45 – 7:15 (30 seconds)
