# Audition: Team Rules for OpenAI Codex with AGENTS.md (v6)

## Files
- `Audition Outline - Akmal Khan - AGENTS.md v6.docx`: from the blank Author Kit template, in bullets
- `Audition Slides - Akmal Khan - AGENTS.md v6.pptx` + `Audition Slides - preview.pdf`: 11 slides, animations, speaker notes
- `TIMED_NARRATION_SCRIPT.md`: about 7:30, with click, callout and switch cues
- `SLIDE_DECK_CONTENT.md`: per-slide visuals and build order
- `RECORDING_AND_DEMO_GUIDE.md`: switch points, recording, demo steps, reset
- `CODEX_PROMPTS.txt`, `verify_demo.py`, `demo-code/`
- `demo_reference_storyboard.mp4`: silent reference from the real rehearsal (same demo as v5). **Not the audition recording.**

## What changed in v6
- **One simple idea:** Codex is a brilliant teammate with no memory; AGENTS.md is the note it reads first. No week timeline, no named characters.
- **Codex is introduced** on slide 2 (what it does, where it runs), so reviewers need no background.
- **The ah-ha is visual:** the reviewer's stickers fly into the note and become rules (slide 7), then the demo proves it: same prompt, zero comments (slide 9).
- A quiz moment ("What would your reviewer say?") on slide 4 for engagement.
- 11 slides instead of 15, about 7:30. The demo is unchanged.

## Final fixes
- Emojis now display in Slide Show: each emoji is in its own text run set to the Segoe UI Emoji font. Symbols that need a hidden variation code (✍️ ▶️ ⌨️) were swapped for plain emojis (📝 🧪 💻).
- Outline: the slide-portion time is corrected to 2.1 min and the conclusion to 0.9 min. The "Other portions" note now says 7-8 minutes (it said 5-8).

## Pluralsight guideline check
| Guideline | Status |
|---|---|
| One specific objective | Pass: turn repeated review comments into checkable AGENTS.md rules |
| Reason to care in the first 30 s | Pass: title hook at 0:05; WIIFM on slide 3 at about 0:55 |
| Ah-ha moment | Pass: stickers become the note (slide 7); same prompt, zero comments (demo and slide 9) |
| Story and analogy | Pass: a brilliant teammate with no memory, and a note left where it looks first |
| Live demo with the why narrated | Pass: rehearsed in the Codex app, with "why" lines at each step |
| Callouts, not the cursor | Pass: callouts cued in the script |
| Visuals over text, large fonts | Pass: diagrams on every slide except the summary |
| Concise, 7-8 min | Pass: about 7:30 |
| No assumed background | Pass: slide 2 introduces Codex |

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
