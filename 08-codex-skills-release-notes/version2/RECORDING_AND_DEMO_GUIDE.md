# Recording & Demo Guide: Reusable Team Workflows with OpenAI Codex Skills (Codex app on Windows)

This guide covers when to switch between slides and the demo, how to record the pieces, and the exact demo steps. The demo was rehearsed in your Codex app on 27 Sep 2026; `demo_reference_storyboard.mp4` shows the real screens with callouts.

---

## 1. The flow

```
 SLIDES 1–6            DEMO in Codex app            SLIDES 7–8
 0:00 ─────── 3:00 ──► 3:00 ─────────── 6:30 ──► 6:30 ─── 7:15
```

- **Slides → demo:** end of slide 6, on *"Let's open Maliha's repo in the Codex app."*
- **Demo → slides:** after *"Let's step back and sum up."* Then show slide 7.

## 2. How to record: three clips plus a voice track

| Clip | What | How |
|------|------|-----|
| **A** | Slides 1–6 in PowerPoint Slide Show | Screen recorder, full screen, 1920×1080 |
| **B** | The demo in the Codex app (section 4) | Same recorder and resolution |
| **C** | Slides 7–8 | Same as A |
| **Voice** | The narration script | USB mic on its own audio track |

Join A → B → C in Camtasia, Clipchamp or DaVinci Resolve with straight cuts. Recording the demo screen first and adding your voice afterwards usually sounds best, because the waits are long.

## 3. One-time setup (already done on your PC)

- The project folder **`skills-take`** is in `G:\ReplitProjects\pluralsight-openai-codex-auditions`, with Git history. It has already been added and trusted in the Codex app.
- The ready-made file you'll copy in during the demo is in **`skills-kit\release-notes`**, next to it.
- The skill has already been copied into `skills-take\.agents\skills` during the rehearsal. **Before recording, delete that `.agents` folder** so you can add the skill on camera (or skip that step and say it's already there).

**Codex app basics (verified)**

| Thing | Where / how |
|-------|-------------|
| New thread in the project | Hover the project name in the sidebar and click the **new chat** icon beside it. The screen says "What should we build in skills-take?" |
| Permission control | **Approve for me**, under the composer (the default worked) |
| Integrated terminal | **Ctrl + J** (PowerShell). **Type single commands only; never paste several lines**, because each line runs |
| Codex's commands | Click **Worked for …** to expand what it ran |
| Result card | **Edited &lt;file&gt; +N −M**, with **Undo** and **Review** |
| Review panel | **Review** → **Last Turn** → expand button (top right) for full width |

**Screen hygiene**
- [ ] Focus Assist on; close Slack, email and the browser.
- [ ] **Move the Claude app window off the recording screen.** During the rehearsal it kept appearing over the Codex app.
- [ ] Zoom the app (Ctrl + =), record one monitor, and cover or activate the "Activate Windows" watermark.
- [ ] Prompts from `CODEX_PROMPTS.txt` ready in Notepad, off-screen.

**Waiting:** requests took **3–8 minutes each** during the rehearsal. The first one also hit a Git "dubious ownership" warning, which Codex worked around by itself. Record everything and cut the waits, labelling each cut "Agent wait shortened".

---

## 4. Demo steps (clip B, 3:00–6:30)

### Step 1 · Without a skill (3:00–3:40)
| Do | You'll see (real run) | Callout |
|----|-----------------------|---------|
| New thread in **skills-take**. Paste: `Write release notes for everything that changed since v1.2.0.` | After several minutes: "Created RELEASE_NOTES.md covering all seven commits…" and an **Edited RELEASE_NOTES.md +24 −0** card | — |
| **Review** → expand | `# Bookshop API release notes since v1.2.0`, then Breaking, Features, Fixes **and "Maintenance and documentation"** (deps bump, tests, README) | "No version number", "Chores and docs included" |

### Step 2 · Add the skill (3:40–4:05)
**Undo** on the card. Then Ctrl+J and type (one line): `Copy-Item -Recurse ..\skills-kit\release-notes .agents\skills\`
Callout: `.agents/skills/release-notes`.

### Step 3 · Call it by name (4:05–4:45)
| Do | You'll see (real run) | Callout |
|----|-----------------------|---------|
| New thread (hover **skills-take**, click the new-chat icon). Type `$rel` | Picker: **Release Notes**, "Write release notes or a changelog for commits since a git tag…", labelled **Project** | "Project skill found" |
| Choose it, type ` since v1.2.0`, press Enter | "I'll use the release-notes skill…", then **Reading Release Notes skill**, **Loaded a tool, ran commands** | "Reading the skill" |

### Step 4 · Review (4:45–5:25)
| Do | You'll see (real run) | Callout |
|----|-----------------------|---------|
| Result: "Created release-notes/2.0.0.md. Includes 2 features, 1 fix, and 1 breaking change since v1.2.0." → **Review** | `## v2.0.0`, ⚠️ Breaking changes, ✨ Features, 🐛 Fixes; no chores; one file (+11) | "release-notes/2.0.0.md", "Breaking change first", "No chores" |

### Step 5 · Plain words (5:25–6:05)
**Undo** the file. New thread. Paste: `Draft the changelog for what we shipped since v1.2.0.`
Real run: the first line reads **"I'll use the release-notes skill to review the commits since v1.2.0 and draft the changelog."** Callouts: "No $ mention", "Skill chosen from its description".

### Step 6 · Close (6:05–6:30)
Show the `.agents/skills/release-notes` folder and say the closing line. Stop the recording.

---

## 5. Resetting between takes

```powershell
cd G:\ReplitProjects\pluralsight-openai-codex-auditions\skills-take
Remove-Item -Recurse -Force .agents, release-notes, RELEASE_NOTES.md -ErrorAction SilentlyContinue
git status   # should say: nothing to commit, working tree clean
```

Always start a **new thread** for each take.

---

## 6. Editing checklist

- [ ] Order: A → B → C; straight cuts.
- [ ] Noise reduction on the voice; remove clicks and typing.
- [ ] Add each callout listed above for 3–5 seconds. Pink = key fact, yellow = attention.
- [ ] Label every cut wait "Agent wait shortened".
- [ ] Zoom 1.5–2× on the diff when the text is small.
- [ ] Final length **5–8 minutes** (target 7:15). Export 1080p MP4 and watch it once before submitting.
