# Timed Narration Script: Team Rules for OpenAI Codex with AGENTS.md

**Author:** Akmal Khan · **Level:** Intermediate · **Target:** 7:15 (about 125–140 words per minute on slides)

`[CLICK]` = advance one slide animation. `[CALLOUT]` = on-screen callout added in video editing. Bracketed text is not spoken.
The demo lines describe what happened in a real practice run. If your run differs, say what you actually see.

---

## 0:00–0:25 · Slide 1 — Title

If you've ever typed the same code review comment three times in one week, this one's for you.

I'm Akmal Khan. In the next seven minutes, we'll write our team's rules down once, in AGENTS.md, and watch Codex follow them on the very next task.

---

## 0:25–1:00 · Slide 2 — Overview (problem, WIIFM, agenda)

`[CLICK]` Here's a pull request Codex wrote for Maliha's bookshop. It works. `[CLICK: ring + comment]` But her team uses AppError, not ValueError, and the changelog wasn't touched. Maliha has typed that comment five times this month.

`[CLICK: WIIFM]` So here's what's in it for you: Codex pull requests that already follow your team's rules.

`[CLICK: agenda]` We'll get there in three steps: meet AGENTS.md, write rules you can check, and prove it in a demo.

---

## 1:00–1:30 · Slide 3 — Step 1: Meet AGENTS.md

`[CLICK]` AGENTS.md is a plain Markdown file. `[CLICK]` It sits at the root of your repo, in Git, so the whole team shares it.

`[CLICK]` When a task starts, `[CLICK]` Codex reads AGENTS.md first, `[CLICK]` and only then your prompt.

`[CLICK: analogy]` Think of it as the onboarding note you'd give a new teammate. Except this teammate rereads it before every single task. `[CLICK]` One tip: if you change the file, start a new thread.

---

## 1:30–2:00 · Slide 4 — Step 2: Write rules you can check

So what goes in the note? `[CLICK]` "Handle errors properly" sounds fine, but nobody can check it. "Raise AppError with an upper-case code" is something you can see in a diff. `[CLICK]` "Test your changes" becomes the exact command to run. `[CLICK]` "Keep docs updated" becomes one changelog line. `[CLICK: banner]` The test for every rule: could a reviewer check it in the diff?

---

## 2:00–2:30 · Slide 5 — From Maliha's comments to rules

Now let's write Maliha's file. The best source of rules is your own review history. `[CLICK]` "Use AppError, not ValueError" becomes a rule. `[CLICK]` "Where are the tests?" becomes the exact test command. `[CLICK]` "Update the changelog" becomes a housekeeping rule. `[CLICK]` Plus two more: an example in every docstring, and no new dependencies. Five rules, all checkable.

---

## 2:30–3:00 · Slide 6 — Step 3: Prove it

Now step three: proof. `[CLICK]` First, we ask Codex for a coupon function with no rules file. `[CLICK]` We check the diff against Maliha's comments. `[CLICK]` Then we add AGENTS.md, `[CLICK]` and send the exact same prompt in a new thread. `[CLICK]` Finally, we compare. Let's open Maliha's repo in the Codex app.

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
