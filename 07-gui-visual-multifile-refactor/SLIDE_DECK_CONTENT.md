# Slide Deck Content: Visual Multi-File Refactoring in OpenAI Codex (VS Code GUI)

> **Template Note:** Use the official Pluralsight Audition PowerPoint Template (`.pptx`). 
> **Pacing Rule:** Slide/visual updates every 20–30 seconds. All bullets animated to appear on-click.

---

### Slide 1: Title Slide
* **Layout:** `Title Slide`
* **Title:** Visual Multi-File Refactoring in OpenAI Codex
* **Subtitle:** Coordinating Cross-File Updates in the VS Code Extension
* **Author:** [Your Name]
* **Credentials/Handle:** Staff Software Engineer | @YourHandle
* **Duration:** 0:00 – 0:25 (25 seconds)

---

### Slide 2: Overview & WIIFM
* **Layout:** `Overview/Summary`
* **Header:** What's In It For You?
* **Subheader:** Beyond Single-File Edits
* **Bullets (Animate On Click):**
  1. *The Coordination Dilemma:* Real refactors touch schemas, services, and routes simultaneously.
  2. *The Codex Multi-File Engine:* Generating synchronized diffs across multiple files in one step.
  3. *Today's Goal:* Learn to scope multi-file prompts and audit changes via the Codex GUI file tree.
* **Duration:** 0:25 – 1:10 (45 seconds)

---

### Slide 3: The Developer Scenario
* **Layout:** `Two Text Chunking`
* **Header:** The Problem: Alex's camelCase Migration
* **Left Column:**
  * **The Frontend Requirement**
  * Modern frontend client expects camelCase (`firstName`, `userRole`).
  * Current API uses snake_case (`first_name`, `user_role`).
* **Right Column:**
  * **The Interdependent Files**
  * `schemas/user.py`: Pydantic serializations.
  * `services/user_service.py`: Business logic dictionaries.
  * `routes/user_routes.py`: Response controllers.
* **Duration:** 1:10 – 1:35 (25 seconds)

---

### Slide 4: Multi-File Tagging in the Codex GUI
* **Layout:** `Three Text Chunking`
* **Header:** The Coordinated GUI Workflow
* **Column 1:**
  * **1. Multi-Tagging**
  * Attach `#schemas/user.py`, `#services/user_service.py`, and `#routes/user_routes.py` in one prompt.
* **Column 2:**
  * **2. Interdependent Planning**
  * Codex plans variable names across files simultaneously.
* **Column 3:**
  * **3. File Tree Review**
  * Inspect diffs file-by-file in the Codex sidebar before accepting.
* **Duration:** 1:35 – 2:05 (30 seconds)

---

### Slide 5: The Review Checklist Principle
* **Layout:** `Important Statement` (Teal accent background)
* **Statement:** "Review multi-file changes file-by-file before clicking 'Accept All'."
* **Supporting Note:** 
  * Use the extension’s visual change tree to audit boundary contracts between schemas and controllers.
* **Duration:** 2:05 – 2:35 (30 seconds)

---

### Slide 6: Demo Transition Slide
* **Layout:** `Demo (Optional)`
* **Title:** Live Demonstration
* **Subtitle:** Coordinating a Multi-File Refactor via the Codex Extension GUI
* **Duration:** 2:35 – 2:45 (10 seconds)

---

### [LIVE DEMO SCREENCAST: 2:45 – 5:45 (3 minutes)]
* **Environment:** VS Code showing open tabs and the Codex extension side panel.
* **Visual Highlights:** Callouts highlighting the 3 `#file` tags, the "Modified Files" tree, and the "Accept All Changes" button.

---

### Slide 7: Summary & Practical Takeaways
* **Layout:** `Overview/Summary`
* **Header:** Summary: Practical Takeaways
* **Bullets (Animate On Click):**
  1. *Tag All Affected Files:* Use `#file` chips to give Codex complete cross-file context.
  2. *Audit via the GUI Tree:* Review each diff independently to verify serialization keys match.
  3. *Coordinated Commits:* Apply synchronized changes with a single 'Accept All' click.
* **Duration:** 5:45 – 6:30 (45 seconds)
