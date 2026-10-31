# Timed Narration Script: Who Reviews the AI? Code Review with Codex (v1)

**Author:** Akmal Khan · **Level:** Intermediate · **Target:** about 7:35

**Story and analogy:** Codex writes code in minutes, so reviewing is now the slow part. Great writers don't edit their own first draft: they switch hats. `/review` is Codex switching from writer to editor.

`[CLICK]` = advance one slide animation. `[CALLOUT]` = on-screen callout added in video editing. Bracketed text is not spoken.

---

## 0:00–0:15 · Slide 1 — Title

Hi, I'm Akmal Khan, a Senior Full Stack AI Architect. Your AI can write code in minutes. So who reviews the AI?

---

## 0:15–0:40 · Slide 2 — Meet Codex

First, a quick introduction. Codex is OpenAI's coding agent. You give it a task in plain English, and it `[CLICK]` reads your repo, `[CLICK]` writes the change, `[CLICK]` runs your tests, `[CLICK]` and hands you a diff to review. `[CLICK]` It runs in the Codex app, the command line, or your IDE. Today, I'll use the Codex app on Windows.

---

## 0:40–1:05 · Slide 3 — Overview

`[CLICK]` Here's what changes when you work with Codex. `[CLICK]` Writing the code takes minutes. `[CLICK]` Reviewing it takes much longer. `[CLICK]` Review is the new bottleneck. `[CLICK]` So by the end, you'll let Codex do the first review, and only check what matters. `[CLICK]` Three parts: the writer, the editor, and the proof.

---

## 1:05–1:45 · Slide 4 — Codex built it. The tests pass. Ship it?

`[CLICK]` Here's the task: let users upload a profile photo. `[CLICK]` Codex writes this. `[CLICK]` Nine tests pass. `[CLICK]` It even handles errors. `[CLICK]` So, would you approve it? `[CLICK]` Take a second. `[CLICK]` Hold that thought. `[CLICK]` Because tests only check what we asked for. They can't check what we forgot to ask.

---

## 1:45–2:10 · Slide 5 — Great writers don't edit their own first draft

`[CLICK]` Think about writing. The writer asks: did I build what was asked? `[CLICK]` The editor asks a different question: what could go wrong? `[CLICK]` Codex can wear both hats. Just never both at once.

---

## 2:10–2:45 · Slide 6 — Switch hats with /review

In the Codex app, switching hats takes one command. `[CLICK]` Type slash review in the composer. `[CLICK]` Pick what to review: here, the uncommitted changes Codex just made. `[CLICK]` Codex reports its findings right on the lines, most important first. `[CLICK]` And it doesn't change any code. You decide. `[CLICK]` You can review your uncommitted changes, or compare against a base branch. `[CLICK]` Today: the uncommitted changes, which are Codex's new edits.

---

## 2:45–3:15 · Slide 7 — Point at the line. Keep the fix small.

`[CLICK]` When a finding matters, `[CLICK]` hover the line and click the plus. `[CLICK]` Leave a short comment. `[CLICK]` Then send: address the inline comments and keep the scope minimal. `[CLICK]` You get one check and one test, and nothing else touched. `[CLICK]` That's the habit: build, review, commit. Never straight from build to commit.

---

## 3:15–3:25 · Slide 8 — Demo: the writer, then the editor

`[CLICK]` First, Codex builds the upload. `[CLICK]` Then we review its changes. `[CLICK]` Comment on the risky line. `[CLICK]` And review again. Let's open the app.

> **⏹ SWITCH → DEMO.** Stop clip A here. Start clip B in the Codex app.

---

## 3:25–4:10 · Demo — The writer

**Screen:** New thread in **photo-take**. Paste the prompt from `CODEX_PROMPTS.txt` and send. Cut the wait (label "Agent wait shortened"). `[CALLOUT: "All 9 tests pass"]`

This is a tiny bookshop app: users, a profile page, and a couple of tests. I'll ask Codex to let users upload a profile photo. Codex reads the project, writes the upload, and runs the tests. All nine pass, and it even added error handling. This is the writer's hat. Would you ship it?

---

## 4:10–5:05 · Demo — The editor

**Screen:** Type `/review` → **Review uncommitted changes**. Cut the wait. `[CALLOUT: "One issue. Tests still pass."]`, then the inline P2 comment on lines 26–32.

Now let's switch hats. Slash review, review uncommitted changes. Codex is in review mode now: it reads, it doesn't change code. And here's a finding, priority two, right on the lines. **(Ah-ha)** All nine tests pass, but if the disk fills up while a photo is being saved, a half-saved file is left behind. Codex even says it reproduced it. The writer made it work. The editor asked what could go wrong.

---

## 5:05–5:40 · Demo — Point at the line

**Screen:** Hover line 26 → **+** → type the comment → **Comment**. Then the follow-up message. `[CALLOUT: "Your decision, in one sentence"]`

I agree with this one, so I'll point at the line. Plus, and one sentence: if saving fails, delete the half-saved file, and add a test for it. Then: address the inline comments and keep the scope minimal.

---

## 5:40–6:20 · Demo — The small fix

**Screen:** Result message. Review scope → **Last Turn**. `[CALLOUT: "New test failed before the fix"]`, `[CALLOUT: "+6 −6"]`

Codex fixed the cleanup and added a test that failed before the fix. Ten tests pass now. And Last Turn shows only this change: six lines in, six lines out. No surprise rewrites.

---

## 6:20–6:40 · Demo — Review again

**Screen:** `/review` → **Review uncommitted changes**. Cut the wait. `[CALLOUT: "No actionable issues"]`

One more review, to be sure. No actionable issues. Now I'm ready to commit. Let's compare the two versions.

> **⏹ SWITCH → SLIDES.** Stop the demo recording. Start clip C at slide 9.

---

## 6:40–7:00 · Slide 9 — One review. One real risk caught.

`[CLICK]` With only the writer, the upload worked and nine tests passed. `[CLICK]` But a full disk could leave a broken file behind. `[CLICK]` With the writer and the editor, the same feature, plus one test, `[CLICK]` and failed saves are cleaned up. `[CLICK]` The tests were green both times. The review made the difference.

---

## 7:00–7:15 · Slide 10 — Your turn

`[CLICK]` So here's one habit to take away: slash review. `[CLICK]` After every Codex task, before every commit. `[CLICK]` And check the findings cover the editor's questions: what if it fails halfway, who's allowed, and what about empty or huge input.

---

## 7:15–7:35 · Slide 11 — Summary

`[CLICK]` To wrap up. Review is the new bottleneck. `[CLICK]` Switch hats with slash review before you commit. `[CLICK]` Point at the line, and keep the fix small. `[CLICK]` And remember: Codex finds, but you decide. Thanks for watching.

---

## If the result differs

- **Rehearsal result (28 Sep 2026):** Codex's writer run passed 9 tests. `/review` found one P2 issue: a disk-full failure leaves a half-saved file. After the inline comment, Codex fixed it with a +6 −6 change and a regression test (10 tests), and the second review found no actionable issues.
- **A different finding comes up first:** use it. Say what could go wrong in one plain sentence, comment on that line, and adjust slide 9's red row.
- **No findings at all:** say so honestly, add your own inline comment and continue. The lesson still holds: you decide.
- **The fix touches more than you asked:** point it out, Undo, and resend with "only change upload_avatar".

## Delivery notes

- Pause for about one second after each `[CLICK]`.
- Keep the mouse still. Use callouts for pointing.
- Cut every Codex wait and label it "Agent wait shortened".
