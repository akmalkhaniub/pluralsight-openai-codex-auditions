# Timed Narration Script: Team Rules for OpenAI Codex with AGENTS.md (v5, story version)

**Author:** Akmal Khan · **Level:** Intermediate · **Target:** about 8:00

**Story:** Monday, tech lead Maliha onboards a new developer, Sam, in 20 minutes. Tuesday, Codex joins the team and nobody onboards it: three review rounds per PR, on every task. Wednesday, the same comments on every task. Thursday, the team writes the onboarding note as AGENTS.md. Friday: one review, zero ping-pong.

`[CLICK]` = advance one slide animation. `[CALLOUT]` = on-screen callout added in video editing. Bracketed text is not spoken.

---

## 0:00–0:20 · Slide 1 — Title

If you've ever typed the same code review comment three times in one week, this story is for you.

I'm Akmal Khan, and this is the story of how one small Markdown file stopped that.

---

## 0:20–0:50 · Slide 2 — Overview (hook, WIIFM, the week ahead)

`[CLICK]` What if your newest teammate forgot everything, every task? `[CLICK]` That's how Codex starts work, unless you give it a note.

`[CLICK: WIIFM]` Here's what's in it for you: Codex pull requests that follow your team's rules the first time.

`[CLICK: week]` We'll follow one team for one week: a new hire on Monday, review ping-pong on Tuesday and Wednesday, a note on Thursday, and the proof on Friday.

---

## 0:50–1:10 · Slide 3 — Monday: Sam joins the team

`[CLICK]` Monday. Maliha, the tech lead, welcomes Sam, a new developer. `[CLICK]` She walks him through the team notes. `[CLICK]` Bad input raises AppError with a code. `[CLICK]` Test with the team's command. `[CLICK]` Add a line to the changelog. `[CLICK]` Twenty minutes, and Sam remembers it all week.

---

## 1:10–1:20 · Slide 4 — Tuesday: Codex joins

Tuesday, the team starts using Codex. It's fast, it's smart, and it writes good code. But nobody gives it the notes Sam got.

---

## 1:20–1:40 · Slide 5 — Tuesday: the review ping-pong

`[CLICK]` Codex opens its first pull request: a coupon function. `[CLICK]` Maliha reviews it: use AppError, not ValueError. `[CLICK]` Fixed. Then: where are the tests? `[CLICK]` Added. Then: the changelog line? `[CLICK]` Three rounds for one small pull request. `[CLICK]`

---

## 1:40–1:55 · Slide 6 — Wednesday: new tasks, same three comments

Wednesday brings new tasks. `[CLICK]` Gift cards: the same three comments. `[CLICK]` Refunds: the same again. `[CLICK]` Shipping, wishlists: every time. `[CLICK: banner]` Sam learned once. For Codex, every task is day one.

---

## 1:55–2:05 · Slide 7 — Thursday: the realisation

By Thursday morning, Maliha sees the real problem. Codex isn't bad at the team's rules. It has never read them.

---

## 2:05–2:20 · Slide 8 — Definition: AGENTS.md

So Codex needs what Sam got on Monday: an onboarding note. That's AGENTS.md. A Markdown file in your repo that Codex reads before every task. The onboarding note for a teammate who starts fresh each time.

---

## 2:20–2:40 · Slide 9 — Thursday: where the note goes

`[CLICK]` The note goes at the root of the repo, `[CLICK]` committed in Git, so the whole team shares one version. `[CLICK]` When a task starts, `[CLICK]` Codex reads AGENTS.md first, `[CLICK]` and then your prompt. `[CLICK]` Read once at the start, so if you change it, start a new thread.

---

## 2:40–3:05 · Slide 10 — Thursday: rewrite Sam's notes for Codex

But Sam's notes can't be pasted in as they are. `[CLICK]` "Handle errors properly" works for a person. For Codex, write the exact rule: raise AppError with an upper-case code. `[CLICK]` "Remember to test" becomes the exact command. `[CLICK]` "Keep docs updated" becomes one changelog line. `[CLICK: banner]` The test for every rule: could a reviewer check it in the diff?

---

## 3:05–3:25 · Slide 11 — Thursday: the team's AGENTS.md

`[CLICK]` Here's the finished note: about ten lines of plain Markdown. `[CLICK]` Tuesday's first review comment is now this rule. `[CLICK]` The second is the test command. `[CLICK]` The third is the changelog rule. `[CLICK]` Every comment the team was tired of typing is now written down, once.

---

## 3:25–3:40 · Slide 12 — Friday: rerun Tuesday's task

Friday: does it work? We rerun Tuesday's task. `[CLICK]` First with no note. `[CLICK]` Do the same comments come back? `[CLICK]` Then add AGENTS.md, `[CLICK]` and send the same prompt in a new thread. `[CLICK]` Compare. Let's open the repo.

