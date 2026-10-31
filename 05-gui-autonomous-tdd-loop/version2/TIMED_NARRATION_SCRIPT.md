# Timed Narration Script — v2

**Topic:** Test Driven Development with OpenAI Codex
**Author:** Akmal Khan · **Level:** Intermediate · **Target:** 7:15 (about 125–135 words per minute)

`[CLICK]` = advance one animation on the slide. `[CALLOUT]` = an on-screen callout added in editing. Bracketed text is not spoken.
The demo narration assumes the expected result. If Codex does something different, say what you actually see (see "If the result differs" at the end).

---

## 0:00–0:25 · Slide 1 — Title

An AI agent can write your pricing code in seconds. But how do you know it charges the customer the right amount?

I'm Akmal Khan. In the next seven minutes, we'll make OpenAI Codex prove its work, with tests written before a single line of implementation.

---

## 0:25–1:00 · Slide 2 — Overview (the problem)

`[CLICK: receipt]` Meet Maliha. She's adding a discount to a bookstore checkout, and here's the bug she's afraid of. A customer spends exactly one hundred dollars and pays one hundred dollars.

`[CLICK: callout]` That customer qualifies. They should pay ninety. The difference is a single character in a comparison.

`[CLICK]` So we'll specify the rule with examples, `[CLICK]` delegate the implementation to Codex, `[CLICK]` and verify the result ourselves. You decide what "correct" means, not the agent.

---

## 1:00–1:30 · Slide 3 — The boundary

`[CLICK]` The rule: one hundred dollars or more gets ten percent off. Ninety-nine ninety-nine stays the same.

`[CLICK: highlight + callout]` Exactly one hundred becomes ninety. This is the row that catches "greater than" when we meant "greater than or equal".

`[CLICK]` One cent above gives ninety dollars and one cent.

`[CLICK: rounding callout]` And one hundred and five cents gives ninety point zero four five, rounding half up to ninety-oh-five. Each example is a decision we make now.

---

## 1:30–2:00 · Slide 4 — The TDD cycle

`[CLICK: RED]` Test-driven development is a loop. In red, we run the tests before the code exists and watch them fail. That matters: a test you never saw fail might not be testing anything.

`[CLICK: GREEN]` In green, we write just enough code to pass.

`[CLICK: REFACTOR + run tests]` In refactor, we improve the code and rerun the same tests, so the behavior can't drift.

`[CLICK: banner]` With an agent in the loop, the tests become our contract with Codex.

---

## 2:00–2:30 · Slide 5 — The prompt contract

`[CLICK: code block]` Here's the prompt we'll give Codex. It has three jobs.

`[CLICK: RULE]` First, the rule: the threshold and the rounding mode.

`[CLICK: SCOPE]` Second, scope: edit only the pricing file and leave the tests alone.

`[CLICK: PROOF + note]` Third, proof: the exact command that checks the work. This is a request, not a lock, so we'll still read the diff.

---

## 2:30–3:00 · Slide 6 — Demo roadmap

Here's our plan in Maliha's project. `[CLICK]` Start red and see the expected errors. `[CLICK]` Hand Codex the contract. `[CLICK]` Review the diff line by line. `[CLICK]` Rerun the same eight tests to green. `[CLICK]` Then decide whether a refactor is worth it, and verify again. Let's open Maliha's project in the Codex app.

> **⏹ SWITCH → DEMO.** Stop the slide recording. Start clip B in the Codex app (see RECORDING_AND_DEMO_GUIDE.md, section 4).

---

## 3:00–3:30 · Demo — Red

**Screen:** Codex app, new thread in the `audition-take` project. Type: *Run python -m unittest -v test_discounts and show me the summary. Do not change any files yet.* Expand "Worked for…" to show the command. `[CALLOUT: "8 errors: expected"]`, then `[CALLOUT: "NotImplementedError"]`.

Here's Maliha's project in the Codex app: a pricing class with a placeholder and eight tests. Before any code exists, I'll ask Codex to run the tests and change nothing. Eight tests, all eight errored, every one from NotImplementedError. They're errors, not failures, because the code doesn't exist yet. That's our red starting point.

---

## 3:30–4:00 · Demo — Read two tests

**Screen:** Open `test_discounts.py` (click the file link in the thread, or Ctrl+J and `Get-Content .\test_discounts.py`). `[CALLOUT: input → expected]` on each test.

