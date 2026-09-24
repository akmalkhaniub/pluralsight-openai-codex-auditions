# Timed Narration Script: Safe Multi-File Refactoring and Verification with OpenAI Codex

* **Target Video Length:** 7 minutes 15 seconds
* **Audio Track Standard:** Clear studio quality, 48kHz / 24-bit, separate vocal track, zero keyboard/mouse clicks.
* **Screen Resolution:** 1920x1080 at 125% IDE scale.

---

### [0:00 - 0:25] Slide 1: Title Slide
* **Visual:** Slide 1 displayed.
* **Speaker Tone:** Confident, engaging, technical.
* **Narration:**
> "Hello and welcome! My name is [Your Name]. In this session, we’re diving into **Safe Multi-File Refactoring and Verification with OpenAI Codex**."
> 
> *[1-second pause]*
> 
> "Refactoring is one of the most critical responsibilities of a software engineer, but it's also where the fear of breaking things runs highest."

---

### [0:25 - 1:15] Slide 2: Overview / WIIFM
* **Visual:** Slide 2 displayed. Click bullets in sync.
* **Speaker Tone:** Empathetic, motivating.
* **Narration:**
> *[Click Bullet 1]*  
> "We've all been there: you need to optimize a core function, but that function is imported across three different controllers and two background workers. Touching it feels like playing Jenga.  
> 
> *[Click Bullet 2]*  
> If you ask a standard AI assistant to refactor that single function, it has no awareness of the ripple effect on your callers, leaving you with broken builds and unawaited coroutines.  
> 
> *[Click Bullet 3]*  
> In this audition, you’ll learn how to use OpenAI Codex’s multi-file planning, isolated worktree editing, and sandboxed test execution to modernize complex pipelines safely and with zero regressions."

---

### [1:15 - 1:45] Slide 3: The Danger of Single-File AI Edits
* **Visual:** Slide 3 displayed. Animate columns.
* **Speaker Tone:** Problem-driven, analytical.
* **Narration:**
> "Let’s look at Sam’s challenge. Sam has a data ingestion engine in Python that reads massive CSV files into memory as a list, causing server memory spikes.  
> 
> Sam wants to convert it to an asynchronous generator.  
> But if you only refactor `engine.py`, the calling `controller.py` will immediately crash because it still expects a list instead of iterating over an async stream.  
> A true refactor is never a single-file operation."

---

### [1:45 - 2:15] Slide 4: The 3-Stage Refactoring Cycle in Codex
* **Visual:** Slide 4 displayed. Animate columns.
* **Speaker Tone:** Clear, educational.
* **Narration:**
> "OpenAI Codex handles this through a structured 3-stage refactoring cycle:  
> 
> First: **Dependency Analysis**—Codex searches for all references to the interface and constructs a multi-file modification plan.  
> Second: **Worktree Isolation**—Codex applies the synchronized edits across both the engine and its callers.  
> And Third: **Sandboxed Verification**—Codex executes your automated test suite inside its sandbox to verify that existing functionality is preserved."

---

### [2:15 - 2:45] Slide 5: The Refactoring Prompt Pattern
* **Visual:** Slide 5 displayed with code styling.
* **Speaker Tone:** Prescriptive, practical.
* **Narration:**
> "To trigger this cycle, we use a 3-part prompt structure:  
> 
> State the **Objective**: convert `DataIngestionEngine` to an async stream generator.  
> State the **Scope**: explicitly instruct Codex to update all caller sites in `controller.py`.  
> And state the **Verification Mandate**: instruct Codex to execute `pytest test_pipeline.py` and resolve any test regressions."

---

### [2:45 - 3:30] Slide 6: Important Statement
* **Visual:** Slide 6 displayed (Teal accent).
* **Speaker Tone:** Authoritative, memorable.
* **Narration:**
> "Keep this motto in mind:  
> 
> *[1-second pause]*  
> 
> *'Refactoring without automated test execution isn't modernizing—it's gambling.'*  
> 
> The true power of OpenAI Codex isn't just writing the diff; it's the execution sandbox that verifies the code works before you ever commit it.  
> 
> Let's see this in action."

