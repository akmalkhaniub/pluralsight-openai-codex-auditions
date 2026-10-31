# Audition: Who Reviews the AI? Code Review with OpenAI Codex (v2)

## Files
- `Audition Outline - Akmal Khan - Code Review v2.docx`: from the blank Author Kit template, in bullets
- `Audition Slides - Akmal Khan - Code Review v2.pptx` + `Audition Slides - preview.pdf`: 11 slides, animations, speaker notes
- `TIMED_NARRATION_SCRIPT.md`: about 7:35, click, callout and switch cues
- `SLIDE_DECK_CONTENT.md`: per-slide visuals and build order
- `RECORDING_AND_DEMO_GUIDE.md`: switch points, recording, demo steps, which finding to use, reset
- `CODEX_PROMPTS.txt`: the exact prompt, review steps, comment and follow-up message
- Demo project: `photo-take` in the project root (clean Git repo, tests pass)

## Pluralsight guideline check
| Guideline | Status |
|---|---|
| One specific objective | Pass: /review on Last turn, act on the finding that matters, small fix |
| Reason to care early | Pass: title hook at 0:05; bottleneck and WIIFM by 1:00 |
| Ah-ha moment | Pass: the same Codex that wrote passing code finds a real risk in it |
| Story and analogy | Pass: the writer and the editor |
| Live demo, why narrated | Pass: every step has a "why" line |
| Callouts, not the cursor | Pass: callouts cued in the script |
| Visuals over text | Pass: diagrams on every slide except the summary |
| Concise, 7–8 min | Pass: about 7:35 |
| No assumed background | Pass: slide 2 introduces Codex |

## What changed in v2 (after a real run in your Codex app)
- `/review` offers "Review uncommitted changes" or "Review against a base branch" (Last Turn is a Review pane scope, not a /review option). Slides 6, 8, 11 and the script now match.
- The real finding replaces the guessed one: a disk-full failure leaves a half-saved file (P2), with all 9 tests passing. Slides 4, 7, 9 and 10, the script and the outline now use it.
- New: `demo_codex_review.mp4`, a silent 2:52 demo video from real screenshots with callouts, ready for your voice-over.

## Rehearsal results (28 Sep 2026)
| Step | Result | Codex time |
|---|---|---|
| Build the upload | 2 files, 9 tests pass | 9.5 min |
| /review (uncommitted) | 1 issue, P2: half-saved file on disk-full | 2.5 min |
| Inline comment + minimal fix | +6 −6 fix, regression test, 10 tests pass | 3 min |
| /review again | No actionable issues | 1.5 min |

## Not verified
- Animations were previewed in LibreOffice only. Check them in PowerPoint (for the web is best).
