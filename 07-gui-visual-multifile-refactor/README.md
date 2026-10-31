# Topic 7: Visual Multi-File Refactoring in OpenAI Codex (VS Code GUI)

## Package Contents
* `AUDITION_OUTLINE.md`: The official filled-out Pluralsight Video Audition Outline form.
* `SLIDE_DECK_CONTENT.md`: Slide-by-slide layout matching the Pluralsight PowerPoint template with on-click animation cues.
* `TIMED_NARRATION_SCRIPT.md`: Word-for-word spoken transcript with second-by-second timestamps and visual callout instructions.
* `demo-code/`: The three interdependent files (`schemas/user.py`, `services/user_service.py`, `routes/user_routes.py`), test suite, and GUI prompts.

## How to Record Your Audition
1. **Prepare Slides:** Copy `SLIDE_DECK_CONTENT.md` into the Pluralsight PowerPoint template. Set bullets to appear one at a time.
2. **Setup the Screencast in VS Code:**
   * Open the `demo-code/` folder in VS Code.
   * Open `schemas/user.py`, `services/user_service.py`, and `routes/user_routes.py` across tabs.
   * Open the Codex extension side panel on the right.
   * Paste the prompt from `codex_gui_prompts.txt` with all 3 `#file` tags attached.
   * In the Codex panel, inspect the "Modified Files" tree, clicking through each file diff.
   * Click **Accept All Changes** in the Codex sidebar toolbar.
   * In the terminal, run `pytest test_api.py` to confirm verification.
3. **Target Video Duration:** 6 minutes 30 seconds.
