# Slide deck content

Use the supplied Pluralsight audition template. Delete helper slides and replace all sample copy. Use the eight-slide sequence below; the editor recording follows slide 6. Preserve the original template branding and source layouts.

## Slide 1 Test Driven Development with OpenAI Codex

Time: 0:00-0:25. Source template slide: 2.

- Dr. Akmal Khan
- Assistant Professor of Data Science & AI Engineer

Production: Use the supplied author's title. Remove the template's stock headshot; do not invent a portrait.

## Slide 2 Overview

Time: 0:25-1:00. Source template slide: 3.

- A $100 order should cost $90
- Examples define the expected behavior
- Codex implements within a clear scope
- You review the changes and verify the result

Production: Reveal one point at a time; emphasize the $100 example after 20 seconds.

## Slide 3 The discount boundary

Time: 1:00-1:30. Source template slide: 6.

- Order amount / Final total
- $99.99 / $99.99
- $100.00 / $90.00
- $100.01 / $90.01
- At $100 or more / 10% off

Production: Use the template comparison layout. Reveal rows as each example is explained.

## Slide 4 The TDD cycle

Time: 1:30-2:00. Source template slide: 4.

- Red: observe the expected failure
- Green: implement the required behavior
- Refactor: improve structure
- Rerun the same tests

Production: Use the template two-column text layout. Emphasize phases in sequence.

## Slide 5 The prompt contract

Time: 2:00-2:30. Source template slide: 4.

- Business rule and boundary examples
- Editable file: discount_service.py
- Existing tests remain unchanged
- Verification: run the supplied test command

Production: Duplicate the two-column layout. Include exact command in notes: python -m unittest -v test_discounts. Instructions are not filesystem enforcement.

## Slide 6 Demo

Time: 2:30-3:00. Source template slide: 8.

- Expected errors before implementation
- Threshold and rounding review
- Unchanged tests, executed again
- A small refactor with verification

Production: Then switch to the real editor for the 3:00-6:30 demo. Use callouts, not cursor pointing.

## Slide 7 Summary

Time: 6:30-6:55. Source template slide: 9.

- Boundary examples make requirements reviewable
- Scoped changes simplify code review
- Unchanged tests check behavior after refactoring
- Passing tests support the cases they cover

Production: Conceptual summary; do not say complete correctness or exhaustive coverage.

## Slide 8 Your next TDD cycle

Time: 6:55-7:15. Source template slide: 4.

- What should happen for a negative amount?
- Decide the behavior
- Write the expectation as a test
- Implement and verify it

Production: Duplicate the source content layout. Pause before showing the practice action.

## Animation and narration

Reveal one bullet or example at a time. The supplied overview, demo and summary layouts contain example animations; verify the finished slideshow in PowerPoint before recording. Match reveals to the timed script. Visual changes should occur every 20-30 seconds.

Do not retain the stock headshot. Use the author information already present in the supplied Guardrails deck. Use authentic screen recordings for the demo, not mock screenshots.
