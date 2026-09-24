# Video Audition Outline - Pluralsight

| Audition Information | |
| :--- | :--- |
| **Title** | Governing OpenAI Codex: Enforcing Architecture Rules with `AGENTS.md` |
| **Author Name** | [Your Name] |
| **Level** | Intermediate |
| **Additional Notes** | Focuses on how tech leads and senior engineers enforce repository-level coding conventions, forbidden dependencies, and test requirements for OpenAI Codex using declarative `AGENTS.md` configuration. |

| Course Planning | |
| :--- | :--- |
| **Learner Prerequisites** | Basic understanding of project architecture (design patterns, test placement), Git, and foundational experience using AI coding assistants. |
| **Storyline** | Maya is a senior engineer whose team recently adopted OpenAI Codex. While developers love the speed, Codex frequently introduces spec drift: it suggests deprecated third-party libraries, puts tests in the wrong directory, and bypasses the team's standardized error handling classes. Maya configures an `AGENTS.md` file in the repository root to permanently anchor Codex's behavior to team conventions without repetitive manual prompting. |
| **Description** | In this audition you’ll learn to standardize and govern OpenAI Codex's output using repository-level `AGENTS.md` files. When you’re finished with this audition, you’ll have the skills and knowledge of OpenAI Codex configuration and rule constraints needed to eliminate spec drift, enforce architectural standards, and guarantee production-ready code generation across your team. |

| Course Organization | |
| :---: | :--- | :--- |
| **1** | **Audition Overview**<br>• Title slide & introduction.<br>• WIIFM: Why unguided AI code generates technical debt and how repository governance fixes it.<br>• Preview: Side-by-side comparison of "Wild West" code generation vs. "Governed" code generation. | **70 seconds (1:10)** |
| **2** | **Conceptual Foundation: The Anatomy of `AGENTS.md`**<br>• *Slide 1:* The "Prompt Fatigue" Trap (Copy-pasting rules in every prompt vs. centralizing repo governance).<br>• *Slide 2:* Discovery & Precedence: How Codex automatically ingests `AGENTS.md` on startup.<br>• *Slide 3:* The 4 Pillars of a Production `AGENTS.md`: Architectural Boundaries, Dependency Whitelists, Error Handling, and Test Placement. | **2:20 minutes** |
| **3** | **Demo: Enforcing Standards Live in Codex**<br>• *Step 1:* Run an ungoverned prompt: *"Create an OrderNotificationService that calls an external webhook"* $\rightarrow$ Codex uses deprecated `requests` with raw `print` statements and saves it to root `/src`.<br>• *Step 2:* Introduce the `AGENTS.md` configuration with highlighted callouts.<br>• *Step 3:* Re-run the prompt in Codex.<br>• *Step 4:* Verify: Codex cites `AGENTS.md`, uses `httpx`, implements `AppError`, and automatically creates `tests/services/test_order_notification.py`. | **3:00 minutes** |
| **4** | **Conclusion**<br>• Summary: Why repository rules belong in version control, not in chat memory.<br>• Next Steps: Adding CI linters to validate `AGENTS.md` compliance. | **0:45 seconds** |
| **Total Duration** | | **~7:15 minutes** |
