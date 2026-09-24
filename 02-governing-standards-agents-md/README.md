# Topic 2: Governing OpenAI Codex with AGENTS.md

## Package Contents
* `AUDITION_OUTLINE.md`: The official filled-out Pluralsight Video Audition Outline form.
* `SLIDE_DECK_CONTENT.md`: Slide-by-slide layout matching the Pluralsight PowerPoint template with on-click animation cues.
* `TIMED_NARRATION_SCRIPT.md`: Word-for-word spoken transcript with second-by-second timestamps and visual callout instructions.
* `demo-code/`: The workspace featuring `AGENTS.md`, base error classes, and test fixtures.

## How to Record Your Audition
1. **Prepare Slides:** Copy `SLIDE_DECK_CONTENT.md` into the Pluralsight PowerPoint template. Set bullets to appear one at a time.
2. **Setup the Demo Screencast:**
   * Step 1: Temporarily rename `AGENTS.md` to `AGENTS.md.disabled`.
   * Run the prompt from `codex_prompts.txt` in Codex. Show the poor default output (blocking `requests`, silent error swallowing).
   * Step 2: Rename `AGENTS.md.disabled` back to `AGENTS.md`. Open it and explain the 4 pillars (highlighting with callout boxes, no cursor circling).
   * Step 3: Run the exact same prompt in Codex. Show Codex acknowledging `AGENTS.md`, using `httpx`, raising `NotificationDeliveryError`, and generating the companion test file in `tests/services/`.
3. **Target Time:** 7 minutes 15 seconds.
