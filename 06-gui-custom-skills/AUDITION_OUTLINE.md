# Video Audition Outline - Pluralsight

| Audition Information | |
| :--- | :--- |
| **Title** | Building Custom Reusable Skills in OpenAI Codex (VS Code GUI) |
| **Author Name** | [Your Name] |
| **Level** | Intermediate |
| **Additional Notes** | Focuses on defining reusable team skills using `SKILL.md` inside `.codex/skills/` and triggering them visually via the `@mention` menu in the Codex VS Code Extension panel. |

| Course Planning | |
| :--- | :--- |
| **Learner Prerequisites** | Familiarity with Git repositories, basic REST API design, and experience using VS Code extensions. |
| **Storyline** | Priya is a lead architect whose engineering team must produce standardized API documentation for every endpoint, complete with parameter tables, error status code matrices, and cURL snippets. Developers often submit PRs with missing error cases because writing manual documentation takes too long. Priya creates a reusable `api-docgen` skill using `SKILL.md` that team members can trigger directly from the Codex GUI with a single `@mention`, generating standardized docs in seconds. |
| **Description** | In this audition you’ll learn to create and trigger custom reusable skills in OpenAI Codex using `SKILL.md` and the VS Code GUI. When you’re finished with this audition, you’ll have the skills and knowledge of Codex skill manifests, directory structures, and GUI `@mention` triggers needed to standardize complex workflows and eliminate repetitive manual prompting across your engineering team. |

| Course Organization | |
| :---: | :--- | :--- |
| **1** | **Audition Overview**<br>• Title slide & introduction.<br>• WIIFM: The cost of prompt repetition and inconsistent documentation across teams.<br>• Sneak peek: Invoking `@api-docgen` in the Codex GUI to produce a production-grade API documentation artifact. | **70 seconds (1:10)** |
| **2** | **Conceptual Foundation: The Anatomy of `SKILL.md`**<br>• *Slide 1:* Prompt Fatigue vs. Packaged Skills (Why team wikis fail).<br>• *Slide 2:* The Skill Structure: `.codex/skills/<skill-name>/SKILL.md` with YAML frontmatter.<br>• *Slide 3:* GUI Auto-Discovery: How the Codex VS Code extension parses skill manifests on boot. | **2:15 minutes** |
| **3** | **Demo: Triggering a Custom Skill in the Codex GUI**<br>• *Step 1:* Show `.codex/skills/api-docgen/SKILL.md` in the VS Code file explorer.<br>• *Step 2:* Open `controllers/payment.py` to show the endpoint with error conditions.<br>• *Step 3:* Open the Codex side panel, type `@`, and select `api-docgen` from the autocompletion menu, tagging `#controllers/payment.py`.<br>• *Step 4:* Review the generated markdown artifact (`docs/api/payment.md`) with clean status code tables and cURL examples. | **3:00 minutes** |
| **4** | **Conclusion**<br>• Practical takeaways: Packaging team standards, version-controlled skills, and GUI discoverability.<br>• Next Steps: Adding scripts and validators to custom skills. | **0:45 seconds** |
| **Total Duration** | | **~7:10 minutes** |
