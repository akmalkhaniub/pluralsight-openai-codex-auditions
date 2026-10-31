# 🎙️ CODEX LIVE DEMO TELEPROMPTER (CLIP B: 3:25 – 6:17)

> **Instructions for Recording:**  
> • Keep this window side-by-side with your Codex app or on your 2nd screen.  
> • Gray code blocks = **Exact text to Copy & Paste**.  
> • Bold blockquotes = **What you Speak into the mic**.  
> • Keep your hands off the mouse while speaking.

---

## ⚡ Quick 5-Second Reset (Run Between Takes in PowerShell)
```powershell
cd G:\ReplitProjects\pluralsight-openai-codex-auditions\photo-take; git reset --hard HEAD; git clean -fd
```

---

## 🟢 SCENE 1: The Feature Developer (3:25 – 4:10)

### 1. ACTION (Codex App)
1. Start a **New Thread** (`Ctrl + N`) in project **`photo-take`**.
2. Paste into the composer and hit **Enter**:

```text
Let users upload a profile photo. Add upload_avatar(user_id, file) to app/profile.py that reads the file stream and saves it under avatars/ using open(), and updates the user's avatar_url. Add unit tests and run them.
```

### 2. SPOKEN SCRIPT (Read aloud clearly)
> Here we are in our clean bookshop repository.
>
> In the composer, I'll paste our feature request:
> *"Let users upload a profile photo. Add upload_avatar in app/profile.py that reads the file stream and saves it under avatars using open, and update the avatar URL. Add unit tests and run them."*
>
> Codex immediately inspects our repo context, writes the function, and runs the test suite.
>
> And right there—all unit tests passing, clean assertions.
>
> The Feature Developer satisfied the ticket requirements and thinks the job is done.
>
> But are we ready to commit? Absolutely not.

*(Take hands off mouse. Let Codex finish. Wait is cut in editing).*

---

## 🔍 SCENE 2: The Senior PR Reviewer (4:10 – 5:05)

### 1. ACTION (Codex App)
1. In the composer, type and send:

```text
/review
```
2. Select: **"Review uncommitted changes"**
3. Codex opens the Review pane and flags lines 25–32 with a **P2 finding** (*unhandled exception leaves orphaned file on disk-full/network drop*).

### 2. SPOKEN SCRIPT (Read aloud clearly)
> Let's put on the Senior Reviewer's hat.
>
> I'll type slash review, and choose **Review uncommitted changes**.
>
> Codex shifts into adversarial inspection mode: it reads, analyzes failure modes, and changes zero code.
>
> And look at what it just caught!
>
> A **Priority 2** finding right on the file stream lines.
>
> All unit tests passed, but Codex realized that if the server disk fills up or the connection terminates mid-transfer...
>
> A half-written, corrupted file is permanently abandoned in our avatars storage!
>
> The Feature Developer proved it worked under sunny-day conditions.
>
> The Senior Reviewer proved what happens during a production failure.

---

## 🎯 SCENE 3: Point at the Line (5:05 – 5:40)

### 1. ACTION (Codex App)
1. In the diff viewer, hover over the file open line (around **line 25 or 26**).
2. Click the blue **`+`** icon on the line margin.
3. Paste into the comment box and click **Comment**:

```text
Agreed: if saving fails, delete the half-saved file. Add a test for it.
```

4. Now in the main composer at the bottom (which shows `1 comment`), paste and send:

```text
Address the inline comments and keep the scope minimal.
```

### 2. SPOKEN SCRIPT (Read aloud clearly)
> We're not going to re-prompt from scratch or let Codex guess.
>
> I'll hover right over the line where the file handle is opened, click the plus icon, and leave our directive:
>
> *"Agreed: if saving fails, delete the half-saved file. Add a test for it."*
>
> Now in the composer, I reinforce the scope boundary:
>
> *"Address the inline comments and keep the scope minimal."*
>
> Hit send.

---

## 🛠️ SCENE 4: The Surgical Fix (5:40 – 6:00)

### 1. ACTION (Codex App)
1. Codex wraps the write in `try...except`, calls `destination.unlink()`, and adds a regression test.
2. Result: **10 tests pass**.
3. At the top of the Review pane, switch the scope dropdown from *Uncommitted* to **"Last Turn"**.
4. Shows the tight **+6 −6 lines** diff.

### 2. SPOKEN SCRIPT (Read aloud clearly)
> Codex gets right to work.
>
> Notice how disciplined this is:
> It wraps the write stream in a clean try/except, triggers destination dot unlink, and adds a dedicated regression test that simulates a broken stream.
>
> All tests are passing!
>
> Switching the diff view to **Last Turn** confirms the beauty of this workflow:
> Exactly six lines added, six lines modified.
>
> No hallucinations, no unwanted refactoring.

---

## ✅ SCENE 5: The Clean Re-Review (6:00 – 6:17)

### 1. ACTION (Codex App)
1. Type into the composer:

```text
/review
```
2. Select: **"Review uncommitted changes"**
3. Codex returns: *"No actionable issues found."*

### 2. SPOKEN SCRIPT (Read aloud clearly)
> One final check to be certain:
> Slash review, review uncommitted changes.
>
> And there it is: *"No actionable issues found."*
>
> Now—and only now—are we confident to git commit and open our PR.
>
> Let's see the side-by-side contrast.

---
*(End of Demo. Switch back to PowerPoint Slide 9 for Clip C).*
