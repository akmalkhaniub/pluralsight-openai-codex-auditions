# Timed Narration Script: Reusable Team Workflows with OpenAI Codex Skills

**Author:** Akmal Khan · **Level:** Intermediate · **Target:** 7:15 (about 125–140 words per minute on slides)

`[CLICK]` = advance one slide animation. `[CALLOUT]` = on-screen callout added in video editing. Bracketed text is not spoken.
The demo lines describe what happened in a real practice run. If your run differs, say what you actually see.

---

## 0:00–0:25 · Slide 1 — Title

Every team has a chore that should look the same every time, and never quite does. Release notes are a classic.

I'm Akmal Khan. In the next seven minutes, we'll turn that chore into a Codex skill, so every teammate and every thread gets the same result.

---

## 0:25–1:00 · Slide 2 — Overview (the problem and WIIFM)

`[CLICK]` Maliha asked Codex for release notes on Monday. `[CLICK]` She asked the same question on Thursday.

`[CLICK]` Two different formats. Monday lists chores nobody cares about. Thursday buries a breaking change and forgets the version number.

`[CLICK]` So we'll capture the team's process once, `[CLICK]` let Codex find it when it's needed, `[CLICK: WIIFM]` and here's what's in it for you: explain a chore once, and every teammate's Codex does it your way.

---

## 1:00–1:30 · Slide 3 — Anatomy of a skill

`[CLICK]` A skill is just a folder. Put it in the repo under dot-agents slash skills, and everyone who clones the repo gets it.

`[CLICK: highlight]` The only required file is SKILL.md: a name, a description, then the steps.

`[CLICK]` A script handles the part that must be exact. Same commits in, same list out.

`[CLICK]` References hold detail, like our format, that Codex reads only when it needs to. Personal skills can live in your home folder instead.

---

## 1:30–2:00 · Slide 4 — How Codex picks a skill

`[CLICK]` Here's the part that matters. When a task starts, Codex sees only each skill's name and description, not the whole file.

`[CLICK]` When your request matches a description, `[CLICK]` Codex loads that skill's full instructions. `[CLICK]` Scripts and references come in only if the steps call for them.

`[CLICK: banner]` It's like a cookbook: you scan the index, and only open the recipe you need. So the description is the trigger. Write it the way people actually ask.

---

## 2:00–2:30 · Slide 5 — Inside SKILL.md

`[CLICK]` Here's Maliha's skill. `[CLICK: FRONTMATTER]` The front matter says when to use it: release notes or a changelog since a tag.

`[CLICK: STEPS]` The steps say what to do: run the script, then write the notes in the team format.

`[CLICK: GUARDRAILS]` The guardrails say what not to do: edit nothing else, and report back. It's plain Markdown. No code needed to write one.

---

## 2:30–3:00 · Slide 6 — Demo roadmap

Here's our plan. `[CLICK]` Ask for release notes with no skill. `[CLICK]` Add the skill to the repo. `[CLICK]` Call it by name. `[CLICK]` Then ask in plain words and see if Codex picks it on its own. `[CLICK]` And review what it wrote. Let's open Maliha's repo in the Codex app.

> **⏹ SWITCH → DEMO.** Stop the slide recording. Start clip B in the Codex app (see RECORDING_AND_DEMO_GUIDE.md, section 4).

---

## 3:00–3:40 · Demo — Without a skill

**Screen:** New thread in **skills-take**. Send: *Write release notes for everything that changed since v1.2.0.* Cut the wait. Open **Review** → expand. `[CALLOUT: "No version number"]` on the title, `[CALLOUT: "Chores and docs included"]` on the Maintenance section.

Here's Maliha's repo: seven commits since version one point two. First, no skill. I'll just ask for release notes.

Codex does a reasonable job, but look at what it chose. A file called RELEASE_NOTES.md in the root, no version number, and a maintenance section with dependency bumps and README edits. Ask again next week and you may get a different shape. Nothing here is wrong. It just isn't our format.

