# Pluralsight Video Audition Packages: OpenAI Codex

This repository contains four complete, self-contained audition packages designed for the **Pluralsight Author Audition** on **OpenAI Codex**. Each package has been structured to satisfy Pluralsight's 5–8 minute audition requirements and scoring rubric.

---

## Audition Packages Overview

```
pluralsight-openai-codex-auditions/
├── 01-rapid-codebase-onboarding/
│   ├── AUDITION_OUTLINE.md          <-- Official Pluralsight Outline Table
│   ├── SLIDE_DECK_CONTENT.md        <-- Slide-by-slide text & animation triggers
│   ├── TIMED_NARRATION_SCRIPT.md    <-- Timed transcript with visual action cues
│   ├── README.md                    <-- Recording checklist & instructions
│   └── demo-code/                   <-- Multi-tier microservice with routes, middleware, models
│
├── 02-governing-standards-agents-md/
│   ├── AUDITION_OUTLINE.md
│   ├── SLIDE_DECK_CONTENT.md
│   ├── TIMED_NARRATION_SCRIPT.md
│   ├── README.md
│   └── demo-code/                   <-- AGENTS.md, AppError classes, and companion test targets
│
├── 03-safe-multifile-refactoring/
│   ├── AUDITION_OUTLINE.md
│   ├── SLIDE_DECK_CONTENT.md
│   ├── TIMED_NARRATION_SCRIPT.md
│   ├── README.md
│   └── demo-code/                   <-- Async data pipeline with pytest self-healing suite
│
└── 04-supercharging-codex-with-mcp/
    ├── AUDITION_OUTLINE.md
    ├── SLIDE_DECK_CONTENT.md
    ├── TIMED_NARRATION_SCRIPT.md
    ├── README.md
    └── demo-code/                   <-- Standalone SQLite MCP server & schema mismatch demo
```

---

## Detailed Comparison Matrix

| Topic Package | Level | Target Video Time | Demo Focus | Key Pluralsight Strength |
| :--- | :---: | :---: | :--- | :--- |
| [**01. Rapid Codebase Onboarding**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/01-rapid-codebase-onboarding/README.md) | Intermediate | ~7:15 | Codex tracing an undocumented auth pipeline from route to DB | **Most Relatable Story:** Solves the universal pain of joining an unfamiliar project. Effortless to record. |
| [**02. Governing Standards with AGENTS.md**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/02-governing-standards-agents-md/README.md) | Intermediate | ~7:15 | Enforcing forbidden packages, error types, and automatic test generation | **Enterprise Appeal:** High value for team leads; demonstrates governance and prompt fatigue elimination. |
| [**03. Safe Multi-File Refactoring**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/03-safe-multifile-refactoring/README.md) | Intermediate | ~7:15 | Multi-file sync-to-async refactor with sandboxed `pytest` verification | **High Technical Impact:** Shows worktree coordination, dependency mapping, and automated test self-healing. |
| [**04. Supercharging Codex with MCP**](file:///g:/ReplitProjects/pluralsight-openai-codex-auditions/04-supercharging-codex-with-mcp/README.md) | Advanced | ~7:15 | Resolving a live database schema discrepancy using an MCP server | **Cutting-Edge Modern Tech:** Highlights agent tool calling, environment awareness, and open standards. |

---

## Pluralsight Audition Recording Checklist

Before hitting record, ensure your setup meets these rubric criteria:

### 1. Screen & Editor Setup
* **Resolution:** 1920x1080 (16:9).
* **IDE Font Size:** 16pt–18pt (or 125%–150% UI zoom) so line numbers and code are legible on mobile.
* **Workspace Cleanliness:** Hide the VS Code status bar and sidebar (`Ctrl+B`). Close extraneous editor tabs.
* **Cursor Discipline:** **DO NOT circle or point at code with your mouse cursor.** Hand off mouse during explanations; use post-production bounding boxes (orange/blue) for callouts.

### 2. Audio & Narration Quality
* **Audio Track:** Record voice on a separate dedicated track (48kHz, 24-bit).
* **Environment:** Quiet room; no audible computer fans, room echo, keyboard clicks, or mouse taps.
* **Delivery:** Energetic, conversational, expert human tone (not robotic). Leave 1-second clean pauses between slide transitions.

### 3. Timing Constraint
* **Duration:** Keep the total video between **5:30 and 7:45**. (Rubric requires strictly 5–8 minutes; under 5 min fails, over 10 min fails).