Two tests are worth reading. This one passes one hundred dollars and expects ninety. That's Maliha's customer, written as code. This one passes one hundred and five cents and expects ninety dollars and five cents, which is our half-up rounding rule. We use Decimal built from strings, so there are no floating-point surprises.

---

## 4:00–4:45 · Demo — Prompt Codex

**Screen:** Paste the implementation prompt into the composer and send. `[CALLOUT: "SCOPE"]` on *Modify only discount_service.py*, then `[CALLOUT: "PROOF"]` on the test command. While it works, show the "1 file changed" chip. Label the cut `Agent wait shortened`.

I'll paste our contract into the thread: the rule, the rounding mode, the one file it may edit, and the command to run. I've also asked it to stop and explain if a test conflicts with the rule. We don't want it quietly "fixing" an expectation.

While it works, here's what I'll check: one general rule, not special cases for our examples. Codex reports that all eight tests pass and that it changed only the pricing file. That's a claim. Let's verify it.

---

## 4:45–5:10 · Demo — Review the diff

**Screen:** Click **Review** on the "Edited discount_service.py" card. Review tab, **Last Turn**, split diff; widen it with the expand button. `[CALLOUT on >=]`, then `[CALLOUT on ROUND_HALF_UP]`.

The review panel shows one file changed, and `test_discounts.py` isn't in the list, so the tests weren't touched. This line matters most: greater than or equal. That protects Maliha's hundred-dollar customer. The discount applies first, then the total is rounded once to cents, half up.

---

## 5:10–5:30 · Demo — Green

**Screen:** Codex's result card: "all 8 tests passed". Optional: Ctrl+J and run `python -m unittest -v test_discounts` yourself. `[CALLOUT: "8 tests passed"]`

Same command, same eight tests, now all passing, including the boundary and the half cent. The expectations stayed fixed while the code changed around them. That's what makes this green worth trusting.

---

## 5:30–6:10 · Demo — Refactor decision

**Screen:** Paste the refactor prompt in the same thread. Show Codex's answer and the unchanged test run. `[CALLOUT: "No useful refactor"]`, then `[CALLOUT: "Still 8 passing"]`.

Now the refactor step. I'll ask Codex to look for a small readability improvement, and in particular whether the rounding is repeated, while keeping the signature and the tests the same.

Its answer: no useful refactor is needed. The code already works out the amount first and rounds once. It changed nothing and reran the suite: still eight passing. That's a good outcome. Refactoring is optional, and adding complexity just to show an edit would make the code worse. When there is something to improve, the same tests tell you the behavior survived.

---

## 6:10–6:30 · Demo — Wrap the ticket

**Screen:** Business rule beside the green test output. `[CALLOUT: "Covered: threshold, rounding"]`, then `[CALLOUT: "Not yet: negative amounts"]`.

Maliha can close her ticket with evidence: every example in the rule has a passing test. And we know exactly what isn't covered yet. Negative amounts were never part of the contract. Let's step back and sum up.

> **⏹ SWITCH → SLIDES.** Stop the demo recording. Start clip C at slide 7.

---

## 6:30–6:50 · Slide 7 — Your next cycle

`[CLICK]` Here's your practice. An order of minus five dollars arrives. What should it return?

`[CLICK]` Decide the policy. `[CLICK]` Write it as a failing test. `[CLICK]` Then let Codex make it green, and run the whole suite again.

---

## 6:50–7:15 · Slide 8 — Summary

`[CLICK]` Here's what to take back to your team. Examples turn a vague rule into a check anyone can run. `[CLICK]` A tight scope keeps the agent's diff small enough to review. `[CLICK]` Rerunning the same tests is what makes a refactor safe. `[CLICK]` And a green suite proves what you tested, nothing more. That's why you choose the examples. You now have a workflow you can apply to your next Python feature. Thanks for watching.

---

## If the result differs

- **Codex's first version rounds in two places.** Then the refactor is real. Show the diff with a "Round once" callout, then the rerun: "Rounding now happens in exactly one place, and the same eight tests still pass."
- **The first attempt fails a test:** "One test still fails. Let's compare the actual value with our rule," then show the real diagnosis and rerun. Do not stage a mistake.
- **Codex edits the test file:** the review panel will list `test_discounts.py`. Say so, use **Undo** or revert that file, restate the scope and rerun. This is strong material, so keep it.

## Delivery notes

- Pause for about one second after each `[CLICK]`, so the slide changes before you speak.
- Keep the mouse still. Use callouts for pointing.
- Record a timed rehearsal. If you run over, shorten the waiting time, not the explanations.