> **⏹ SWITCH → DEMO.** Stop the slide recording. Start clip B in the Codex app (see RECORDING_AND_DEMO_GUIDE.md, section 4).

---

## 3:40–4:25 · Demo — Without rules

**Screen:** New thread in **agents-take**. Paste the task prompt and send. Cut the wait. `[CALLOUT: "Same prompt both times"]` on the prompt.

This is the team's pricing service: an order total function, one test, and a changelog. There's no AGENTS.md yet. I'll ask Codex to add a coupon function: SAVE10 takes ten percent off, and unknown codes are invalid.

---

## 4:25–4:55 · Demo — Spot the gaps

**Screen:** Result card → **Review** → expand. Ring each gap: `[CALLOUT: "ValueError, not AppError"]`, `[CALLOUT: "No Example: line"]`, `[CALLOUT: "2 files: no CHANGELOG.md"]`.

The code is reasonable, and Codex even added tests on its own. But hold it against the team's rules. The unknown coupon raises ValueError, not AppError. The docstring has no example. And only two files changed, so the changelog was never touched. Codex didn't do anything wrong. It simply didn't know our rules.

---

## 4:55–5:20 · Demo — Add AGENTS.md

**Screen:** **Undo** the change. Terminal (Ctrl+J): `Copy-Item ..\agents-kit\AGENTS.md .`. Show the file. `[CALLOUT: "Repo root"]`

I'll undo that change and add the rules file from the slides at the root of the repo. That's all the setup there is.

---

## 5:20–5:45 · Demo — Same task again

**Screen:** New thread (rules are read when a task starts). Paste the same prompt. Cut the wait.

New thread, because Codex reads AGENTS.md when a task starts. Same prompt, word for word.

---

## 5:45–6:45 · Demo — Compare the diff

**Screen:** Review → expand. `[CALLOUT: "AppError('INVALID_COUPON')"]`, `[CALLOUT: "Docstring Example:"]`, `[CALLOUT: "Tests added"]`, `[CALLOUT: "CHANGELOG.md updated"]`. Show Codex's message about running the test command.

Now look at the difference. Three files changed this time. The invalid coupon raises AppError with an upper-case code, INVALID_COUPON. The docstring has an example line. Codex ran the exact test command from our rules, and there's CHANGELOG.md, with one line under Unreleased.

**(Ah-ha)** Same model, same prompt. The only thing we changed is one Markdown file in the repo.

---

## 6:45–7:05 · Demo — Close

**Screen:** AGENTS.md beside the changed-files list. `[CALLOUT: "Commit AGENTS.md"]`

The team commits AGENTS.md, and every teammate and every new thread gets the same note. So how did Friday end?

> **⏹ SWITCH → SLIDES.** Stop the demo recording. Start clip C at slide 13.

---

## 7:05–7:25 · Slide 13 — Friday: one review, zero ping-pong

`[CLICK]` Friday afternoon. Codex opens the coupon pull request again. `[CLICK]` AppError with a code. `[CLICK]` An example in the docstring. `[CLICK]` Tested with the team command, and the changelog updated. `[CLICK]` Maliha approves it in one pass. `[CLICK]` Same prompt as Tuesday. The only change was one Markdown file.

---

## 7:25–7:40 · Slide 14 — Your turn

`[CLICK]` Now your turn. What's in your team's onboarding notes that Codex has never read? `[CLICK]` List the three review comments you type most. `[CLICK]` Make each one checkable. `[CLICK]` And commit AGENTS.md.

---

## 7:40–8:00 · Slide 15 — Summary

`[CLICK]` So, what can you do now that you couldn't before? Codex starts every task like a new hire. `[CLICK]` AGENTS.md is its onboarding note. `[CLICK]` Write rules a reviewer can check. `[CLICK]` And keep reviewing: rules guide Codex, but review still checks the result. Thanks for watching.

---

## If the result differs

- **The first run (no rules) already follows a rule**, such as adding tests: say so honestly. "Codex added tests on its own, but it still raised ValueError and skipped the changelog." Point at whatever differs.
- **The second run misses a rule:** show it, and tighten the wording in AGENTS.md (for example, "Always add a line to CHANGELOG.md"), then run again in a new thread. Real iteration is good teaching.
- **The rules don't seem to apply:** check that you started a new thread after adding the file, and that AGENTS.md is at the repo root.

## Delivery notes

- Pause for about one second after each `[CLICK]`.
- Keep the mouse still. Use callouts for pointing.
- Each Codex request took several minutes in practice. Record everything and cut the waits, labelling each cut "Agent wait shortened".
