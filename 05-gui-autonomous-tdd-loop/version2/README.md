# TDD Audition — version 2

Revised after the rubric review. The materials in `../finalized` are unchanged.

## Files
- `Audition Slides - Akmal Khan - TDD v2.pptx`: redesigned deck with diagrams, click builds, callouts and the narration in the speaker notes
- `Audition Slides - preview.pdf`: static preview of the deck (no animations)
- `Audition Outline - Akmal Khan - TDD v2.docx`: outline in the official template, updated to match
- `RECORDING_AND_DEMO_GUIDE.md`: when to switch between slides and demo, how to record and merge the clips, and a step-by-step demo runbook for the Codex app on Windows
- `demo_reference_storyboard.mp4`: 2:40 silent reference built from real screenshots of a practice run in your Codex app, with the callouts in place. For timing and layout only; it is not the audition recording
- `rehearsal/codex-app-run-green.py`: the actual implementation Codex wrote in the practice run
- `TIMED_NARRATION_SCRIPT.md`: rewritten script with click cues and callout cues
- `SLIDE_DECK_CONTENT.md`: slide-by-slide visuals and build order
- `CODEX_PROMPTS.txt`, `demo-code/`, `rehearsal/`, `verify_demo.py`: copied from `finalized` (the demo is unchanged)

## What changed
**Slides**
- The eight slides now use six different visual forms: title, receipt with callout, highlighted boundary table, cycle diagram, code block with callouts, numbered roadmap and question-plus-flow. Previously six of eight slides were four plain bullets.
- The boundary table adds the $100.05 → $90.05 rounding row, which the narration had promised but the slide did not show.
- The prompt slide shows the actual prompt, not a description of it.
- Every content slide builds on click (26 builds in total).
- The title now matches the outline: Akmal Khan, Senior Full Stack AI Architect, with your photo. The mixed bullet indentation on slides 6 and 7 is fixed.

**Script**
- Opens with a hook, not "In this lesson we'll…".
- Most hedging sentences are removed. The honest limit ("green proves only what you tested") is said once, in the summary.
- The demo gives clear verdicts ("This line matters most: greater than or equal").
- Adds a technical teaching point: unittest reports *errors*, not *failures*, before the implementation exists.
- Adds a plan for when Codex's result differs from what you expect; it is kept separate from the spoken script.
- Pace: about 825 words over 7:15. The busiest slide runs at about 140 words per minute; the demo is slower to leave room for waiting and typing.

**Outline**
- Rebuilt from the original `Audition Outline Template (MAKE A COPY).docx` in the Author Kit, keeping every template instruction line and time hint. The template's 'Slide portion' instructions sit in a stray table in the page footer; they are moved into row 2 where they belong, and the stray footer table is removed.
- The Description follows the Pluralsight sentence pattern exactly. The storyline names the one-character bug. The slide and demo rows match the new deck and script.

## Next steps
1. Open the deck in PowerPoint and step through Slide Show mode to check the animations.
2. Do a timed read-through with the slides and adjust any section that runs long.
3. Submit the outline to your Author Evangelist, then record.
