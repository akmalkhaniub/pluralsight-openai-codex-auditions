# Topic 3: Safe Multi-File Refactoring and Verification with OpenAI Codex

## Package Contents
* `AUDITION_OUTLINE.md`: The official filled-out Pluralsight Video Audition Outline form.
* `SLIDE_DECK_CONTENT.md`: Slide-by-slide layout matching the Pluralsight PowerPoint template with on-click animation cues.
* `TIMED_NARRATION_SCRIPT.md`: Word-for-word spoken transcript with second-by-second timestamps and visual callout instructions.
* `demo-code/`: The legacy pipeline codebase (`engine.py`, `controller.py`, `test_pipeline.py`).

## How to Record Your Audition
1. **Prepare Slides:** Copy `SLIDE_DECK_CONTENT.md` into the Pluralsight PowerPoint template. Set bullets to appear one at a time.
2. **Setup the Demo Screencast:**
   * Step 1: Open terminal in `demo-code/` and run `pytest test_pipeline.py`. Show green passing baseline.
   * Step 2: Open Codex panel. Paste the prompt from `codex_prompts.txt`.
   * Step 3: Watch Codex edit `engine.py`, `controller.py`, and `test_pipeline.py`.
   * Step 4: Show Codex running the test suite in the sandbox and confirming green passing status.
3. **Target Time:** 7 minutes 15 seconds.
