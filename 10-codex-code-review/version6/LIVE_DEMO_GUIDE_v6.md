# Live demo guide v6: what to do in the Codex app

Jessica asked for a **real run in the Codex app** instead of screenshots. The story stays the same: build the feature, review it, comment on the line, make a small fix, and review again.

## The plan in one line

You record the screen while you work in Codex. I cut the waits, add the callouts and smooth the edits. Then you record the voice-over, watching the edited video.

Doing the voice-over separately is easier than talking while you click. You can watch the screen and speak at a relaxed pace. Jessica's narration feedback is easier to meet this way too.

---

## 1. Before you record (10 minutes)

**Reset the project:**
1. Open PowerShell (outside Codex) and run:
   ```
   cd G:\ReplitProjects\pluralsight-openai-codex-auditions\photo-take
   git status
   git checkout -- .
   git clean -fd
   ```
   - The checkout and clean commands remove the changes from the last run, including the `avatars/` folder.
   - `photo-take` currently has leftover edits from the last run, so this step is needed.
2. Check the reset worked: open `app\profile.py`. It should **not** contain `upload_avatar`.

**Set up the screen:**
- **Windows:** turn on Focus Assist (no notifications) and use one monitor. Check that "Activate Windows" isn't showing.
- **Codex app:** maximise the window and zoom in one step (**Ctrl +**), so the code is easy to read.
- **Recorder:** OBS or similar, recording at **1920×1080** and 30 fps. Record the whole screen.
- **Prompts:** keep the three messages from section 4 in Notepad, ready to copy.

**Mouse rules (Pluralsight):**
- Move the mouse only to click or hover.
- Don't circle or point at things with the mouse; the callouts do that job.
- Park the mouse at the side of the screen while you wait.

---

## 2. Record the run (one take, about 15–20 minutes of raw video)

Keep recording through the waits; I'll cut them. If something goes wrong, keep going. I can usually edit around it.

| # | What you do | What should appear |
|---|---|---|
| 1 | In the sidebar, hover **photo-take** and click its new-chat icon. Wait 2 seconds. | "What should we build in photo-take?" |
| 2 | Click the composer. **Type** Prompt 1 at a steady speed, or paste it (typing looks more real; I'll speed up the typing if it's long). Wait 2 seconds so the prompt is readable, then press **Enter**. | Codex starts working |
| 3 | Wait. Don't touch anything. If it asks for permission, approve it. | After a few minutes: "Edited 2 files", tests passed |
| 4 | Scroll slowly so the result card ("Edited…", "N tests passed") is fully visible. Pause 3 seconds. | The Feature Developer result |
| 5 | Click the composer, **type `/review`**, and wait for the menu. Pause 1 second, then pick **Review uncommitted changes**. | Review mode starts |
| 6 | Wait. | The findings, e.g. "One issue found", with a **P1/P2** label |
| 7 | Click the finding, or the **Review** button, to open the code with the comment on the line. Pause 4 seconds. Let the comment be read. | The comment shown on the code lines |
| 8 | Hover the first line of the finding until the **+** appears, then click it. **Type** your comment (section 4). Click **Comment**. | "1 comment" in the composer |
| 9 | In the composer, type the follow-up message and press **Enter**. | Codex fixes it |
| 10 | Wait. | "N tests passed" and a new test |
| 11 | Open the Review panel. Set the scope menu to **Last Turn**. Pause 4 seconds on the diff. | Only the small fix (+ and − lines) |
| 12 | In the composer: `/review` → **Review uncommitted changes**. Wait. | "No actionable issues" (or similar) |
| 13 | Pause 3 seconds on the clean result. Stop recording. | End of the demo |

**If the Review panel shows "No file changes yet":** its scope menu (top left of the panel) has switched to Branch. Choose **Unstaged**, or **Uncommitted**, and carry on.

---

## 3. If Codex behaves differently (it often does)

Codex doesn't give the same answer every time. Earlier runs found two different issues:
- **28 Sep:** a full disk leaves a half-saved file behind.
- **5 Oct:** an unusual file name crashes a valid upload.

**Whatever it finds first is fine.** The lesson is the same either way. Use that finding, write your comment about it in one plain sentence, and send me the recording. I'll update:
- slide 10's red row and test counts;
- the demo narration.

Other cases:
- **No findings at all:** start a new thread and run it once more. If it still finds nothing, tell me and we'll decide together. Don't stage a fake bug.
- **The fix changes more than one thing:** click **Undo** and resend with: *"Only change upload_avatar. Keep the scope minimal."*
- **A take goes badly:** reset (section 1) and start again.

---

## 4. The messages to use

**Prompt 1** (new thread):
```
Let users upload a profile photo. Add upload_avatar(user_id, file) to app/profile.py that saves the file under avatars/ and updates the user's avatar_url. Add tests and run them.
```

**Inline comment** (on the line Codex flagged; adapt it to the finding):
```
Agreed. If saving fails, delete the half-saved file. Add a test for it.
```
Example for the file-name finding instead:
```
Agreed. If the file name isn't text, fall back to .png. Add a test for it.
```

**Follow-up message:**
```
Address the inline comments and keep the scope minimal.
```

---

## 5. Voice-over for the demo (after I edit the video)

I'll send you the edited demo with callouts and a time-coded script that matches what Codex actually did. Below is the draft, written for the disk-full finding.

**How to deliver it:** use the same style as the slides. Talk to one colleague, pause at ⏸, and say what you're doing and *why*.

**Feature Developer**
Here's a small bookshop app called photo-take. ⏸ It has users, a profile page, and a couple of tests. ⏸
I'll start a new thread and ask Codex for a feature, in plain English. ⏸ Let users upload a profile photo, save it under avatars, and add tests. ⏸
Codex reads the project, writes the code, and runs the tests. This takes a few minutes, so I've shortened the wait. ⏸
And there it is. ⏸ The tests pass, and two files changed. ⏸ This is the moment most of us would commit. ⏸ But remember Friday afternoon? ⏸ ***Not yet.***

**Senior Reviewer**
Now we switch hats. ⏸ I type slash review, ⏸ and choose Review uncommitted changes, which is exactly what Codex just wrote. ⏸
Codex is in review mode now. It reads the code, looking for real risks, ⏸ but it doesn't change anything. ⏸
And look at that. ⏸ ***One issue***, even though every test is still green. ⏸
Here it is, right on the lines that save the file. ⏸ If the disk fills up mid-save, the upload fails, but a broken, half-saved file stays behind. ⏸ That's our Saturday, two am. ⏸

**Point at the line**
I agree, so I'll point at that exact line. ⏸ Hover, click the plus, ⏸ and write one sentence: if saving fails, delete the half-saved file, and add a test. ⏸
Then one short message: address the inline comments, and keep the scope minimal. ⏸

**The small fix**
Codex fixes the cleanup and adds a test that covers it. ⏸ All the tests pass. ⏸
In Last Turn, I can see only this change. ⏸ No surprise rewrites. ⏸

**Review again**
One last check. ⏸ Slash review, again. ⏸ ***No actionable issues.*** ⏸ Now, and only now, I'm ready to commit. ⏸ Let's compare the two versions.

---

## 6. Then send me

- The raw screen recording (no voice needed).
- A one-line note on what Codex found, if it differed from the disk-full case.

I'll return:
- the edited demo with callouts and the waits cut;
- the matching time-coded voice-over script;
- the updated slide 10.