---

## 3:40–4:05 · Demo — Add the skill

**Screen:** Delete the generated file (Undo). Terminal (Ctrl+J): `Copy-Item -Recurse ..\skills-kit\release-notes .agents\skills\`. Then open the folder in Explorer or show `Get-ChildItem -Recurse .agents`. `[CALLOUT: ".agents/skills/release-notes"]`

I'll undo that file and add the skill. It's the folder from the slides: SKILL.md, the script and the format reference, copied into dot-agents slash skills. Because it lives in the repo, it's versioned and reviewed like any other code.

---

## 4:05–4:45 · Demo — Call it by name

**Screen:** New thread. Type `$rel` and show the picker: **Release Notes … Project**. Choose it, add *since v1.2.0*, send. `[CALLOUT: "Project skill found"]` on the picker. Cut the wait.

In a new thread, I type a dollar sign and start the name. There it is: Release Notes, labelled as a project skill, with the description we wrote. I pick it and add: since version one point two.

Codex says it's using the release-notes skill. It runs the script, and writes the notes.

---

## 4:45–5:25 · Demo — Review the result

**Screen:** Result card → **Review** → expand. `[CALLOUT: "release-notes/2.0.0.md"]` on the file name, `[CALLOUT: "Breaking change first"]`, `[CALLOUT: "No chores"]`.

Now compare. The file is release-notes slash two point zero point zero, because the script saw a breaking change and bumped the major version. Breaking changes come first, then features, then fixes. The chores, tests and docs are gone, exactly as our format says. And only this one file changed.

---

## 5:25–6:05 · Demo — Ask in plain words

**Screen:** Undo the file. New thread. Send: *Draft the changelog for what we shipped since v1.2.0.* `[CALLOUT: "No $ mention"]` on the prompt, then `[CALLOUT: "Skill chosen from its description"]` on Codex's first line.

One more test. New thread, and this time I don't name the skill. I just ask for a changelog of what we shipped.

**(Ah-ha)** Codex matches the request to the description and uses the same skill. Same file, same format. That's the payoff: nobody has to remember a command. They just ask.

---

## 6:05–6:30 · Demo — Close

**Screen:** The skill folder next to the generated notes. `[CALLOUT: "Commit the skill with the repo"]`

Maliha commits the skill folder, and the whole team gets it on their next pull. Let's step back and sum up.

> **⏹ SWITCH → SLIDES.** Stop the demo recording. Start clip C at slide 7.

---

## 6:30–6:50 · Slide 7 — Your first skill

`[CLICK]` Here's your practice. Which chore does your team repeat every week? That's your first skill.

`[CLICK]` Write the steps, `[CLICK]` script the fixed part, `[CLICK]` and test it with a plain request.

---

## 6:50–7:15 · Slide 8 — Summary

`[CLICK]` So, what can you do now that you couldn't before? Capture a chore once, and every thread can reuse it. `[CLICK]` The description decides when a skill loads, so write it the way people ask. `[CLICK]` Put the exact parts in a script, so the steps repeat reliably. `[CLICK]` And remember: a skill guides Codex, it doesn't replace your review. You now have a workflow you can use on your very next task. Thanks for watching.

---

## If the result differs

- **Codex doesn't pick the skill from plain words:** say so. Open SKILL.md, show the description, and add the words people use ("changelog", "what shipped"). Then retry in a new thread. This is a real lesson about descriptions, so keep it.
- **The first answer (no skill) already looks tidy:** point out what isn't your team's format: file name, version, the included chores.
- **Git "dubious ownership" message:** Codex works around it (you'll see `safe.directory` in its commands). The skill's script already handles this.

## Delivery notes

- Pause for about one second after each `[CLICK]`.
- Keep the mouse still. Use callouts for pointing.
- Each Codex request took two to eight minutes in practice. Record the whole thing and cut the waits, labelling each cut "Agent wait shortened".
