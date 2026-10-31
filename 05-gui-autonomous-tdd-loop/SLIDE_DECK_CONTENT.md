# Slide Deck Content: The Autonomous TDD Loop in OpenAI Codex (VS Code GUI)

> **Template Note:** Use the official Pluralsight Audition PowerPoint Template (`.pptx`). 
> **Pacing Rule:** Slide/visual updates every 20–30 seconds. All bullets animated to appear on-click.

---

### Slide 1: Title Slide
* **Layout:** `Title Slide`
* **Title:** The Autonomous TDD Loop in OpenAI Codex
* **Subtitle:** From Failing Specifications to Verified Green Code in VS Code
* **Author:** [Your Name]
* **Credentials/Handle:** Senior Software Engineer | @YourHandle
* **Duration:** 0:00 – 0:25 (25 seconds)

---

### Slide 2: Overview & WIIFM
* **Layout:** `Overview/Summary`
* **Header:** What's In It For You?
* **Subheader:** Accelerating Test-Driven Development
* **Bullets (Animate On Click):**
  1. *The TDD Friction:* Writing tests first guarantees correctness, but implementing boilerplate logic is slow.
  2. *The Codex GUI Solution:* Pinning test specifications directly into the Codex extension side panel.
  3. *Today's Goal:* Learn to review side-by-side editor diffs and turn red test suites completely green in minutes.
* **Duration:** 0:25 – 1:10 (45 seconds)

---

### Slide 3: The Developer Scenario
* **Layout:** `Two Text Chunking`
* **Header:** The Problem: Marcus's Discount Engine
* **Left Column:**
  * **The Business Rules**
  * Tier 1: 10% discount on orders over $100.
  * Tier 2: 20% discount on orders over $500.
  * Stacking coupon rules & 2-decimal rounding.
* **Right Column:**
  * **The Starting State**
  * `test_discounts.py`: 4 exhaustive unit tests written.
  * `discount_service.py`: Empty placeholder (`NotImplementedError`).
* **Duration:** 1:10 – 1:35 (25 seconds)

---

### Slide 4: The 3-Step Codex GUI Workflow
* **Layout:** `Three Text Chunking`
* **Header:** The Visual Codex TDD Loop
* **Column 1:**
  * **1. Context Pinning**
  * Tag `#test_discounts.py` in the Codex prompt box as read-only context.
* **Column 2:**
  * **2. Side-by-Side Diff**
  * Review green additions and line changes directly inside the VS Code editor.
* **Column 3:**
  * **3. One-Click Verification**
  * Click 'Accept' and re-run pytest in the integrated terminal to confirm 100% green.
* **Duration:** 1:35 – 2:05 (30 seconds)

---

### Slide 5: The Golden Rule of AI-Driven TDD
* **Layout:** `Important Statement` (Teal accent background)
* **Statement:** "Never allow your AI assistant to modify the test suite to make it pass."
* **Supporting Note:** 
  * Treat the test file as an immutable behavioral contract. Only permit Codex to edit the implementation file.
* **Duration:** 2:05 – 2:35 (30 seconds)

---

### Slide 6: Demo Transition Slide
* **Layout:** `Demo (Optional)`
* **Title:** Live Demonstration
* **Subtitle:** Driving the TDD Loop via the Codex Extension GUI
* **Duration:** 2:35 – 2:45 (10 seconds)

---

### [LIVE DEMO SCREENCAST: 2:45 – 5:45 (3 minutes)]
* **Environment:** VS Code with Codex extension side panel open.
* **Editor Scale:** 125% zoom, status bar hidden, callout overlays for UI buttons (no mouse waving).

---

### Slide 7: Summary & Practical Takeaways
* **Layout:** `Overview/Summary`
* **Header:** Summary: Practical Takeaways
* **Bullets (Animate On Click):**
  1. *Pin Tests via `#file`:* Give Codex full behavioral context right inside the prompt panel.
  2. *Enforce Immutability:* Keep tests strictly read-only so the AI cannot bypass edge cases.
  3. *Visual Diff Supervision:* Always review changes in the side-by-side editor before clicking 'Accept'.
* **Duration:** 5:45 – 6:30 (45 seconds)
