# Slide Deck Content: Rapid Codebase Onboarding Using OpenAI Codex

> **Template Note:** Use the official Pluralsight Audition PowerPoint Template (`.pptx`). 
> **Pacing Rule:** Every slide must transition or update its visuals every 20–30 seconds. All bullets must have an **Appear** or **Fade** on-click animation.

---

### Slide 1: Title Slide
* **Layout:** `Title Slide`
* **Title:** Rapid Codebase Onboarding Using OpenAI Codex
* **Subtitle:** Mastering Repository Exploration & Architecture Tracing
* **Author:** [Your Name]
* **Credentials/Handle:** Senior Software Engineer | @YourHandle
* **Visual:** Pluralsight standard dark title background with subtle orange branding.
* **Duration:** 0:00 – 0:25 (25 seconds)

---

### Slide 2: Overview / WIIFM
* **Layout:** `Overview/Summary` (Split screen: Orange accent left, content right)
* **Header:** What's In It For You?
* **Subheader:** The Cost of Exploring Unfamiliar Code
* **Bullets (Animate On Click):**
  1. *The Onboarding Tax:* Traditional onboarding consumes days of manual file reading and outdated wiki pages.
  2. *The Codex Advantage:* OpenAI Codex understands full repository context, call hierarchies, and dependencies.
  3. *Today's Goal:* Learn how to direct Codex to trace request flows end-to-end and generate verified architecture maps.
* **Duration:** 0:25 – 1:15 (50 seconds)

---

### Slide 3: The Developer Dilemma
* **Layout:** `Two Text Chunking`
* **Header:** The Problem: Onboarding Blind
* **Left Column:**
  * **The Scenario**
  * You inherit an undocumented 50,000-line service.
  * You need to fix a critical bug in 48 hours.
  * Searching keywords yields hundreds of irrelevant matches.
* **Right Column:**
  * **The Human Limitation**
  * Context switching between 15 open tabs.
  * Missed middleware and hidden decorators.
  * Risk of breaking unspoken assumptions.
* **Duration:** 1:15 – 1:45 (30 seconds)

---

### Slide 4: How Codex Sees Your Codebase
* **Layout:** `Three Text Chunking`
* **Header:** OpenAI Codex Repository Intelligence
* **Column 1:**
  * **AST & Structure**
  * Indexes syntax trees, classes, and exported functions.
* **Column 2:**
  * **Call Hierarchies**
  * Traces caller-to-callee relationships across directories.
* **Column 3:**
  * **Execution Context**
  * Understands framework conventions (FastAPI, Express, Django).
* **Duration:** 1:45 – 2:15 (30 seconds)

---

### Slide 5: The Formula for Scoped Exploration
* **Layout:** `Important Statement` (Solid teal/blue accent background)
* **Statement:** "Never ask Codex 'How does this project work?'"
* **Supporting Callout Box:** 
  * "Anchor your prompt to a concrete **entry point**, specify the **data entity**, and request an **execution trace**."
* **Duration:** 2:15 – 2:45 (30 seconds)

---

### Slide 6: The Scoped Prompt Formula
* **Layout:** `Code Notes Dark`
* **Header:** The 3-Part Scoping Anatomy
* **Code / Text Box:**
  ```text
  [1. Entry Point]  Starting from /api/v1/users/register (routes/auth.py)...
  [2. Scope Filter] Trace the registration flow through validation middleware & service layers...
  [3. Output Target] Generate a step-by-step call graph and note database write side-effects.
  ```
* **Duration:** 2:45 – 3:30 (45 seconds)

---

### Slide 7: Demo Transition Slide
* **Layout:** `Demo (Optional)` (Teal icon layout)
* **Title:** Hands-On Demo
* **Subtitle:** Tracing an Auth Pipeline Live in OpenAI Codex
* **Duration:** 3:30 – 3:45 (15 seconds)

---

### [LIVE DEMO SCREENCAST: 3:45 – 6:45 (3 minutes)]
* **Environment:** VS Code with OpenAI Codex / Terminal clean (No cursor circling; all highlights via post-production callouts).

---

### Slide 8: Summary & Key Takeaways
* **Layout:** `Overview/Summary`
* **Header:** Summary: Practical Takeaways
* **Bullets (Animate On Click):**
  1. *Avoid Open-Ended Prompts:* Always provide an entry point, a layer filter, and an explicit output format.
  2. *Leverage Repository Awareness:* Codex bridges the gap between router, middleware, and database models.
  3. *Accelerate Onboarding:* Cut ramp-up time from 3 days to 15 minutes with verified architectural traces.
* **Duration:** 6:45 – 7:15 (30 seconds)
