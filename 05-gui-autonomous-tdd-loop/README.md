> **Finalized TDD audition:** Use [the updated package](finalized/README.md), including the completed official DOCX outline, slides, script and verified demo. The files below describe the earlier draft.

# Topic 5: The Autonomous TDD Loop in OpenAI Codex (VS Code GUI)

## Package Contents
* `AUDITION_OUTLINE.md`: The official filled-out Pluralsight Video Audition Outline form.
* `SLIDE_DECK_CONTENT.md`: Slide-by-slide layout matching the Pluralsight PowerPoint template with on-click animation cues.
* `TIMED_NARRATION_SCRIPT.md`: Word-for-word spoken transcript with second-by-second timestamps and visual callout instructions.
* `demo-code/`: The unit test suite (`test_discounts.py`), empty implementation (`discount_service.py`), and GUI prompts.

## How to Record Your Audition
1. **Prepare Slides:** Copy `SLIDE_DECK_CONTENT.md` into the Pluralsight PowerPoint template. Set bullets to appear one at a time.
2. **Setup the Screencast in VS Code:**
   * Open the `demo-code/` folder in VS Code.
   * Open the terminal at the bottom (`Ctrl+\``) and run `pytest test_discounts.py` to show the red failure.
   * Open the Codex extension panel on the right (`Ctrl+Shift+P` -> Codex: Open Chat).
   * Paste the prompt from `codex_gui_prompts.txt` with `#test_discounts.py` attached.
   * Show the side-by-side visual diff that opens in the editor.
   * Click **Accept** in the VS Code editor toolbar.
   * In the terminal, re-run `pytest test_discounts.py` to confirm 4 passed (100% green).
3. **Target Video Duration:** 6 minutes 30 seconds.
