# Video Audition Outline - Pluralsight

| Audition Information | |
| :--- | :--- |
| **Title** | Visual Multi-File Refactoring in OpenAI Codex (VS Code GUI) |
| **Author Name** | [Your Name] |
| **Level** | Intermediate |
| **Additional Notes** | Focuses on using multi-file `#file` tagging in the Codex VS Code extension side panel, navigating the visual "Modified Files" tree, and executing synchronized cross-file refactoring. |

| Course Planning | |
| :--- | :--- |
| **Learner Prerequisites** | Intermediate Python/FastAPI knowledge, understanding of API serialization schemas (Pydantic), and familiarity with VS Code editor features. |
| **Storyline** | Alex is modernizing an API to support a new frontend client that requires camelCase JSON responses (`firstName`, `userRole`) instead of legacy snake_case. This requires synchronized modifications across three interdependent files: `schemas/user.py`, `services/user_service.py`, and `routes/user_routes.py`. Missing a single field will break the frontend contract. Alex uses multi-file referencing in the Codex GUI to coordinate the refactor, inspects each file diff via the extension's change tree, and applies the changes with one click. |
| **Description** | In this audition you’ll learn to coordinate multi-file refactoring workflows using the OpenAI Codex Extension GUI in VS Code. When you’re finished with this audition, you’ll have the skills and knowledge of Codex multi-file tagging, change-tree navigation, and synchronized diff reviews needed to execute cross-file architectural changes with complete confidence and zero broken references. |

| Course Organization | |
| :---: | :--- | :--- |
| **1** | **Audition Overview**<br>• Title slide & introduction.<br>• WIIFM: The risk of manual multi-file edits (tab fatigue, broken variable references) and how Codex coordinates them.<br>• Sneak peek: Synchronized camelCase refactor across 3 interdependent files verified passing tests. | **70 seconds (1:10)** |
| **2** | **Conceptual Foundation: Coordinated Multi-File Refactoring**<br>• *Slide 1:* The Ripple Effect: Why single-file edits break interdependent modules.<br>• *Slide 2:* The Codex GUI Multi-File Pattern: Tagging multiple `#file` references in one cohesive prompt.<br>• *Slide 3:* The Review Checklist Principle: Auditing diffs file-by-file before clicking 'Accept All'. | **2:15 minutes** |
| **3** | **Demo: Cross-File Refactoring Live in the Codex GUI**<br>• *Step 1:* Show `schemas/user.py`, `services/user_service.py`, and `routes/user_routes.py` with legacy snake_case.<br>• *Step 2:* Open the Codex side panel and tag all 3 files with the camelCase refactoring instruction.<br>• *Step 3:* Walk through the "Modified Files" tree in the Codex panel, clicking each file to show the synchronized diff.<br>• *Step 4:* Click **Accept All Changes**, run `pytest test_api.py` in the terminal, and verify 100% green tests. | **3:00 minutes** |
| **4** | **Conclusion**<br>• Practical takeaways: Cross-file context tagging, visual change trees, and coordinated commits.<br>• Next Steps: Refactoring across Git branches and worktrees. | **0:45 seconds** |
| **Total Duration** | | **~7:10 minutes** |
