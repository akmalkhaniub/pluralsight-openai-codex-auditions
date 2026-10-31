# Topic 6: Custom Reusable Skills in OpenAI Codex (VS Code GUI)

## Package Contents
* `AUDITION_OUTLINE.md`: The official filled-out Pluralsight Video Audition Outline form.
* `SLIDE_DECK_CONTENT.md`: Slide-by-slide layout matching the Pluralsight PowerPoint template with on-click animation cues.
* `TIMED_NARRATION_SCRIPT.md`: Word-for-word spoken transcript with second-by-second timestamps and visual callout instructions.
* `demo-code/`: The `.codex/skills/api-docgen/` directory, the target `controllers/payment.py`, and GUI prompts.

## How to Record Your Audition
1. **Prepare Slides:** Copy `SLIDE_DECK_CONTENT.md` into the Pluralsight PowerPoint template. Set bullets to appear one at a time.
2. **Setup the Screencast in VS Code:**
   * Open the `demo-code/` folder in VS Code.
   * Highlight `.codex/skills/api-docgen/SKILL.md` in the file tree (use an orange callout box; do not circle with mouse).
   * Open `controllers/payment.py` in the editor.
   * Open the Codex extension side panel on the right.
   * Type `@api-docgen #controllers/payment.py` and hit Enter.
   * Watch Codex generate `docs/api/payment.md` with parameters, status code matrix, and cURL snippet.
3. **Target Video Duration:** 6 minutes 30 seconds.
