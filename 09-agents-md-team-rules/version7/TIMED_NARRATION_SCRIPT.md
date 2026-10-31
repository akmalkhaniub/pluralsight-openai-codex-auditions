# Timed Narration Script: Team Rules for OpenAI Codex with AGENTS.md (v6)

**Author:** Akmal Khan · **Level:** Intermediate · **Target:** about 7:30

**Story and analogy:** Codex is a brilliant teammate with no memory. Every task starts with an empty head, so your review comments come back every time. The fix is a note it reads first: AGENTS.md. Your review comments become the note.

`[CLICK]` = advance one slide animation. `[CALLOUT]` = on-screen callout added in video editing. Bracketed text is not spoken.

---

## 0:00–0:15 · Slide 1 — Title

Hi, I'm Akmal Khan, a Senior Full Stack AI Architect. If you've ever left the same review comment on AI-written code twice, this one is for you.

---

## 0:15–0:40 · Slide 2 — Meet Codex

First, a quick introduction. Codex is OpenAI's coding agent. You give it a task in plain English, and it `[CLICK]` reads your repo, `[CLICK]` writes the change, `[CLICK]` runs your tests, `[CLICK]` and hands you a diff to review. `[CLICK]` You can use it in the Codex app, the command line, or your IDE. Today, I'll use the Codex app on Windows.

---

## 0:40–1:05 · Slide 3 — Overview

`[CLICK]` Here's the thing about Codex. It's your smartest teammate, and it forgets everything between tasks. `[CLICK]` While it works, it knows plenty. `[CLICK]` Task done, memory empty. `[CLICK]` So by the end, you'll stop leaving the same review comments on Codex's code. `[CLICK]` We'll see the problem, the fix, and the proof.

---

## 1:05–1:45 · Slide 4 — Codex wrote this. Spot the problem.

`[CLICK]` Codex just added a login limit to our bookshop: five failed tries and the account locks for fifteen minutes. `[CLICK]` It works. But pause for a second. What would your reviewer say? `[CLICK]` Here's what ours said. `[CLICK]` One: the limits are hard-coded. They belong in our config file, so ops can change them. `[CLICK]` Two: "No account for this email" tells an attacker which emails are real. `[CLICK]` Three: a print statement isn't an audit trail. Our security team reads audit_log. None of this is a bug. These are our team's rules.

---

## 1:45–2:05 · Slide 5 — Why? Every task starts with an empty head.

`[CLICK]` Task one, we explain the rules. `[CLICK]` Task two, it's forgotten. `[CLICK]` Task three, same comments again. `[CLICK]` That's because our rules live in people's heads, onboarding docs, and old review threads. `[CLICK]` None of those is where Codex looks.

---

## 2:05–2:35 · Slide 6 — The fix: leave a note where Codex looks first

`[CLICK]` Think of a teammate with no memory. What would you do? `[CLICK]` You'd leave a note on their screen. `[CLICK]` Read me first. `[CLICK]` For Codex, that note is a file called AGENTS.md, at the root of your repo. `[CLICK]` Codex reads it before every task. `[CLICK]` It's committed in Git, so the whole team shares it. `[CLICK]` And if you edit it, start a new thread so Codex reads it again.

---

## 2:35–3:00 · Slide 7 — Your review comments ARE the note

`[CLICK]` So what goes in the note? Here's the trick: your review comments. `[CLICK]` Limits in config becomes a rule. `[CLICK]` Never reveal whether an email exists becomes a rule. `[CLICK]` Use audit_log becomes a rule. `[CLICK]` Plus the test command. `[CLICK]` Write each comment once, as a rule a reviewer could check in the diff.

---

## 3:00–3:10 · Slide 8 — Demo: same prompt, without the note, then with it

`[CLICK]` First, no note. `[CLICK]` We'll check whether the stickers come back. `[CLICK]` Then we add AGENTS.md and send the same prompt. `[CLICK]` And compare. Let's open the repo.

