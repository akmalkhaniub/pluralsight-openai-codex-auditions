import sys
from pptx import Presentation

pptx_path = "version3/Audition Slides - Akmal Khan - Code Review v3.pptx"
try:
    prs = Presentation(pptx_path)
    slide1 = prs.slides[0]
    slide1.notes_slide.notes_text_frame.text = (
        "AI can write code in sixty seconds. But who reviews the AI?\n\n"
        "When nobody audits the edge cases, bugs don't just slip into production—they multiply.\n\n"
        "Hi, I'm Akmal Khan, Senior Full Stack AI Architect. Today, we're unlocking the single most critical habit for working with OpenAI Codex: code review.\n\n"
        "[CLICK → Advance to Slide 2]"
    )
    prs.save(pptx_path)
    print("Slide 1 speaker notes updated cleanly!")
except Exception as e:
    print(f"Notice: {e}")
