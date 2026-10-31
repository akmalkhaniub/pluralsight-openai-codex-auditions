# Pluralsight Video Audition Packages: OpenAI Codex

This repository contains complete, production-ready audition packages designed specifically for the **Pluralsight Author Audition** on **OpenAI Codex**. Every package is engineered to satisfy Pluralsight's 5–8 minute audition requirements and scoring rubric.

---

## 🎯 Featured GUI-Driven Packages (VS Code Codex Extension)

These three packages are tailored specifically for developers demonstrating the **OpenAI Codex Extension inside VS Code (GUI interface)**—featuring context pinning (`#file`), visual side-by-side diff viewers, `@mention` skill autocompletion, and the extension's "Modified Files" review tree:

| Package | Audition Title | Screencast Focus (VS Code GUI) | Target Time |
| :--- | :--- | :--- | :---: |
| [**05-gui-autonomous-tdd-loop**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/05-gui-autonomous-tdd-loop/README.md) | *The Autonomous TDD Loop in OpenAI Codex* | Pinning `#test_discounts.py` in the Codex panel $\rightarrow$ Reviewing editor diff $\rightarrow$ One-click Accept $\rightarrow$ 100% Green. | ~6:30 |
| [**06-gui-custom-skills**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/06-gui-custom-skills/README.md) | *Custom Reusable Skills in OpenAI Codex* | Packaging `.codex/skills/` $\rightarrow$ Triggering `@api-docgen` via GUI dropdown $\rightarrow$ Reviewing generated markdown doc. | ~6:30 |
| [**07-gui-visual-multifile-refactor**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/07-gui-visual-multifile-refactor/README.md) | *Visual Multi-File Refactoring in OpenAI Codex* | Tagging 3 files (`#schemas`, `#services`, `#routes`) $\rightarrow$ Navigating the "Modified Files" tree $\rightarrow$ "Accept All Changes". | ~6:30 |

---

## 📂 Additional Architecture & Ecosystem Packages

| Package | Audition Title | Focus Area | Target Time |
| :--- | :--- | :--- | :---: |
| [**01-rapid-codebase-onboarding**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/01-rapid-codebase-onboarding/README.md) | *Rapid Codebase Onboarding Using OpenAI Codex* | Scoped prompt traversal from route to middleware down to DB. | ~7:15 |
| [**02-governing-standards-agents-md**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/02-governing-standards-agents-md/README.md) | *Governing OpenAI Codex with `AGENTS.md`* | Enforcing package whitelists, error hierarchies, and test mandates. | ~7:15 |
| [**03-safe-multifile-refactoring**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/03-safe-multifile-refactoring/README.md) | *Safe Multi-File Refactoring and Verification* | Sync-to-async data engine refactor with sandboxed `pytest` verification. | ~7:15 |
| [**04-supercharging-codex-with-mcp**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/04-supercharging-codex-with-mcp/README.md) | *Supercharging OpenAI Codex with MCP* | Connecting Codex to a Model Context Protocol server to inspect live DB schemas. | ~7:15 |
| [**08-codex-skills-release-notes**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/08-codex-skills-release-notes/version1/README.md) | *Reusable Team Workflows with Codex Skills* | Automated release notes generator, semantic versioning, and changelog drafting. | ~7:15 |
| [**09-agents-md-team-rules**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/09-agents-md-team-rules/version1/README.md) | *Team Rules for OpenAI Codex with AGENTS.md* | Deterministic error handling rules, test execution gates, and docstring standards. | ~7:15 |
| [**10-codex-code-review**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/10-codex-code-review/version1/README.md) | *Who Reviews the AI? Code Review with OpenAI Codex* | Automated PR code review, finding security risks in AI-generated code, targeted fixes. | ~7:35 |


---

## Package Directory Structure

Every topic folder is fully autonomous and contains:
1. `AUDITION_OUTLINE.md`: The official filled-out Pluralsight Video Audition Outline form.
2. `SLIDE_DECK_CONTENT.md`: Slide-by-slide copy with animation triggers mapped to Pluralsight's PowerPoint template.
3. `TIMED_NARRATION_SCRIPT.md`: Exact word-for-word spoken transcript with second-by-second timestamps and visual callout cues.
4. `README.md`: Step-by-step recording checklist and setup guide.
5. `demo-code/`: Working sample projects, configuration files, test suites, and pre-formatted prompt texts.

---

## Pluralsight Audition Recording Best Practices

* **Screen Setup:** 1920x1080 (16:9), 125% IDE scaling, dark theme. Hide unnecessary sidebars (`Ctrl+B`).
* **Mouse Discipline:** **Strictly DO NOT circle or wave the mouse cursor.** Keep hands off the mouse during spoken explanations. All highlights should be added in post-production using colored bounding boxes (orange/blue).
* **Audio Track:** Record clean vocal audio on a dedicated track (48kHz, 24-bit). Ensure zero keyboard clatter or fan noise.
* **Timing:** Strictly between **5 and 8 minutes** (all scripts are timed to ~6:30–7:15).
