# Video Audition Outline - Pluralsight

| Audition Information | |
| :--- | :--- |
| **Title** | Safe Multi-File Refactoring and Verification with OpenAI Codex |
| **Author Name** | [Your Name] |
| **Level** | Intermediate |
| **Additional Notes** | Focuses on using OpenAI Codex’s multi-file planning, worktree isolation, and automated test sandbox execution to modernize legacy codebases without regressions. |

| Course Planning | |
| :--- | :--- |
| **Learner Prerequisites** | Intermediate Python experience, understanding of synchronous vs asynchronous programming, familiarity with `pytest`, and Git branching. |
| **Storyline** | Sam is an engineer tasked with modernizing a synchronous, memory-heavy CSV ingestion engine that causes server timeouts during large uploads. Refactoring this engine requires modifying the data engine, the API controller, and downstream batch callers simultaneously. Making edits manually across multiple files is risky and prone to silent breaking changes. Sam leverages OpenAI Codex to orchestrate the refactoring across all affected files in an isolated worktree and verify the changes against the test suite inside the Codex sandbox before committing. |
| **Description** | In this audition you’ll learn to orchestrate safe, multi-file refactoring workflows using OpenAI Codex. When you’re finished with this audition, you’ll have the skills and knowledge of OpenAI Codex’s refactoring cycles and sandboxed verification needed to modernize legacy modules with confidence and zero regressions. |

| Course Organization | |
| :---: | :--- | :--- |
| **1** | **Audition Overview**<br>• Title slide & introduction.<br>• WIIFM: How to eliminate the fear of multi-file refactoring in interdependent codebases.<br>• Preview: A 3-file refactor from sync to async streaming verified passing tests in under 3 minutes. | **75 seconds (1:15)** |
| **2** | **Conceptual Foundation: The 3-Stage Refactoring Cycle**<br>• *Slide 1:* The Refactoring Bottleneck (Why single-file AI prompts break downstream dependencies).<br>• *Slide 2:* Stage 1: Dependency Analysis & Multi-file Planning in Codex.<br>• *Slide 3:* Stages 2 & 3: Worktree Isolation & Sandboxed Test Verification. | **2:15 minutes** |
| **3** | **Demo: Refactoring a Data Pipeline Live in Codex**<br>• *Step 1:* Run baseline unit tests via pytest (Green baseline).<br>• *Step 2:* Issue refactoring objective to Codex: *"Refactor `DataIngestionEngine` to use async streaming generators; update calling controllers and verify tests."*<br>• *Step 3:* Callout overlays show Codex constructing the multi-file dependency plan and applying patches across `engine.py`, `controller.py`, and `test_pipeline.py`.<br>• *Step 4:* Watch Codex execute the test sandbox, catch an `await` mismatch, self-heal the test, and re-run to 100% green. | **3:00 minutes** |
| **4** | **Conclusion**<br>• Recap: The power of the Analyze $\rightarrow$ Plan $\rightarrow$ Execute $\rightarrow$ Verify cycle.<br>• Next Steps: Automating pull request generation with before/after benchmarks. | **0:45 seconds** |
| **Total Duration** | | **~7:15 minutes** |
