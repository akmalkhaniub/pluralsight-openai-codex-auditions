# Audition: Team Rules for OpenAI Codex with AGENTS.md (v5)

## Files
- `Audition Outline - Akmal Khan - AGENTS.md v5.docx`: built from the blank Author Kit template
- `Audition Slides - Akmal Khan - AGENTS.md v5.pptx` + `Audition Slides - preview.pdf`: 8 slides with diagrams, click builds, callouts and speaker notes
- `TIMED_NARRATION_SCRIPT.md`: 7:15 script with click, callout and switch cues
- `SLIDE_DECK_CONTENT.md`: per-slide visuals and build order
- `RECORDING_AND_DEMO_GUIDE.md`: how to record, the step-by-step demo in the Codex app, reset and editing checklist
- `CODEX_PROMPTS.txt`: the exact task prompt
- `demo_reference_storyboard.mp4`: 2:18 silent reference built from real screenshots of the rehearsal, with callouts. **Not the audition recording.**
- `demo-code/`: `AGENTS.md` and `rehearsal-with-rules.diff` (what Codex produced with the rules)
- `verify_demo.py`: runs the demo repo's tests

The live demo projects are in the project root: `agents-take` (repo, clean, no AGENTS.md) and `agents-kit/AGENTS.md`.


## What changed in v5
- **Story continuity:** every story slide has a Mon-Fri tracker, and each title starts with its day. Wednesday is now its own beat ("new tasks, same three comments"). Friday's demo is framed as "rerun Tuesday's task".
- **The name "Maliha" is used only where she acts** (onboarding Sam, reviewing, the Thursday quote, approving). Elsewhere it says "the team's".
- **No dark slides**, a few emojis for the characters, and more varied animations and slide transitions (see SLIDE_DECK_CONTENT.md).

## What changed in v4
- **Rebuilt as a story:** one week in Maliha's team. Monday a new hire is onboarded; Tuesday Codex joins with no onboarding; three review rounds on every task; AGENTS.md becomes Codex's onboarding note; Friday the same prompt passes review first time.
- **15 slides instead of 8,** each on screen for 10-25 seconds, using more of the Pluralsight template: Title Only, Important Statement, Quotation, Definition, Comparison, Code Dark, Demo and Summary. No more half-split slides for the story beats.
- The demo is unchanged (same rehearsed steps and results); it now sits inside the story and hands back to the "Friday" slide.
- Runtime about 8:00 (within the 7-8 minute target).
- The outline is updated to match, in bullets.

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
