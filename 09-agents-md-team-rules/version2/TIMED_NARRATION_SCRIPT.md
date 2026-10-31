# Timed Narration Script: Team Rules for OpenAI Codex with AGENTS.md

**Author:** Akmal Khan · **Level:** Intermediate · **Target:** 7:15 (about 125–140 words per minute on slides)

`[CLICK]` = advance one slide animation. `[CALLOUT]` = on-screen callout added in video editing. Bracketed text is not spoken.
The demo lines describe what happened in a real practice run. If your run differs, say what you actually see.

---

## 0:00–0:25 · Slide 1 — Title

If you've ever typed the same code review comment three times in one week, this one's for you.

I'm Akmal Khan. In the next seven minutes, we'll write our team's rules down once, in AGENTS.md, and watch Codex follow them on the very next task.

---

## 0:25–1:00 · Slide 2 — Overview (the problem and WIIFM)

`[CLICK]` Here's a pull request Codex wrote for Maliha's bookshop. It works. `[CLICK: ring + comment]` But the team uses AppError codes, not ValueError. And the changelog wasn't touched. Maliha has typed that review comment many times.

`[CLICK]` So we'll write the rules once, `[CLICK]` in a file Codex reads before every task, `[CLICK: WIIFM]` and here's what's in it for you: Codex pull requests that already follow your team's rules, and no more repeat review comments.

---

## 1:00–1:30 · Slide 3 — Rules Codex can follow, and you can check

The whole trick is how you write the rules. `[CLICK]` "Handle errors properly" means nothing to anyone. "Raise AppError with an upper-case code" is something you can see in a diff. `[CLICK]` Same for docs: an Example line, not "document your code". `[CLICK]` Same for tests: the exact command. `[CLICK]` Same for the changelog. `[CLICK: tag]` One test for every rule: could a reviewer check it in the diff?

---

## 1:30–2:00 · Slide 4 — AGENTS.md is an onboarding note

`[CLICK]` Think of AGENTS.md as the onboarding note you'd give a new teammate. A person reads it on day one and forgets half of it by Friday. `[CLICK]` Codex reads it every time a task starts, and never forgets.

`[CLICK]` Put it at the repo root, in Git. `[CLICK]` Edited it? Start a new thread. `[CLICK: banner]` And write it for a smart new hire.

---

## 2:00–2:30 · Slide 5 — Maliha's AGENTS.md

`[CLICK]` Here's the file we'll use. `[CLICK: CODE]` How we write code: Decimal for money, AppError with an upper-case code for bad input, and an example in every docstring.

`[CLICK: TESTS]` How we prove it: tests in the matching test file, and the exact command to run before finishing.

`[CLICK: HOUSEKEEPING]` What else changes: one changelog line, no new dependencies. Notice every rule is something you can check in a diff. "Write clean code" would do nothing.

---

## 2:30–3:00 · Slide 6 — Demo roadmap

Here's the plan. `[CLICK]` Give Codex a task with no rules file. `[CLICK]` Review it against the team's rules. `[CLICK]` Add AGENTS.md. `[CLICK]` Reset and run the exact same prompt. `[CLICK]` Then compare the two diffs. Let's open Maliha's repo in the Codex app.

> **⏹ SWITCH → DEMO.** Stop the slide recording. Start clip B in the Codex app (see RECORDING_AND_DEMO_GUIDE.md, section 4).

---

## 3:00–3:45 · Demo — Without rules

**Screen:** New thread in **agents-take**. Paste the task prompt and send. Cut the wait. `[CALLOUT: "Same prompt both times"]` on the prompt.

This is Maliha's pricing service: an order total function, one test, and a changelog. There's no AGENTS.md yet. I'll ask Codex to add a coupon function: SAVE10 takes ten percent off, and unknown codes are invalid.

---

## 3:45–4:15 · Demo — Spot the gaps

**Screen:** Result card → **Review** → expand. Ring each gap: `[CALLOUT: "ValueError, not AppError"]`, `[CALLOUT: "No Example: line"]`, `[CALLOUT: "2 files: no CHANGELOG.md"]`.

The code is reasonable, and Codex even added tests on its own. But hold it against the team's rules. The unknown coupon raises ValueError, not AppError. The docstring has no example. And only two files changed, so the changelog was never touched. Codex didn't do anything wrong. It simply didn't know our rules.

---

## 4:15–4:40 · Demo — Add AGENTS.md

**Screen:** **Undo** the change. Terminal (Ctrl+J): `Copy-Item ..\agents-kit\AGENTS.md .`. Show the file. `[CALLOUT: "Repo root"]`

I'll undo that change and add the rules file from the slides at the root of the repo. That's all the setup there is.

---

## 4:40–5:05 · Demo — Same task again

**Screen:** New thread (rules are read when a task starts). Paste the same prompt. Cut the wait.

New thread, because Codex reads AGENTS.md when a task starts. Same prompt, word for word.

---

## 5:05–6:05 · Demo — Compare the diff

**Screen:** Review → expand. `[CALLOUT: "AppError('INVALID_COUPON')"]`, `[CALLOUT: "Docstring Example:"]`, `[CALLOUT: "Tests added"]`, `[CALLOUT: "CHANGELOG.md updated"]`. Show Codex's message about running the test command.

Now look at the difference. Three files changed this time. The invalid coupon raises AppError with an upper-case code, INVALID_COUPON. The docstring has an example line. Codex ran the exact test command from our rules, and there's CHANGELOG.md, with one line under Unreleased.

**(Ah-ha)** Same model, same prompt. The only thing we changed is one Markdown file in the repo.

---

## 6:05–6:30 · Demo — Close

**Screen:** AGENTS.md beside the changed-files list. `[CALLOUT: "Commit AGENTS.md"]`

Maliha commits AGENTS.md, and every teammate and every new thread gets the same rules. Review can now focus on the logic. Let's step back and sum up.

> **⏹ SWITCH → SLIDES.** Stop the demo recording. Start clip C at slide 7.

---

## 6:30–6:50 · Slide 7 — Your first AGENTS.md

`[CLICK]` Here's your practice. What do you correct in every code review? Those are your first three rules.

`[CLICK]` List them, `[CLICK]` make each one checkable, `[CLICK]` and rerun a real task to see the difference.

---

## 6:50–7:15 · Slide 8 — Summary

`[CLICK]` So, what can you do now that you couldn't before? Write your rules once, in the repo, where everyone gets them. `[CLICK]` Make every rule checkable, because that's what changes the diff. `[CLICK]` Codex rereads them at the start of every task, like an onboarding note it never forgets. `[CLICK]` And keep reviewing: rules guide Codex, but review is still how you check the result. You now have a workflow you can use on your very next task. Thanks for watching.

---

## If the result differs

- **The first run (no rules) already follows a rule**, such as adding tests: say so honestly. "Codex added tests on its own, but it still raised ValueError and skipped the changelog." Point at whatever differs.
- **The second run misses a rule:** show it, and tighten the wording in AGENTS.md (for example, "Always add a line to CHANGELOG.md"), then run again in a new thread. Real iteration is good teaching.
- **The rules don't seem to apply:** check that you started a new thread after adding the file, and that AGENTS.md is at the repo root.

## Delivery notes

- Pause for about one second after each `[CLICK]`.
- Keep the mouse still. Use callouts for pointing.
- Each Codex request took several minutes in practice. Record everything and cut the waits, labelling each cut "Agent wait shortened".
