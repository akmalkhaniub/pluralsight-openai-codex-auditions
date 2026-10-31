# Test Driven Development with OpenAI Codex

## Author

Dr. Akmal Khan

## Level

Intermediate

## Notes

Target 7:15: overview 1:00, concepts 2:00, demo 3:30, conclusion 0:45. Python and Codex in VS Code. One prepared red-green-refactor cycle with eight focused tests.

## Prerequisites

Read basic Python, understand a unit-test assertion, and run Python commands in a terminal. Basic VS Code familiarity. Codex is installed and signed in before recording.

## Story

Priya is adding a discount rule to a bookstore checkout. Orders of $100 or more receive 10% off. An order of exactly $100 must cost $90, so a boundary mistake would charge too much. Priya defines examples before implementation, asks Codex to complete only the pricing function, reviews the diff, and runs the tests. She then requests a small refactor and checks that the same tests still pass.

## Description

In this audition you will learn to guide OpenAI Codex through a test-driven development cycle for a small Python feature. When you finish, you will be able to translate a business rule into boundary examples, constrain an implementation prompt, review generated changes, and verify that a refactor preserves the tested behavior.

## Concepts

Slide portion
1:00-1:30: Explain Priya's pricing rule using $99.99, $100 and $100.01 examples.
1:30-2:00: Explain red, green and refactor, including why each phase needs test execution.
2:00-2:30: Show the prompt contract: business rule, editable file, unchanged tests and verification command.
2:30-3:00: Explain diff review and the limits of a passing suite. Transition to the demo.
Use the audition template, short text, and visual changes every 20-30 seconds.

## Demo

Demo
3:00-3:30: Run eight tests against the placeholder. Explain the expected NotImplementedError.
3:30-4:00: Inspect the $100 boundary assertion and the rounding example. State the expected totals.
4:00-4:45: Ask Codex to implement discount_service.py without changing tests. Review the actual result.
4:45-5:30: Inspect threshold and rounding logic, confirm unchanged tests, then run the suite to green.
5:30-6:10: Request a small readability refactor that preserves behavior. Review the diff and rerun the same suite.
6:10-6:30: Connect the result to Priya's ticket and identify one untested input policy.
Use a clean editor, readable code, and callouts. Shorten actual wait time transparently.

## Other

Other Portions (optional)
No additional section. Keep the finished video within the rubric's 5-8 minute range.

## Conclusion

Conclusion
6:30-7:15: Explain why boundary examples make the requirement reviewable and why rerunning unchanged tests supports confidence after refactoring. Passing tests provide evidence for covered cases. Practice: specify and test the policy for negative order amounts before changing the implementation.