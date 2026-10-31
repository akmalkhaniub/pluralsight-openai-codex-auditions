# Timed narration script

Topic: Test Driven Development with OpenAI Codex

Author: Dr. Akmal Khan. Target: 7:15. This is a rehearsal target, not measured recording duration.
Read conversationally in your own voice. Bracketed directions are production cues, not spoken text.
Adapt result-dependent sentences to the actual recording. The supplied green/refactored checkpoints are rehearsal examples, not recorded agent output.

## 0:00-0:25 Slide 1

**Visual:** Title slide. Brief pause after your name. At 0:20, prepare the overview transition.

Hello, I'm Dr. Akmal Khan. In this lesson, we'll use OpenAI Codex to implement a small Python feature through a test-driven development cycle. We'll start with examples of the required behavior, review the generated implementation, and check that a later refactor preserves those examples.

## 0:25-1:00 Slide 2

**Visual:** Overview. Reveal the customer requirement, then the reviewable result. At 0:45, emphasize $100 costs $90.

Priya is adding a discount to a bookstore checkout. A customer spending exactly one hundred dollars should pay ninety. A small boundary mistake could charge that customer too much. Our goal is to turn this requirement into something we can check, even when an agent writes the implementation. By the end, you'll know how to specify the behavior, inspect the changes, and verify the result yourself.

## 1:00-1:30 Slide 3

**Visual:** Comparison layout. Reveal each amount and final total in sequence. Keep the pointer still.

Here is the rule: orders of one hundred dollars or more receive ten percent off. Below the threshold, the amount stays unchanged. Notice these three examples: ninety-nine ninety-nine, exactly one hundred, and one hundred and one cent. They sit just below, at, and just above the boundary. These examples help distinguish greater than from greater than or equal to. We'll also state how to round the final total.

## 1:30-2:00 Slide 4

**Visual:** Explain red, green and refactor in sequence; emphasize the phase being discussed.

Test-driven development gives us a repeatable cycle. In red, we run a test before the feature exists and confirm the expected failure. In green, we add enough implementation to satisfy the behavior. In refactor, we improve the code's structure while keeping its behavior. We then rerun the tests. I've prepared a small set of examples for this demonstration so we can focus on guiding and reviewing Codex.

## 2:00-2:30 Slide 5

**Visual:** Prompt contract on a template content slide. Highlight the allowed file, then the test command.

The prompt needs the business rule and a clear scope. We'll allow changes to discount_service.py and ask Codex to leave the tests unchanged. We'll also supply the exact command that verifies the work. That request guides the agent; it does not lock the test file. We still inspect the changed files. If a test conflicts with the requirement, the right next step is to discuss the conflict, rather than quietly changing the expected result.

## 2:30-3:00 Slide 6

**Visual:** Demo transition. Reveal expected error, code review and verified result. At 2:50, transition to the editor.

During review, we'll check the threshold comparison and the rounding operation, then confirm that the test file stayed unchanged. A green suite gives evidence for the cases we wrote. It cannot prove that every possible input works. This lesson assumes valid, nonnegative decimal amounts. Let's open Priya's project and work through the cycle, using the actual code and test output to decide whether we're ready to move on.

## 3:00-3:30 Live demo

**Visual:** Run python -m unittest -v test_discounts. Callout on NotImplementedError, then the eight-error summary. Capture test hash in a prepared terminal command.

The project contains a pricing class and eight focused tests. I'll run the suite before asking Codex to implement anything. Each test reaches the placeholder, which raises NotImplementedError. These are expected errors from missing implementation, so we have our red starting point. If the runner instead reported an import problem, we would fix the setup first. I'm also recording the test file's hash so we can check later that its contents stayed unchanged.

## 3:30-4:00 Live demo

**Visual:** Show test_exactly_at_threshold, then test_half_cent_rounds_up. Callout on the input and expected value for each.

