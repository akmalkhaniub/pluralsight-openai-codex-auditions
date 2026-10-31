# Audition: Team Rules for OpenAI Codex with AGENTS.md (v2)

## Files
- `Audition Outline - Akmal Khan - AGENTS.md v2.docx`: built from the blank Author Kit template
- `Audition Slides - Akmal Khan - AGENTS.md v2.pptx` + `Audition Slides - preview.pdf`: 8 slides with diagrams, click builds, callouts and speaker notes
- `TIMED_NARRATION_SCRIPT.md`: 7:15 script with click, callout and switch cues
- `SLIDE_DECK_CONTENT.md`: per-slide visuals and build order
- `RECORDING_AND_DEMO_GUIDE.md`: how to record, the step-by-step demo in the Codex app, reset and editing checklist
- `CODEX_PROMPTS.txt`: the exact task prompt
- `demo_reference_storyboard.mp4`: 2:18 silent reference built from real screenshots of the rehearsal, with callouts. **Not the audition recording.**
- `demo-code/`: `AGENTS.md` and `rehearsal-with-rules.diff` (what Codex produced with the rules)
- `verify_demo.py`: runs the demo repo's tests

The live demo projects are in the project root: `agents-take` (repo, clean, no AGENTS.md) and `agents-kit/AGENTS.md`.


## What changed in v2
- The story character is now **Maliha**.
- **One objective:** write checkable rules in a root AGENTS.md and prove in the diff that Codex followed them.
- **WIIFM** is explicit: a "What's in it for you" box on slide 2 and a matching line in the script.
- Slide 3 is now **weak rule vs checkable rule** (it was "where files live").
- Slide 4 is now the **analogy**: AGENTS.md is an onboarding note Codex rereads every task (it was the layering diagram).
- The global/folder/32 KiB trivia is gone, and the outline is rewritten in short, plain sentences.
- The **ah-ha** moment (same prompt, one Markdown file, different diff) is named in the outline and marked in the script.

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
