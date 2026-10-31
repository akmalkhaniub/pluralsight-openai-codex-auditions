import sys
from pptx import Presentation

pptx_path = "version3/Audition Slides - Akmal Khan - Code Review v3.pptx"
prs = Presentation(pptx_path)

notes_content = {
    0: (
        "AI coding agents can build features, generate unit tests, and touch multiple files in under sixty seconds. It feels like pure magic.\n\n"
        "[CLICK] But here is the critical question every engineering team is facing right now: Who reviews the AI?\n\n"
        "Because when AI writes the code, and nobody audits the edge cases... bugs don't just slip into production—they multiply.\n\n"
        "[CLICK] Hi, I'm Akmal Khan, Senior Full Stack AI Architect. Today, we're unlocking the single most critical developer habit for the agentic era: code review inside OpenAI Codex."
    ),
    1: (
        "First, let's meet our player. OpenAI Codex isn't just an autocomplete snippet engine. You give it a task in plain English, and it "
        "[CLICK] reads your entire repository context, [CLICK] plans and writes the changes, [CLICK] runs your test suite autonomously, "
        "[CLICK] and hands you a clean diff. [CLICK] Whether in your terminal, IDE, or the standalone Codex app on Windows—it acts like an eager junior engineer on your team."
    ),
    2: (
        "[CLICK] But here's the reality check of working with AI. [CLICK] Writing code used to take hours; now Codex knocks it out in five minutes flat. "
        "[CLICK] But reviewing that generated code? That still takes thirty minutes! [CLICK] Code review is officially the new bottleneck in software development. "
        "[CLICK] Today's mission: you'll learn how to let Codex perform its own first-pass review, so you only spend your brainpower on the risks that truly matter. "
        "[CLICK] Three quick acts: The Writer, The Editor, and The Proof."
    ),
    3: (
        "[CLICK] Here's our real-world scenario: we need a profile photo upload feature for our bookshop application. "
        "[CLICK] Codex tackles it instantly. [CLICK] It writes thirty lines of Python. Nine automated unit tests run and pass with flying colors! "
        "[CLICK] It even includes error handling for invalid image formats. "
        "[CLICK] So... would you hit Merge and push this straight to production on a Friday afternoon? "
        "[CLICK] Take a second. [CLICK] Hold that thought! "
        "[CLICK] Because unit tests only verify what you remembered to ask for. They can never test what you completely forgot!"
    ),
    4: (
        "[CLICK] Think about world-class authors. Ernest Hemingway never sent his raw first draft straight to the printing press! "
        "[CLICK] Why? Because the Writer's brain is laser-focused on one question: 'Did I build what was asked?' "
        "[CLICK] But the Editor asks a completely ruthless question: 'What could break this in production?' "
        "[CLICK] OpenAI Codex can wear both hats. But here is the golden rule: Never both at the same time."
    ),
    5: (
        "In the Codex app, changing hats takes exactly one command. [CLICK] You type slash review right into the composer. "
        "[CLICK] Pick your scope: here, we choose Review uncommitted changes—the exact edits Codex just produced. "
        "[CLICK] Codex immediately re-analyzes the codebase, pinpointing findings directly on the offending lines, sorted by severity. "
        "[CLICK] And best of all: it doesn't touch a single line of your code yet. You remain the senior engineer in the driver's seat. "
        "[CLICK] You can review uncommitted changes or diff against a base branch. [CLICK] Today, we inspect our fresh uncommitted changes."
    ),
    6: (
        "[CLICK] When Codex flags a real finding, don't let it rewrite the entire file. "
        "[CLICK] Simply hover over the exact line, click the blue plus icon, "
        "[CLICK] and drop a punchy, one-sentence comment. "
        "[CLICK] Then tell Codex: 'Address the inline comments and keep the scope minimal.' "
        "[CLICK] You get exactly one targeted fix, one focused regression test, and zero unwanted side effects. "
        "[CLICK] This is the new elite engineering habit: Build. Review. Commit. Never jump straight from Build to Commit!"
    ),
    7: (
        "[CLICK] Here is our live flight plan: [CLICK] First, Codex wears the Writer hat to build the upload. "
        "[CLICK] Second, we switch hats with /review. [CLICK] Third, we pin an inline comment on the danger zone. "
        "[CLICK] And fourth, we verify the surgical fix. Let's fire up the Codex app!\n\n"
        "[SWITCH TO CODEX APP DEMO]"
    ),
    8: (
        "[CLICK] Look at this side-by-side verdict. [CLICK] With only the Writer, our upload functioned and nine tests were green—"
        "[CLICK] but an unhandled disk-full condition was lurking to corrupt user storage. "
        "[CLICK] With the Writer and the Editor, we have the exact same feature, plus one robust regression test, "
        "[CLICK] and zero orphaned files. [CLICK] The tests were green both times. The code review made all the difference."
    ),
    9: (
        "[CLICK] Here is the one career habit to cement from this audition: "
        "[CLICK] Run /review after every Codex task, and before every single commit. "
        "[CLICK] Whenever you evaluate Codex's findings, ensure you test the three questions the Editor always asks:\n"
        "1. What if the operation fails halfway?\n"
        "2. Who is authorized to call this?\n"
        "3. What happens when input is empty or gigantic?"
    ),
    10: (
        "[CLICK] To wrap it all up:\n"
        "1. Review is your new competitive bottleneck.\n"
        "[CLICK] 2. Switch hats with /review before every commit.\n"
        "[CLICK] 3. Point at the line, and demand surgical fixes.\n"
        "[CLICK] And above all: Codex finds the risks, but you decide what ships to production.\n\n"
        "I'm Akmal Khan—thank you for watching."
    )
}

for idx, text in notes_content.items():
    slide = prs.slides[idx]
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = text
    print(f"Slide {idx + 1} notes updated successfully.")

prs.save(pptx_path)
print("All 11 slides successfully updated with the v3 timed narration script!")