> **⏹ SWITCH → DEMO.** Stop clip A here. Start clip B in the Codex app.

---

## 3:10–3:55 · Demo — Without the note

**Screen:** New thread in **login-take**. Paste the prompt and send. Cut the wait. `[CALLOUT: "Same prompt both times"]`

Here's the bookshop login from the slides: a login function, a config file, an audit log, and a couple of tests. There's no AGENTS.md yet. I'll ask Codex to add a login limit: after five failed attempts, lock that email for fifteen minutes.

---

## 3:55–4:25 · Demo — Spot the gaps

**Screen:** Result card → **Review** → expand. Box each gap with a numbered callout, same numbers as slide 4.

The code works, and Codex added tests. But hold it against our review comments, and check each one in the diff. Wherever a sticker comes back, Codex didn't do anything wrong. It simply had no note.

---

## 4:25–4:50 · Demo — Add AGENTS.md

**Screen:** **Undo** the change. Terminal (Ctrl+J): `Copy-Item ..\login-kit\AGENTS.md .`. Show the file. `[CALLOUT: "Repo root"]`

I'll undo that change and add the note from the slides, AGENTS.md, at the root of the repo. That's all the setup there is.

---

## 4:50–5:15 · Demo — Same task again

**Screen:** New thread (the note is read when a task starts). Paste the same prompt. Cut the wait.

New thread, because Codex reads AGENTS.md when a task starts. Same prompt, word for word.

---

## 5:15–6:15 · Demo — Compare the diff

**Screen:** Review → expand. `[CALLOUT: "Limits from config.py"]`, `[CALLOUT: "Invalid email or password."]`, `[CALLOUT: "audit_log('LOGIN_LOCKED')"]`. Show Codex's message about running the test command.

Now look at the difference. The limits come from config. Every failure says the same thing: invalid email or password, so an attacker learns nothing. The lockout is recorded with audit_log. And Codex ran the exact test command from our note.

**(Ah-ha)** Every sticker from before is now a line in the diff. Same model, same prompt. The only thing we changed is one note in the repo.

---

## 6:15–6:35 · Demo — Close

**Screen:** AGENTS.md beside the changed-files list. `[CALLOUT: "Commit AGENTS.md"]`

The team commits AGENTS.md, and every teammate and every new thread reads the same note. Let's put the two diffs side by side.

> **⏹ SWITCH → SLIDES.** Stop the demo recording. Start clip C at slide 9.

---

## 6:35–6:55 · Slide 9 — Same prompt. One file. Zero comments.

`[CLICK]` Without the note, three review comments. `[CLICK]` With AGENTS.md, the same prompt. `[CLICK]` Every comment is already handled. One file changed the result: zero comments.

---

## 6:55–7:10 · Slide 10 — Your turn

`[CLICK]` Now your turn. What's on your team's note? `[CLICK]` Look at your last few reviews. `[CLICK]` Copy the comments you type most. `[CLICK]` Rewrite each one as a rule someone could check, and commit it.

---

## 7:10–7:30 · Slide 11 — Summary

`[CLICK]` So, to wrap up. Codex starts every task fresh. `[CLICK]` AGENTS.md is the note it reads first. `[CLICK]` Your review comments become its rules. `[CLICK]` And rules guide Codex, but you still review the result. Thanks for watching.

---

## If the result differs

- **The first run already follows a rule** (Codex can copy habits it sees in the repo, such as using config.py): say so honestly, and point at the rules it missed.
- **The second run misses a rule:** show it, tighten the wording in AGENTS.md, and run again in a new thread. Real iteration is good teaching.
- **The rules don't seem to apply:** check that you started a new thread after adding the file, and that AGENTS.md is at the repo root.

## Delivery notes

- Pause for about one second after each `[CLICK]`.
- Keep the mouse still. Use callouts for pointing.
- Each Codex request took several minutes in practice. Record everything and cut the waits, labelling each cut "Agent wait shortened".