---

### [3:30 - 3:45] Slide 7: Demo Transition
* **Visual:** Slide 7 displayed.
* **Narration:**
> "Let's switch over to VS Code and watch Codex perform a synchronized 3-file refactor live."

---

### [3:45 - 6:45] LIVE DEMO SCREENCAST (3:00)

#### Segment 1: The Baseline State [3:45 - 4:15]
* **Screen:** VS Code showing `engine.py`, `controller.py`, and `test_pipeline.py`.
* **Action:** Open terminal and run `pytest test_pipeline.py`.
* **Visual Cue:** `[CALLOUT BOX: Highlight 1 passed in green]` *(Hand off mouse)*.
* **Narration:**
> "Here is our starting codebase. In `engine.py`, we have a synchronous `read_records` function that loads entire datasets into memory. In `controller.py`, our handler calls this synchronously.  
> Let's run our test suite first: `pytest test_pipeline.py`. All tests pass green. This is our baseline."

#### Segment 2: Issuing the Multi-File Refactor Prompt [4:15 - 4:55]
* **Screen:** Open the Codex prompt panel.
* **Action:** Paste the multi-file refactoring prompt from `codex_prompts.txt`.
* **Visual Cue:** `[CALLOUT BOX: Highlight the prompt text]`
* **Narration:**
> "Now let's open Codex and issue our prompt:  
> *'Refactor DataIngestionEngine in engine.py to be an asynchronous generator using async/await. Update controller.py to consume the stream with async for, and adapt test_pipeline.py to run with pytest-asyncio.'*  
> Let's run the agent."

#### Segment 3: Multi-File Patching [4:55 - 5:45]
* **Screen:** Codex opens files and applies diffs sequentially.
* **Visual Cue:** `[CALLOUT BOX: Highlight engine.py -> controller.py -> test_pipeline.py diffs]`
* **Narration:**
> "Watch Codex work:  
> First, it updates `engine.py`, converting the method signature to `async def` and yielding records as a stream.  
> Next, without stopping, it moves to `controller.py`. It updates `process_upload` to be an `async def` and replaces the list loop with `async for record in engine.stream_records()`.  
> And third, it updates `test_pipeline.py` to add the `@pytest.mark.asyncio` decorator."

#### Segment 4: Sandboxed Test Execution & Self-Correction [5:45 - 6:45]
* **Screen:** Codex automatically triggers `pytest test_pipeline.py` inside the sandbox.
* **Visual Cue:** `[CALLOUT BOX: Highlight sandbox test execution and passing status]`
* **Narration:**
> "Now comes the magic: Codex automatically invokes its execution sandbox and runs `pytest`.  
> 
> Notice that on the first run, the test caught an unawaited future on line 18.  
> Codex intercepts the test failure traceback, immediately edits line 18 to add the missing `await`, and re-runs the sandbox.  
> And there it is: two tests passed, 100% green.  
> 
> In less than 90 seconds, Sam has completed a complex, multi-file asynchronous refactor with complete test verification."

---

### [6:45 - 7:15] Slide 8: Summary & Key Takeaways
* **Visual:** Slide 8 displayed. Click bullets in sync.
* **Speaker Tone:** Energized, wrapping up.
* **Narration:**
> *[Click Bullet 1]*  
> "To summarize: always approach refactoring through the lens of the complete dependency graph.  
> 
> *[Click Bullet 2]*  
> Allow OpenAI Codex to coordinate edits across interfaces, controllers, and tests simultaneously.  
> 
> *[Click Bullet 3]*  
> And always mandate sandboxed test verification so the AI proves the refactor works before you merge.  
> 
> Thank you for watching, and happy refactoring!"
