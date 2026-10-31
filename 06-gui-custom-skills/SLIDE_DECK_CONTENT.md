# Slide Deck Content: Custom Reusable Skills in OpenAI Codex (VS Code GUI)

> **Template Note:** Use the official Pluralsight Audition PowerPoint Template (`.pptx`). 
> **Pacing Rule:** Slide/visual updates every 20–30 seconds. All bullets animated to appear on-click.

---

### Slide 1: Title Slide
* **Layout:** `Title Slide`
* **Title:** Custom Reusable Skills in OpenAI Codex
* **Subtitle:** Standardizing Workflows with `SKILL.md` in the VS Code GUI
* **Author:** [Your Name]
* **Credentials/Handle:** Lead Architect | @YourHandle
* **Duration:** 0:00 – 0:25 (25 seconds)

---

### Slide 2: Overview & WIIFM
* **Layout:** `Overview/Summary`
* **Header:** What's In It For You?
* **Subheader:** Beyond One-Off Prompting
* **Bullets (Animate On Click):**
  1. *The Repetition Tax:* Copy-pasting long prompt templates into chat wastes engineering hours.
  2. *The Custom Skill Paradigm:* Packaging reusable prompts, rules, and schemas into `SKILL.md`.
  3. *Today's Goal:* Learn to build and trigger custom skills directly in the Codex VS Code GUI with `@mentions`.
* **Duration:** 0:25 – 1:10 (45 seconds)

---

### Slide 3: The Team Documentation Dilemma
* **Layout:** `Two Text Chunking`
* **Header:** The Problem: Inconsistent API Specs
* **Left Column:**
  * **The Team Standard**
  * Parameter schemas & data types.
  * Complete error status matrices (400, 402, 500).
  * Copy-pasteable cURL examples.
* **Right Column:**
  * **The Reality in PRs**
  * Developers omit error scenarios.
  * Inconsistent markdown formatting.
  * Constant review friction.
* **Duration:** 1:10 – 1:35 (25 seconds)

---

### Slide 4: Anatomy of a Codex Skill
* **Layout:** `Three Text Chunking`
* **Header:** How Codex Discovers Skills
* **Column 1:**
  * **1. Location**
  * Stored in `.codex/skills/<skill-name>/` in your git repo.
* **Column 2:**
  * **2. YAML Frontmatter**
  * Defines the display name, description, and GUI autocomplete trigger.
* **Column 3:**
  * **3. Execution Rules**
  * Step-by-step markdown instructions and required output templates.
* **Duration:** 1:35 – 2:05 (30 seconds)

---

### Slide 5: The Skill Manifest Pattern
* **Layout:** `Code Notes Dark`
* **Header:** The `SKILL.md` Manifest
* **Code / Text Box:**
  ```yaml
  ---
  name: api-docgen
  description: Generates enterprise API docs with error matrices
  ---
  ## Instructions
  1. Parse route definitions and Pydantic/TypeScript schemas.
  2. Document all 2xx, 4xx, and 5xx response codes.
  3. Generate a copy-pasteable cURL example.
  ```
* **Duration:** 2:05 – 2:35 (30 seconds)

---

### Slide 6: Demo Transition Slide
* **Layout:** `Demo (Optional)`
* **Title:** Live Demonstration
* **Subtitle:** Invoking a Custom Skill from the Codex Extension Panel
* **Duration:** 2:35 – 2:45 (10 seconds)

---

### [LIVE DEMO SCREENCAST: 2:45 – 5:45 (3 minutes)]
* **Environment:** VS Code showing file tree and Codex extension side panel.
* **Visual Styling:** 125% zoom, callout bounding boxes over the `@` autocomplete dropdown and generated markdown artifact.

---

### Slide 7: Summary & Practical Takeaways
* **Layout:** `Overview/Summary`
* **Header:** Summary: Practical Takeaways
* **Bullets (Animate On Click):**
  1. *Version Control Your Workflows:* Store team skills in `.codex/skills/` alongside project code.
  2. *Intuitive GUI Discoverability:* Trigger skills with `@mention` directly in the Codex panel.
  3. *Eliminate Spec Inconsistency:* Guarantee standardized outputs across junior and senior engineers alike.
* **Duration:** 5:45 – 6:30 (45 seconds)
