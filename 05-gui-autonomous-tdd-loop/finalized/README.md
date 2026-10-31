# Test Driven Development with OpenAI Codex

Final audition topic for Dr. Akmal Khan. Target duration: 7 minutes 15 seconds.

Start with the completed DOCX outline in this folder. It follows the supplied Pluralsight form.
The kit timeline places outline approval before recording. Submit this outline to your Author Evangelist before producing the final video.

## Final scope

Use a bookstore checkout to teach one prepared red-green-refactor cycle.
Orders of $100 or more receive 10% off. Teach boundary examples, a scoped implementation prompt, human diff review, and verification after a small refactor.
The input contract is nonnegative Decimal amounts in cents. Round the final total with ROUND_HALF_UP.
Coupon stacking and the second discount tier are removed to keep the audition focused.

## Files

- Audition Outline - Dr Akmal Khan - TDD.docx: completed official form.
- Audition Slides - Dr Akmal Khan - TDD.pptx: eight slides using the official template, speaker notes and on-click reveals.
- TIMED_NARRATION_SCRIPT.md: spoken script, visual cues and timing.
- SLIDE_DECK_CONTENT.md: exact slide content and template layout plan.
- CODEX_PROMPTS.txt: implementation and refactor prompts.
- demo-code: deliberately incomplete starting project.
- rehearsal/red, rehearsal/green, rehearsal/refactored: separate, deterministic rehearsal checkpoints.
- KIT_REVIEW.md: supplied kit requirements and corrections to the previous plan.
- verify_demo.py: checks starting failures and both completed reference implementations.

## Rehearsal setup

Open only demo-code as the VS Code workspace, so the answer checkpoints stay outside the agent's working folder.
Use Python 3.10 or later and sign into the Codex IDE extension before recording.
The demo uses Python's built-in unittest runner, so no package installation is needed. Tests are also compatible with pytest.
Run this command from demo-code:

    python -m unittest -v test_discounts

The initial result must be eight errors caused by NotImplementedError. Explain that these are expected errors, not assertion failures or a broken test runner.
Use a disposable copy for every rehearsal; keep the original starting files intact.

Capture a hash before invoking Codex in PowerShell:

    $testHashBefore = (Get-FileHash ./test_discounts.py -Algorithm SHA256).Hash

After implementation and again after refactoring:

    if ((Get-FileHash ./test_discounts.py -Algorithm SHA256).Hash -ne $testHashBefore) { throw "Tests changed" }
    python -m unittest -v test_discounts

Review all modified files in the editor or Git diff. Passing the hash check proves the file is unchanged, not that the implementation is correct.
The command and its actual test output provide the behavioral evidence.

## Recording plan

Overview 0:00-1:00; concepts 1:00-3:00; demo 3:00-6:30; conclusion 6:30-7:15.
Use the official audition slide template. Change slides, reveals or focused callouts every 20-30 seconds.
Narrate in your own voice, with clear pauses and an audio track separate from the screen recording.
Keep code and results readable at the final playback size. Use callouts instead of pointing with the cursor.
Record real Codex interactions and actual test output. Label time compression of agent waits.
If the implementation is already simple, explain that no useful refactor is needed, or use the clearly identified rehearsal checkpoint to teach a real refactor. Never present prepared reference code as a live agent response.
Do not promise a predictable first response or manufacture an agent mistake.

## Scope and status

The earlier MP4, PPTX, audio, teleprompter and generation scripts in the parent folder are previous drafts. They are not synchronized to this finalized lesson.
This folder is the source of truth for the new audition. No submission, email, or upload has been performed.