Let's inspect two examples. The boundary test passes one hundred dollars and expects ninety. That is the customer's requirement in executable form. The rounding example expects ninety dollars and five cents from an order of one hundred dollars and five cents. The unrounded total is ninety point zero four five. Our stated rule rounds that half cent upward. We use Decimal values created from strings so the example has explicit decimal arithmetic.

## 4:00-4:45 Live demo

**Visual:** Paste implementation prompt. Callout on only discount_service.py and the verification command. Show actual agent actions. Label any edited waiting interval 'Agent wait shortened'.

Now I'll give Codex the specification and tests, and ask it to implement only the pricing file. Notice that the prompt includes the inclusive threshold, the rounding rule, and the verification command. I'm asking for an explanation if the requirements conflict. While Codex works, our review criteria are already clear. We are looking for a general implementation of the rule, not special cases that happen to match our examples. Once the result arrives, we'll inspect what actually changed.

## 4:45-5:10 Live demo

**Visual:** Open actual implementation diff. Callout on >= and ROUND_HALF_UP. Verify test hash. If agent output differs, adapt narration to it.

Here is the implementation. Check that the comparison includes an order of exactly one hundred dollars. Then check that the ten percent discount applies before the final rounding operation. I also want to see Decimal arithmetic throughout this small calculation. The modified-file view and our hash check let us confirm that the tests remain unchanged. If Codex changed an assertion, we would investigate that before accepting this result.

## 5:10-5:30 Live demo

**Visual:** Run the same test command locally; show actual eight-test OK summary. Callout on the boundary test result.

I'll run the same command again. The eight examples now pass, including the threshold and half-cent cases. That gives us a green implementation for this contract. The result is useful because we kept the expected behavior stable while changing the implementation.

## 5:30-6:10 Live demo

**Visual:** Send refactor prompt. Show a genuine readability improvement, then rerun the same tests and verify the hash. Change callout after 20 seconds.

Now we consider refactoring. If both branches repeat the rounding operation, we can calculate the multiplier first and round once. I'll ask Codex for that small improvement without changing the public method or the tests. We review the resulting diff and rerun the same suite. If the implementation is already this simple, there may be no worthwhile change to make. Refactoring should improve the code, so we don't add complexity just to demonstrate another edit.

## 6:10-6:30 Live demo

**Visual:** Show the verified result beside the business rule. Callout 'Covered: threshold and rounding' and 'Next: invalid-input policy'.

Priya can now connect the implementation to concrete acceptance examples. The tests still pass after our review of the refactor. Negative amounts remain outside the input contract we chose. Before supporting those, we would decide the intended behavior and add an example that captures it.

## 6:30-6:55 Slide 7

**Visual:** Summary slide. Reveal the practical meaning of boundary examples and unchanged tests.

The useful habit is to make behavior explicit before delegating implementation. Boundary examples explain what the customer should receive. A scoped prompt tells Codex where to work, and reviewing the diff lets you assess the result. Running the same tests after a refactor helps you check that the covered behavior remains intact.

## 6:55-7:15 Slide 8

**Visual:** Practice slide. Reveal the question, pause, then the next action. End cleanly.

For practice, decide what should happen when an order amount is negative. Write that expectation as a test before changing the implementation, and repeat the cycle. You now have a small workflow you can apply to your next Python feature. Thank you for watching.

## Alternate delivery when the first result needs correction

Say: 'This test still fails. Let's compare the actual value with our stated requirement, then ask Codex to correct the implementation.' Show the genuine diagnosis and rerun. Do not script or manufacture a mistake.

If no refactor is needed, explain the decision. If teaching the concrete rounding extraction from the rehearsal version, explicitly label it 'Prepared refactoring example'; show before and after and execute the tests.

## Pacing check

Record a timed rehearsal. Leave room for reading assertions and seeing results. Keep the overview at 60 seconds and the demo at least 3 minutes. Shorten agent waiting time transparently rather than rushing explanations. The finished audition must remain 5-8 minutes.
