import sys
from pptx import Presentation

pptx_path = "version3/Audition Slides - Akmal Khan - Code Review v3.pptx"
prs = Presentation(pptx_path)

# --- 1. Slide 3 (Overview) ---
slide3 = prs.slides[2]
slide3.shapes[6].text = "1  Feature Dev"
slide3.shapes[7].text = "2  Senior Reviewer"

# --- 2. Slide 4 (The PR Looks Green) ---
slide4 = prs.slides[3]
slide4.shapes[0].text = "The PR Looks Green. Would You Approve It?"
slide4.shapes[3].text = "def upload_avatar(user_id, file):"
slide4.shapes[4].text = "    destination = AVATAR_DIR / f\"{uuid4().hex}.png\""
slide4.shapes[5].text = "    with open(destination, \"wb\") as target:"
slide4.shapes[6].text = "        copyfileobj(file, target)"
slide4.shapes[7].text = "    return f\"/avatars/{destination.name}\""
slide4.shapes[13].text = "🤔 Would you approve this PR?"

# Ensure font for code shapes
for idx in [3, 4, 5, 6, 7]:
    p = slide4.shapes[idx].text_frame.paragraphs[0]
    p.font.name = "Consolas"

# --- 3. Slide 5 (Every PR Needs a Second Pair of Eyes) ---
slide5 = prs.slides[4]
slide5.shapes[0].text = "Every Pull Request Needs a Second Pair of Eyes"
slide5.shapes[1].text = "💻"
slide5.shapes[2].text = "Feature Developer"
slide5.shapes[3].text = "“Did I satisfy the ticket requirements?”"
slide5.shapes[4].text = "🔍"
slide5.shapes[5].text = "Senior PR Reviewer"
slide5.shapes[6].text = "“What breaks this in production?”"
slide5.shapes[8].text = "Codex wears both hats. Never in the same prompt."

# --- 4. Slide 8 (Roadmap) ---
slide8 = prs.slides[7]
slide8.shapes[0].text = "First the Feature Dev, then the Senior Reviewer.\nSame Codex, same app."
slide8.shapes[2].text = "Ask Codex to add profile photo upload (Feature Dev)"
slide8.shapes[4].text = "/review → uncommitted changes (Senior Reviewer)"

# --- 5. Slide 9 (The Proof) ---
slide9 = prs.slides[8]
slide9.shapes[1].text = "💻 Feature Dev only"
slide9.shapes[5].text = "💻 + 🔍 Feature Dev + Senior Reviewer"

# --- 6. Speaker Notes across all slides ---
notes_content = {
    0: (
        "AI can write code in sixty seconds. But who reviews the AI?\n\n"
        "When nobody audits the edge cases, bugs don't just slip into production—they multiply.\n\n"
        "Hi, I'm Akmal Khan, Senior Full Stack AI Architect. Today, we're unlocking the single most critical habit for working with OpenAI Codex: code review.\n\n"
        "[CLICK → Advance to Slide 2]"
    ),
    1: (
        "First, let's meet our player. OpenAI Codex isn't just a code autocomplete engine. You give it a task in plain English, and it "
        "[CLICK] reads your entire repository context, [CLICK] plans and writes the changes across files, [CLICK] runs your test suite autonomously, "
        "[CLICK] and hands you a clean diff. [CLICK] Whether in your terminal, IDE, or the standalone Codex app on Windows—it acts like an eager junior engineer on your team."
    ),
    2: (
        "[CLICK] But here's the reality check of working with AI. [CLICK] Writing code used to take hours; now Codex knocks it out in five minutes flat. "
        "[CLICK] But reviewing that generated code? That still takes thirty minutes! [CLICK] Code review is officially the new bottleneck in software development. "
        "[CLICK] Today's mission: you'll learn how to let Codex perform its own first-pass code review, so you only spend your brainpower on the risks that truly matter. "
        "[CLICK] Three quick acts: The Feature Developer, The Senior Reviewer, and The Proof."
    ),
    3: (
        "[CLICK] Here's our real-world scenario: we need a profile photo upload feature for our bookshop application. "
        "[CLICK] Codex tackles it instantly. [CLICK] It writes thirty lines of Python. Nine automated unit tests run and pass with flying colors! "
        "[CLICK] It even includes error handling for invalid image formats. "
        "[CLICK] So... would you hit Approve on this Pull Request and ship it straight to production on a Friday afternoon? "
        "[CLICK] Take a second. [CLICK] Hold that thought! "
        "[CLICK] Because unit tests only verify what you remembered to test. They never test what you completely forgot!"
    ),
    4: (
        "[CLICK] Think about why engineering teams have strict code review policies. Why don't we let developers approve their own Pull Requests? "
        "[CLICK] Because when you build a feature, your brain is in Implementation Mode: 'Did I satisfy the ticket? Are my tests green?' "
        "[CLICK] But a Senior PR Reviewer looks at that same code in Failure Mode: 'What breaks this when storage fills up or the network drops?' "
        "[CLICK] OpenAI Codex can wear both hats. But here is the golden rule: Never both in the same prompt."
    ),
    5: (
        "In the Codex app, turning Codex into your Senior Reviewer takes exactly one command. [CLICK] You type slash review right into the composer. "
        "[CLICK] Pick your scope: here, we choose Review uncommitted changes—the exact edits Codex just produced. "
        "[CLICK] Codex immediately re-analyzes the codebase, pinpointing findings directly on the offending lines, sorted by severity. "
        "[CLICK] And best of all: it doesn't touch a single line of your code yet. You remain the senior engineer in the driver's seat. "
        "[CLICK] You can review uncommitted changes or diff against a base branch. [CLICK] Today, we inspect our fresh uncommitted changes."
    ),
    6: (
        "[CLICK] When Codex flags a real architectural finding, don't let it rewrite the entire file. "
        "[CLICK] Simply hover over the exact line, click the blue plus icon, "
        "[CLICK] and drop a punchy, one-sentence directive. "
        "[CLICK] Then tell Codex: 'Address the inline comments and keep the scope minimal.' "
        "[CLICK] You get exactly one targeted fix, one focused regression test, and zero unwanted side effects. "
        "[CLICK] This is the new elite engineering habit: Build. Review. Commit. Never jump straight from Build to Commit!"
    ),
    7: (
        "[CLICK] Here is our live flight plan: [CLICK] First, Codex wears the Feature Dev hat to build the upload. "
        "[CLICK] Second, we switch hats with /review. [CLICK] Third, we pin an inline comment on the danger zone. "
        "[CLICK] And fourth, we verify the surgical fix. Let's fire up the Codex app!\n\n"
        "[SWITCH TO LIVE DEMO]"
    ),
    8: (
        "[CLICK] Look at this side-by-side verdict. [CLICK] With only the Feature Developer, our upload functioned and nine tests were green—"
        "[CLICK] but an unhandled disk-full condition was lurking to corrupt user storage. "
        "[CLICK] With the Feature Developer and the Senior Reviewer, we have the exact same feature, plus one robust regression test, "
        "[CLICK] and zero orphaned files. [CLICK] The tests were green both times. The code review made all the difference."
    ),
    9: (
        "[CLICK] Here is the one career habit to cement from this audition: "
        "[CLICK] Run /review after every Codex task, and before every single commit. "
        "[CLICK] Whenever you evaluate Codex's findings, ensure you test the three questions a Senior Reviewer always asks:\n"
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
    slide.notes_slide.notes_text_frame.text = text

prs.save(pptx_path)
print("SUCCESS: All slides, titles, code snippets, and speaker notes fully updated!")
