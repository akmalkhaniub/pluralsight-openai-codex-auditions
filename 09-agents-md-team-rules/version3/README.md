# Audition: Team Rules for OpenAI Codex with AGENTS.md (v3)

## Files
- `Audition Outline - Akmal Khan - AGENTS.md v3.docx`: built from the blank Author Kit template
- `Audition Slides - Akmal Khan - AGENTS.md v3.pptx` + `Audition Slides - preview.pdf`: 8 slides with diagrams, click builds, callouts and speaker notes
- `TIMED_NARRATION_SCRIPT.md`: 7:15 script with click, callout and switch cues
- `SLIDE_DECK_CONTENT.md`: per-slide visuals and build order
- `RECORDING_AND_DEMO_GUIDE.md`: how to record, the step-by-step demo in the Codex app, reset and editing checklist
- `CODEX_PROMPTS.txt`: the exact task prompt
- `demo_reference_storyboard.mp4`: 2:18 silent reference built from real screenshots of the rehearsal, with callouts. **Not the audition recording.**
- `demo-code/`: `AGENTS.md` and `rehearsal-with-rules.diff` (what Codex produced with the rules)
- `verify_demo.py`: runs the demo repo's tests

The live demo projects are in the project root: `agents-take` (repo, clean, no AGENTS.md) and `agents-kit/AGENTS.md`.


## What changed in v3
- **The slides were rebuilt around one storyline:** Problem → 1 Meet AGENTS.md → 2 Write rules you can check → Maliha's comments become rules → 3 Prove it → Practice → Summary.
- Slide 2 now has a 3-step agenda, and the step numbers appear on the slides that follow.
- The new slide 3 explains what AGENTS.md is (repo tree, read order, onboarding-note analogy) *before* slide 4 shows how to write rules.
- The new slide 5 connects Maliha's review comments on slide 2 to the lines in her AGENTS.md.
- Larger text and fuller layouts. Summary is the last slide, and the template icons appear instantly.
- **The outline is now bullet points**, including the Audition Overview row.

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
