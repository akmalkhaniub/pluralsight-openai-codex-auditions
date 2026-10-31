# Timed Narration Script: The Autonomous TDD Loop in OpenAI Codex (VS Code GUI)

* **Target Video Length:** 6 minutes 30 seconds
* **Audio Track Standard:** Clean studio narration, 48kHz / 24-bit, separate vocal channel, zero keyboard/mouse clicks.
* **Screen Resolution:** 1920x1080 at 125% IDE scale.

---

### [0:00 - 0:25] Slide 1: Title Slide
* **Visual:** Slide 1 displayed.
* **Speaker Tone:** Confident, engaging, warm.
* **Narration:**
> "Hello everyone, and welcome! My name is [Your Name]. In this session, we’re exploring **The Autonomous Test-Driven Development Loop using the OpenAI Codex Extension in VS Code**."
> 
> *[1-second intentional pause]*
> 
> "Test-Driven Development is an industry gold standard, but manually writing all the boilerplate to satisfy test assertions can slow down feature delivery."

---

### [0:25 - 1:10] Slide 2: Overview & WIIFM
* **Visual:** Slide 2 displayed. Click bullets in sync.
* **Speaker Tone:** Empathetic, motivating.
* **Narration:**
> *[Click Bullet 1]*  
> "Writing your tests before your code guarantees high reliability, but it also creates friction when you have to write dozens of lines of repetitive logic.  
> 
> *[Click Bullet 2]*  
> With the OpenAI Codex extension in VS Code, we can bridge this gap by pinning our test suite directly into the extension's side panel.  
> 
> *[Click Bullet 3]*  
> By the end of this audition, you’ll know how to reference your test suite in the Codex GUI, review generated side-by-side diffs, and turn red test suites completely green in minutes."

---

### [1:10 - 1:35] Slide 3: The Developer Scenario
* **Visual:** Slide 3 displayed.
* **Speaker Tone:** Story-driven, analytical.
* **Narration:**
> "Let’s look at our scenario. Marcus is an engineer building an e-commerce discount calculator. He has already written a suite of four thorough unit tests covering volume discounts and coupon stacking.  
> 
> If Marcus runs `pytest` right now, every single test fails because the service file is just an empty placeholder. Let’s see how Codex turns these specifications into reality."

---

### [1:35 - 2:05] Slide 4: The 3-Step Codex GUI Workflow
* **Visual:** Slide 4 displayed. Animate columns.
* **Speaker Tone:** Instructional, clear.
* **Narration:**
> "The Codex extension interface makes this workflow visual and controllable in three steps:  
> 
> First, we attach our test file as a context anchor using the hash symbol in the Codex prompt box.  
> Second, Codex displays a side-by-side visual diff in VS Code, showing exactly what it intends to add.  
> And third, we click 'Accept' and verify the tests in our terminal."

---

### [2:05 - 2:35] Slide 5: The Golden Rule of AI-Driven TDD
* **Visual:** Slide 5 displayed (Teal accent).
* **Speaker Tone:** Emphatic, authoritative.
* **Narration:**
> "Here is a critical rule when doing TDD with AI:  
> 
> *[1-second pause]*  
> 
> *'Never allow the AI to edit your test file to make it pass.'*  
> 
> In the Codex GUI, we pass the test file as read-only context and explicitly target the implementation file as the only writable surface.  
> 
> Let's see this in action."

---

### [2:35 - 2:45] Slide 6: Demo Transition
* **Visual:** Slide 6 displayed.
* **Narration:**
> "Let's switch over to VS Code and watch Marcus execute the TDD loop live in the Codex extension."

---

### [2:45 - 5:45] LIVE DEMO SCREENCAST (VS Code GUI)

#### Step 1: The Failing Baseline [2:45 - 3:20]
* **Screen:** VS Code. Left editor showing `test_discounts.py`. Bottom terminal open.
* **Action:** In terminal, run `pytest test_discounts.py`. Terminal displays **4 FAILED (Red)**.
* **Visual Cue:** `[CALLOUT BOX: Highlight "4 failed in 0.08s" in terminal]` *(Hand off mouse; no cursor circling)*.
* **Narration:**
> "Here we are inside VS Code. In our editor, we have `test_discounts.py` with four test cases testing tier thresholds and rounding logic. In the terminal below, we run pytest: all four tests fail with `NotImplementedError`. This is our red baseline."

#### Step 2: Prompting in the Codex Side Panel [3:20 - 4:05]
* **Screen:** Open the Codex extension side panel on the right.
* **Action:** Paste prompt from `codex_gui_prompts.txt`:  
  `#test_discounts.py Implement DiscountEngine in discount_service.py so all tests pass. Do not modify test_discounts.py.`
* **Visual Cue:** `[CALLOUT BOX: Highlight the #test_discounts.py tag chip in the prompt box]`.
* **Narration:**
> "Now, look at the Codex panel on the right. Notice how we reference `#test_discounts.py`. This pins the test file directly into the model's active working memory.  
> 
> We instruct Codex to implement `DiscountEngine` inside `discount_service.py` to satisfy all assertions, without touching the test file itself. Let's send the prompt."

#### Step 3: Inspecting the Side-by-Side Diff [4:05 - 5:00]
* **Screen:** Codex processes the request and opens a side-by-side diff in the VS Code editor.
* **Visual Cue:** `[CALLOUT BOX: Highlight green additions in discount_service.py]` and `[CALLOUT BOX: Highlight Accept / Reject buttons in the top right]`.
* **Narration:**
> "Look at what the extension does next: it automatically opens a visual diff directly in our editor.  
> 
> On the left is our empty file, and on the right are the green additions generated by Codex.  
> Notice how it accurately implemented the 10% tier above $100, the 20% tier above $500, and handled rounding to two decimal places.  
> In the top right corner of the editor, we have our extension controls: 'Review', 'Reject', or 'Accept'. Everything stays completely under developer supervision."

#### Step 4: Accepting & Verifying Green [5:00 - 5:45]
* **Screen:** Click the **Accept** button in the VS Code editor toolbar.
* **Action:** In the integrated terminal, re-run `pytest test_discounts.py`.
* **Visual Cue:** `[CALLOUT BOX: Highlight "4 passed in 0.02s (Green)"]`.
* **Narration:**
> "Let’s click 'Accept'. The file is saved.  
> 
> Now let's switch to our integrated terminal and re-run our test suite: `pytest test_discounts.py`.  
> 
> And look at that: 4 passed in 0.02 seconds—one hundred percent green on the very first try.  
> Marcus has just built a fully verified, production-ready discount calculator without writing boilerplate or leaving VS Code."

---

### [5:45 - 6:30] Slide 7: Summary & Practical Takeaways
* **Visual:** Slide 7 displayed. Click bullets in sync.
* **Speaker Tone:** Energized, concluding.
* **Narration:**
> *[Click Bullet 1]*  
> "To wrap up:  
> First, pin your test files directly into the Codex GUI as your behavioral contract.  
> 
> *[Click Bullet 2]*  
> Second, enforce that your test files remain immutable so the AI cannot game the assertions.  
> 
> *[Click Bullet 3]*  
> And third, always use the side-by-side visual diff in VS Code to review before you accept.  
> 
> Thank you so much for watching, and enjoy building with OpenAI Codex!"
