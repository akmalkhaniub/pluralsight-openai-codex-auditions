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

`[CLICK]` Here's the task: let users upload a profile photo. `[CLICK]` Codex writes this. `[CLICK]` Four tests pass. `[CLICK]` The code is clean and readable. `[CLICK]` So, would you approve it? `[CLICK]` Take a second. `[CLICK]` Hold that thought. `[CLICK]` Because tests only check what we asked for. They can't check what we forgot to ask.

---

## 1:45–2:10 · Slide 5 — Great writers don't edit their own first draft

`[CLICK]` Think about writing. The writer asks: did I build what was asked? `[CLICK]` The editor asks a different question: what could go wrong? `[CLICK]` Codex can wear both hats. Just never both at once.

---

## 2:10–2:45 · Slide 6 — Switch hats with /review

In the Codex app, switching hats takes one command. `[CLICK]` Type slash review in the composer. `[CLICK]` Pick what to review. `[CLICK]` Codex reports its findings right on the lines, most important first. `[CLICK]` And it doesn't change any code. You decide. `[CLICK]` It can review uncommitted changes, a branch, or a commit. `[CLICK]` Today we'll use Last turn: Codex's own edits.

---

## 2:45–3:15 · Slide 7 — Point at the line. Keep the fix small.

`[CLICK]` When a finding matters, `[CLICK]` hover the line and click the plus. `[CLICK]` Leave a short comment. `[CLICK]` Then send: address the inline comments and keep the scope minimal. `[CLICK]` You get one check and one test, and nothing else touched. `[CLICK]` That's the habit: build, review, commit. Never straight from build to commit.

---

## 3:15–3:25 · Slide 8 — Demo: the writer, then the editor

`[CLICK]` First, Codex builds the upload. `[CLICK]` Then we review its last turn. `[CLICK]` Comment on the risky line. `[CLICK]` And review again. Let's open the app.

> **⏹ SWITCH → DEMO.** Stop clip A here. Start clip B in the Codex app.

---

## 3:25–4:10 · Demo — The writer

**Screen:** New thread in **photo-take**. Paste the prompt from `CODEX_PROMPTS.txt` and send. Cut the wait (label "Agent wait shortened"). `[CALLOUT: "Tests pass"]` on Codex's final message.

This is a small bookshop app with user profiles. I'll ask Codex to let users upload a profile photo. Codex reads the project, writes the upload, and runs the tests. They pass. This is the writer's hat.

---

## 4:10–5:05 · Demo — The editor

**Screen:** Type `/review`, choose **Last turn**. Cut the wait. Box the finding with a callout: `[CALLOUT: "Finding on the upload line"]`.

Now let's switch hats. Slash review, and I'll review the last turn: Codex's own edits. It hasn't changed any code. It's only reading. And here's a finding on the upload line. **(Ah-ha)** Same Codex, a minute later, but a different job. The writer made it work. The editor asked what could go wrong: nothing stops someone uploading a two-gigabyte file.

*[If the top finding is different, read it, say why it matters in one sentence, and use it. See the recording guide.]*

---

## 5:05–5:40 · Demo — Point at the line

**Screen:** Hover the line → **+** → type the comment. Send the follow-up message. `[CALLOUT: "One comment, one line"]`

I agree with this one, so I'll point at the line. Plus, and a short comment: reject files over five megabytes. Then: address the inline comments and keep the scope minimal.

---

## 5:40–6:20 · Demo — The small fix

**Screen:** Result card → **Review**. `[CALLOUT: "Size check"]`, `[CALLOUT: "New test"]`. Show the files-changed count.

Codex added a size check and a test for it. Look at the diff: only what I asked for. No surprise rewrites.

---

## 6:20–6:40 · Demo — Review again

**Screen:** `/review` → **Last turn** again. `[CALLOUT: "No findings on the upload"]`

One more review, to be sure. The upload finding is gone. Now I'm ready to commit. Let's compare the two versions.

> **⏹ SWITCH → SLIDES.** Stop the demo recording. Start clip C at slide 9.

---

## 6:40–7:00 · Slide 9 — One review. One real risk caught.

`[CLICK]` With only the writer, the upload worked and the tests passed. `[CLICK]` But a huge file could fill the disk. `[CLICK]` With the writer and the editor, the same feature, one more test, `[CLICK]` and big files are rejected. `[CLICK]` The tests were green both times. The review made the difference.

---

## 7:00–7:15 · Slide 10 — Your turn

`[CLICK]` So here's one habit to take away: slash review. `[CLICK]` After every Codex task, before every commit. `[CLICK]` And check the findings cover the editor's questions: size, permissions, and empty or huge input.

---

## 7:15–7:35 · Slide 11 — Summary

`[CLICK]` To wrap up. Review is the new bottleneck. `[CLICK]` Switch hats with slash review on the last turn. `[CLICK]` Point at the line, and keep the fix small. `[CLICK]` And remember: Codex finds, but you decide. Thanks for watching.

---

## If the result differs

- **Codex's top finding isn't about file size** (for example, any file type is accepted, or the file name isn't safe): use it. Say what could go wrong in one plain sentence, comment on that line, and adjust the payoff slide wording if needed.
- **No findings at all:** say so honestly, then add your own inline comment on the write line ("Reject files over 5 MB") and continue. The lesson still holds: you decide.
- **The fix touches more than you asked:** point it out, Undo, and resend with "only change the upload function".

## Delivery notes

- Pause for about one second after each `[CLICK]`.
- Keep the mouse still. Use callouts for pointing.
- Cut every Codex wait and label it "Agent wait shortened".
