import sys
from pptx import Presentation

pptx_path = "version3/Audition Slides - Akmal Khan - Code Review v3.pptx"

notes = {
    0: (
        "AI can write code in sixty seconds. But who reviews the AI?\n\n"
        "When nobody audits the edge cases, bugs don't just slip into production—they multiply.\n\n"
        "Hi, I'm Akmal Khan, Senior Full Stack AI Architect. Today, we're unlocking the single most critical habit for working with OpenAI Codex: code review.\n\n"
        "[CLICK → Advance to Slide 2]"
    ),
    1: (
        "First, let's meet our player. OpenAI Codex isn't just a code autocomplete engine.\n\n"
        "You give it a task in plain English, and it:\n"
        "[CLICK] Reads your entire repository context,\n"
        "[CLICK] Plans and writes the changes across files,\n"
        "[CLICK] Runs your test suite autonomously,\n"
        "[CLICK] And hands you a clean diff.\n\n"
        "[CLICK] Whether in your terminal, IDE, or the standalone Codex app on Windows—it acts like an eager junior engineer on your team."
    ),
    2: (
        "[CLICK] But here's the reality check of working with AI.\n\n"
        "[CLICK] Writing code used to take hours; now Codex knocks it out in five minutes flat.\n\n"
        "[CLICK] But reviewing that generated code? That still takes thirty minutes!\n\n"
        "[CLICK] Code review is officially the new bottleneck in software development.\n\n"
        "[CLICK] Today's mission: you'll learn how to let Codex perform its own first-pass code review, so you only spend your brainpower on the risks that truly matter.\n\n"
        "[CLICK] Three quick acts: The Feature Developer, The Senior Reviewer, and The Proof."
    ),
    3: (
        "[CLICK] Here's our real-world scenario: we need a profile photo upload feature for our bookshop application.\n\n"
        "[CLICK] Codex tackles it instantly.\n\n"
        "[CLICK] It writes thirty lines of Python. Nine automated unit tests run and pass with flying colors!\n\n"
        "[CLICK] It even includes error handling for invalid image formats.\n\n"
        "[CLICK] So... would you hit Approve on this Pull Request and ship it straight to production on a Friday afternoon?\n\n"
        "[CLICK] Take a second.\n\n"
        "[CLICK] Hold that thought!\n\n"
        "[CLICK] Because unit tests only verify what you remembered to test. They never test what you completely forgot!"
    ),
    4: (
        "[CLICK] Think about why engineering teams have strict code review policies. Why don't we let developers approve their own Pull Requests?\n\n"
        "[CLICK] Because when you build a feature, your brain is in Implementation Mode:\n"
        "\"Did I satisfy the ticket? Are my tests green?\"\n\n"
        "[CLICK] But a Senior PR Reviewer looks at that same code in Failure Mode:\n"
        "\"What breaks this when storage fills up or the network drops?\"\n\n"
        "[CLICK] OpenAI Codex can wear both hats.\n"
        "But here is the golden rule: Never both in the same prompt."
    ),
    5: (
        "In the Codex app, turning Codex into your Senior Reviewer takes exactly one command.\n\n"
        "[CLICK] You type slash review right into the composer.\n\n"
        "[CLICK] Pick your scope: here, we choose Review uncommitted changes—the exact edits Codex just produced.\n\n"
        "[CLICK] Codex immediately re-analyzes the codebase, pinpointing findings directly on the offending lines, sorted by severity.\n\n"
        "[CLICK] And best of all: it doesn't touch a single line of your code yet. You remain the senior engineer in the driver's seat.\n\n"
        "[CLICK] You can review uncommitted changes or diff against a base branch. Today, we inspect our fresh uncommitted changes."
    ),
    6: (
        "[CLICK] When Codex flags a real architectural finding, don't let it rewrite the entire file.\n\n"
        "[CLICK] Simply hover over the exact line, click the blue plus icon,\n\n"
        "[CLICK] And drop a punchy, one-sentence directive.\n\n"
        "[CLICK] Then tell Codex: \"Address the inline comments and keep the scope minimal.\"\n\n"
        "[CLICK] You get exactly one targeted fix, one focused regression test, and zero unwanted side effects.\n\n"
        "[CLICK] This is the new elite engineering habit: Build. Review. Commit.\n"
        "Never jump straight from Build to Commit!"
    ),
    7: (
        "[CLICK] Here is our live flight plan:\n\n"
        "[CLICK] First, Codex wears the Feature Dev hat to build the upload.\n\n"
        "[CLICK] Second, we switch hats with /review.\n\n"
        "[CLICK] Third, we pin an inline comment on the danger zone.\n\n"
        "[CLICK] And fourth, we verify the surgical fix. Let's fire up the Codex app!\n\n"
        "[SWITCH TO LIVE DEMO]"
    ),
    8: (
        "[CLICK] Look at this side-by-side verdict.\n\n"
        "[CLICK] With only the Feature Developer, our upload functioned and nine tests were green—\n\n"
        "[CLICK] But an unhandled disk-full condition was lurking to corrupt user storage.\n\n"
        "[CLICK] With the Feature Developer and the Senior Reviewer, we have the exact same feature, plus one robust regression test,\n\n"
        "[CLICK] And zero orphaned files.\n\n"
        "[CLICK] The tests were green both times. The code review made all the difference."
    ),
    9: (
        "[CLICK] Here is the one career habit to cement from this audition:\n\n"
        "[CLICK] Run /review after every Codex task, and before every single commit.\n\n"
        "[CLICK] Whenever you evaluate Codex's findings, ensure you test the three questions a Senior Reviewer always asks:\n"
        "1. What if the operation fails halfway?\n"
        "2. Who is authorized to call this?\n"
        "3. What happens when input is empty or gigantic?"
    ),
    10: (
        "[CLICK] To wrap it all up:\n\n"
        "1. Review is your new competitive bottleneck.\n\n"
        "[CLICK] 2. Switch hats with /review before every commit.\n\n"
        "[CLICK] 3. Point at the line, and demand surgical fixes.\n\n"
        "[CLICK] And above all: Codex finds the risks, but you decide what ships to production.\n\n"
        "I'm Akmal Khan—thank you for watching."
    )
}

try:
    prs = Presentation(pptx_path)
    for idx, text in notes.items():
        prs.slides[idx].notes_slide.notes_text_frame.text = text
    prs.save(pptx_path)
    print("SUCCESS: All slide notes formatted line-by-line with teleprompter breathing room!")
except Exception as e:
    print(f"Error: {e}")
