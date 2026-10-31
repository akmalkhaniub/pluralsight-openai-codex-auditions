# Timed Narration Script: Custom Reusable Skills in OpenAI Codex (VS Code GUI)

* **Target Video Length:** 6 minutes 30 seconds
* **Audio Track Standard:** Clear studio sound, 48kHz / 24-bit, separate audio track, zero mouse/keyboard clicks.
* **Screen Resolution:** 1920x1080 at 125% IDE scale.

---

### [0:00 - 0:25] Slide 1: Title Slide
* **Visual:** Slide 1 displayed.
* **Speaker Tone:** Authoritative, welcoming, enthusiastic.
* **Narration:**
> "Hello everyone, and welcome! My name is [Your Name]. In this session, we’re learning how to **Build and Trigger Custom Reusable Skills using `SKILL.md` in the OpenAI Codex VS Code Extension**."
> 
> *[1-second intentional pause]*
> 
> "While one-off prompting works for quick questions, repeating the same complex multi-step instructions across a team is inefficient and error-prone."

---

### [0:25 - 1:10] Slide 2: Overview & WIIFM
* **Visual:** Slide 2 displayed. Click bullets in sync.
* **Speaker Tone:** Conversational, practical.
* **Narration:**
> *[Click Bullet 1]*  
> "Every engineering team has recurring tasks—like generating API docs, auditing security headers, or formatting release notes. Copy-pasting giant prompt templates from a team wiki wastes time.  
> 
> *[Click Bullet 2]*  
> Instead, OpenAI Codex allows you to package workflows into modular, reusable **Skills** committed directly to your repository.  
> 
> *[Click Bullet 3]*  
> In this audition, you’ll learn how to structure a `SKILL.md` manifest and invoke it with a single `@mention` click inside the Codex VS Code interface."

---

### [1:10 - 1:35] Slide 3: The Team Documentation Dilemma
* **Visual:** Slide 3 displayed.
* **Speaker Tone:** Relatable, problem-focused.
* **Narration:**
> "Consider Priya, a lead architect. Her team requires comprehensive markdown documentation for all API routes, including error status matrices and curl examples.  
> 
> Junior engineers constantly miss edge cases, resulting in back-and-forth PR reviews.  
> Priya’s solution is to encapsulate the team’s documentation standard into a reusable Codex Skill."

---

### [1:35 - 2:05] Slide 4: Anatomy of a Codex Skill
* **Visual:** Slide 4 displayed. Animate columns.
* **Speaker Tone:** Educational, clear.
* **Narration:**
> "A Codex skill lives right inside your repository under `.codex/skills/`.  
> Inside this folder, a single file called `SKILL.md` defines everything:  
> The YAML header provides metadata that the Codex GUI reads to populate its menus.  
> The markdown body provides the strict instructions and output schema the AI must follow."

---

### [2:05 - 2:35] Slide 5: The Skill Manifest Pattern
* **Visual:** Slide 5 displayed (Code notes).
* **Speaker Tone:** Practical, guiding.
* **Narration:**
> "Here is our `SKILL.md`. Notice the frontmatter: it has a name, `api-docgen`, and a clear description.  
> In the instructions, we explicitly mandate the three steps every team member needs: parse the schema, document all status codes, and generate a cURL example.  
> Let's see how this appears in the VS Code GUI."

---

### [2:35 - 2:45] Slide 6: Demo Transition
* **Visual:** Slide 6 displayed.
* **Narration:**
> "Let's switch into VS Code and see how easy it is to trigger our custom skill."

---

### [2:45 - 5:45] LIVE DEMO SCREENCAST (VS Code GUI)

#### Step 1: The Skill Manifest in the File Tree [2:45 - 3:20]
* **Screen:** VS Code file tree. Highlight `.codex/skills/api-docgen/SKILL.md`.
* **Visual Cue:** `[CALLOUT BOX: Highlight SKILL.md in the file explorer]` *(Hand off mouse; no cursor circling)*.
* **Narration:**
> "In our project explorer, look inside `.codex/skills/api-docgen/`. Here is our `SKILL.md` file committed to version control. Because it’s in this repository folder, the Codex extension automatically discovers it on startup."

#### Step 2: The Target Controller [3:20 - 4:00]
* **Screen:** Open `controllers/payment.py` in the main editor.
* **Visual Cue:** `[CALLOUT BOX: Highlight lines showing payment route with error handlers]`.
* **Narration:**
> "Now look at `controllers/payment.py`. We have a payment processing endpoint with validation logic, fraud check exceptions, and a Stripe webhook call. Documenting all these status codes manually would take 15 minutes of digging."

#### Step 3: Triggering the Skill in the Codex GUI [4:00 - 4:55]
* **Screen:** Open the Codex extension panel on the right.
* **Action:** Type `@` or click the Skill icon in the Codex input box. Select `api-docgen` from the auto-complete dropdown. Attach `#controllers/payment.py`.
* **Visual Cue:** `[CALLOUT BOX: Highlight the "@api-docgen" chip in the prompt box]`.
* **Narration:**
> "Now watch the Codex panel on the right. We type the `@` symbol, and look: `api-docgen` appears right in the extension's autocompletion menu with its description.  
> 
> We select `api-docgen` and tag `#controllers/payment.py`.  
> We don't need to write any custom instructions—the skill already contains all the rules. We hit Enter."

#### Step 4: Reviewing the Generated Artifact [4:55 - 5:45]
* **Screen:** Codex creates `docs/api/payment.md` and displays a preview in VS Code.
* **Visual Cue:** `[CALLOUT BOX: Highlight the formatted Markdown table showing 200, 400, 402, and 500 status codes]`.
* **Narration:**
> "Look at the output stream. Codex read the instructions from `SKILL.md` and created `docs/api/payment.md`.  
> Look at the generated markdown:  
> It created an accurate parameter table.  
> It extracted every single exception—from 400 Bad Request to 402 Payment Required—into a clean status matrix.  
> And it generated an exact, copy-pasteable cURL command.  
> 
> With a single click, any developer on Priya’s team can produce standardized, production-grade documentation."

---

### [5:45 - 6:30] Slide 7: Summary & Practical Takeaways
* **Visual:** Slide 7 displayed. Click bullets in sync.
* **Speaker Tone:** Energized, closing.
* **Narration:**
> *[Click Bullet 1]*  
> "To summarize:  
> Turn repetitive developer workflows into reusable skills using `SKILL.md`.  
> 
> *[Click Bullet 2]*  
> Leverage the VS Code Codex extension GUI to make these skills discoverable across your entire engineering team.  
> 
> *[Click Bullet 3]*  
> And eliminate human error by enforcing consistent output templates.  
> 
> Thank you for watching, and start building your team’s custom skills today!"
