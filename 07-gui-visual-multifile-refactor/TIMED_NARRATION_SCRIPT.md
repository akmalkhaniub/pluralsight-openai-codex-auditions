# Timed Narration Script: Visual Multi-File Refactoring in OpenAI Codex (VS Code GUI)

* **Target Video Length:** 6 minutes 30 seconds
* **Audio Track Standard:** Studio narration, 48kHz / 24-bit, separate vocal channel, zero background/mouse noise.
* **Screen Resolution:** 1920x1080 at 125% IDE scale.

---

### [0:00 - 0:25] Slide 1: Title Slide
* **Visual:** Slide 1 displayed.
* **Speaker Tone:** Professional, confident, authoritative.
* **Narration:**
> "Hello everyone, and welcome! My name is [Your Name]. In this session, we’re mastering **Visual Multi-File Refactoring using the OpenAI Codex Extension in VS Code**."
> 
> *[1-second intentional pause]*
> 
> "Most code changes aren't isolated to a single file. When you update a core model or interface, the ripple effect touches controllers, services, and tests."

---

### [0:25 - 1:10] Slide 2: Overview & WIIFM
* **Visual:** Slide 2 displayed. Click bullets in sync.
* **Speaker Tone:** Conversational, motivating.
* **Narration:**
> *[Click Bullet 1]*  
> "When you have to modify three or four interdependent files, doing it by hand means switching between tabs and hoping you didn’t miss a variable name.  
> 
> *[Click Bullet 2]*  
> The Codex extension in VS Code is built specifically for synchronized multi-file editing.  
> 
> *[Click Bullet 3]*  
> In this audition, you’ll learn how to scope multi-file refactors, navigate the extension’s change review tree, and apply synchronized updates with complete confidence."

---

### [1:10 - 1:35] Slide 3: The Developer Scenario
* **Visual:** Slide 3 displayed.
* **Speaker Tone:** Relatable, problem-focused.
* **Narration:**
> "Let’s look at Alex’s situation. Alex is preparing an API for a new frontend client that expects camelCase JSON keys like `firstName` and `userRole` instead of legacy snake_case.  
> 
> This requires synchronized modifications across the Pydantic schema, the service serializer, and the API route handlers.  
> Let's see how Codex coordinates this in one cohesive operation."

---

### [1:35 - 2:05] Slide 4: Multi-File Tagging in the Codex GUI
* **Visual:** Slide 4 displayed. Animate columns.
* **Speaker Tone:** Educational, clear.
* **Narration:**
> "The Codex extension interface handles this seamlessly:  
> In the prompt box, we can tag multiple files using `#` chips.  
> Codex processes them as an interdependent unit, ensuring that variable names match across boundaries.  
> And in the extension sidebar, Codex displays a visual review tree allowing you to inspect each diff individually."

---

### [2:05 - 2:35] Slide 5: The Review Checklist Principle
* **Visual:** Slide 5 displayed (Teal accent).
* **Speaker Tone:** Authoritative, deliberate.
* **Narration:**
> "Here is our golden rule for multi-file refactors:  
> 
> *[1-second pause]*  
> 
> *'Always review your changes file-by-file in the GUI before clicking Accept All.'*  
> 
> The Codex extension gives you a dedicated file checklist. Use it to verify that interface names in your schemas match the calls in your controllers.  
> Let’s jump into VS Code."

---

### [2:35 - 2:45] Slide 6: Demo Transition
* **Visual:** Slide 6 displayed.
* **Narration:**
> "Let's switch over to VS Code and watch Alex execute a multi-file refactor live."

---

### [2:45 - 5:45] LIVE DEMO SCREENCAST (VS Code GUI)

#### Step 1: The Three Interdependent Files [2:45 - 3:25]
* **Screen:** VS Code showing 3 open tabs: `schemas/user.py`, `services/user_service.py`, `routes/user_routes.py`.
* **Visual Cue:** `[CALLOUT BOX: Highlight snake_case fields like first_name, last_name, user_role]` *(Hand off mouse; no cursor circling)*.
* **Narration:**
> "Here are our three files: `schemas/user.py`, `services/user_service.py`, and `routes/user_routes.py`. Notice that all user attributes are currently formatted in snake_case: `first_name`, `last_name`, and `user_role`. We need all three files updated in lockstep."

#### Step 2: Multi-File Tagging in the Codex Panel [3:25 - 4:10]
* **Screen:** Open the Codex extension panel on the right.
* **Action:** Paste prompt from `codex_gui_prompts.txt`:  
  `#schemas/user.py #services/user_service.py #routes/user_routes.py Refactor all user response fields from snake_case to camelCase (e.g. firstName, lastName, userRole). Ensure serializers and route responses remain synchronized.`
* **Visual Cue:** `[CALLOUT BOX: Highlight the 3 file tags in the Codex prompt box]`.
* **Narration:**
> "In the Codex panel, notice how we tag all three files: `#schemas/user.py`, `#services/user_service.py`, and `#routes/user_routes.py`.  
> 
> We instruct Codex to refactor all response fields to camelCase and ensure serializers and routes remain synchronized. Let's send the command."

#### Step 3: Navigating the File Change Tree [4:10 - 5:05]
* **Screen:** Codex processes the request and displays the "Modified Files" tree in the extension panel showing:
  * `schemas/user.py` (+4, -4)
  * `services/user_service.py` (+6, -6)
  * `routes/user_routes.py` (+2, -2)
* **Visual Cue:** `[CALLOUT BOX: Highlight the 3-file list in the Codex panel]`.
* **Narration:**
> "Watch the Codex panel: it displays a clean 'Modified Files' tree showing the exact diff count for each file.  
> 
> Let's click on `schemas/user.py` first. The editor splits into a diff view: `first_name` is cleanly mapped to `firstName` with Pydantic aliases.  
> Now let's click on `services/user_service.py` in the tree. The diff view instantly switches: the dictionary serialization keys are updated to match."

#### Step 4: Accepting All and Running Verification [5:05 - 5:45]
* **Screen:** In the Codex panel, click **Accept All Changes**.
* **Action:** Open terminal and run `pytest test_api.py`.
* **Visual Cue:** `[CALLOUT BOX: Highlight "Accept All Changes" button, then highlight passing test output in terminal]`.
* **Narration:**
> "Once we’ve verified all three files, we click the 'Accept All Changes' button right inside the Codex panel.  
> All three files are saved simultaneously.  
> 
> Now let's run our integration tests: `pytest test_api.py`.  
> All tests pass with the new camelCase response format intact!  
> 
> In less than two minutes, Alex executed a coordinated cross-file refactor without a single broken reference."

---

### [5:45 - 6:30] Slide 7: Summary & Practical Takeaways
* **Visual:** Slide 7 displayed. Click bullets in sync.
* **Speaker Tone:** Energized, closing.
* **Narration:**
> *[Click Bullet 1]*  
> "To wrap up:  
> Use `#file` tags to give Codex complete cross-file context.  
> 
> *[Click Bullet 2]*  
> Use the extension’s visual change tree to audit diffs before accepting.  
> 
> *[Click Bullet 3]*  
> And coordinate your refactors seamlessly without manual tab-juggling.  
> 
> Thank you for watching, and happy coding with OpenAI Codex!"
