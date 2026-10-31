# Audition: Team Rules for OpenAI Codex with AGENTS.md (v1)

## Files
- `Audition Outline - Akmal Khan - AGENTS.md v1.docx`: built from the blank Author Kit template
- `Audition Slides - Akmal Khan - AGENTS.md v1.pptx` + `Audition Slides - preview.pdf`: 8 slides with diagrams, click builds, callouts and speaker notes
- `TIMED_NARRATION_SCRIPT.md`: 7:15 script with click, callout and switch cues
- `SLIDE_DECK_CONTENT.md`: per-slide visuals and build order
- `RECORDING_AND_DEMO_GUIDE.md`: how to record, the step-by-step demo in the Codex app, reset and editing checklist
- `CODEX_PROMPTS.txt`: the exact task prompt
- `demo_reference_storyboard.mp4`: 2:18 silent reference built from real screenshots of the rehearsal, with callouts. **Not the audition recording.**
- `demo-code/`: `AGENTS.md` and `rehearsal-with-rules.diff` (what Codex produced with the rules)
- `verify_demo.py`: runs the demo repo's tests

The live demo projects are in the project root: `agents-take` (repo, clean, no AGENTS.md) and `agents-kit/AGENTS.md`.

## Rehearsal results (Codex app, 27 Sep 2026)
| Rule | Without AGENTS.md | With AGENTS.md |
|------|-------------------|----------------|
| Invalid input | `raise ValueError("Invalid coupon code")` | `raise AppError("INVALID_COUPON", …)` |
| Docstring `Example:` line | missing | present |
| Tests | added (Codex did this on its own) | added |
| Test command | its own choice | `python -m unittest discover -s tests -v` |
| CHANGELOG.md | untouched (2 files changed) | one line under Unreleased (3 files changed) |
| Time | 7.7 min | 4 min |

## Next steps
1. Step through the deck in PowerPoint Slide Show and check the animations.
2. Watch the storyboard video, then do one timed practice run using the guide.
3. Send the outline to your Author Evangelist.
