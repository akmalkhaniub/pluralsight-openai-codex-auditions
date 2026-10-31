# AGENTS.md audition, v7 (slides and outline first)

## What changed from v6
- New example: a login rate limiter (5 failed attempts locks the email for 15 minutes), replacing the coupon.
- Plain-English review comments that need no background: limits belong in config.py; don't reveal if an email exists; log lockouts with audit_log(). AppError/ValueError are gone.
- Slide 4: numbered red boxes on the problem lines, matched to numbered review comments. No arrows.
- Slides 5-10, the script and the outline are updated to match. "In the next seven minutes" is cut.

## Not done yet
- The demo for this example is NOT rehearsed. A first test showed Codex may copy repo habits (it used config.py without the note), so the demo claims on slide 9 must be checked in a real run before recording.
- Demo guide, prompts and verify script still describe the coupon demo (see version6). They'll be updated after the rehearsal.
- Demo repo: login-take; the note to copy in: login-kit/AGENTS.md.
