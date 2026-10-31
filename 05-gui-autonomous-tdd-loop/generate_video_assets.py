import os
import subprocess
import json
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
OUTPUT_DIR = "g:/ReplitProjects/pluralsight-openai-codex-auditions/05-gui-autonomous-tdd-loop"
FRAMES_DIR = os.path.join(OUTPUT_DIR, "video_frames")
AUDIO_DIR = os.path.join(OUTPUT_DIR, "video_audio")
os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)

# 1920x1080 Full HD
WIDTH, HEIGHT = 1920, 1080

# Colors (Pluralsight palette)
BG_DARK = (27, 24, 30)         # #1B181E
CARD_BG = (38, 35, 43)         # #26232B
ORANGE = (241, 91, 42)         # #F15B2A
TEAL = (0, 180, 216)           # #00B4D8
WHITE = (255, 255, 255)
MUTED = (176, 172, 186)
BORDER = (60, 56, 68)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
TERMINAL_BG = (15, 13, 18)

# Load fonts
try:
    font_cat = ImageFont.truetype("segoeui.ttf", 24)
    font_title = ImageFont.truetype("segoeuib.ttf", 52)
    font_subtitle = ImageFont.truetype("segoeui.ttf", 32)
    font_card_title = ImageFont.truetype("segoeuib.ttf", 28)
    font_body = ImageFont.truetype("segoeui.ttf", 26)
    font_small = ImageFont.truetype("segoeui.ttf", 22)
    font_code = ImageFont.truetype("consola.ttf", 24)
    font_code_bold = ImageFont.truetype("consolab.ttf", 26)
except Exception:
    font_cat = ImageFont.load_default()
    font_title = font_cat
    font_subtitle = font_cat
    font_card_title = font_cat
    font_body = font_cat
    font_small = font_cat
    font_code = font_cat
    font_code_bold = font_cat

def draw_header(draw, title, category="OPENAI CODEX FOR DEVELOPERS"):
    draw.text((120, 80), category.upper(), font=font_cat, fill=ORANGE)
    draw.text((120, 120), title, font=font_title, fill=WHITE)

def synthesize_audio(text, output_wav):
    """Uses Windows PowerShell SAPI SpeechSynthesizer to generate clean WAV audio."""
    # Escape quotes
    clean_text = text.replace('"', '""').replace("'", "''")
    ps_cmd = f"""
    Add-Type -AssemblyName System.Speech
    $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $synth.SelectVoice("Microsoft David Desktop")
    $synth.Rate = 0
    $synth.SetOutputToWaveFile('{output_wav}')
    $synth.Speak("{clean_text}")
    $synth.Dispose()
    """
    subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], check=True)

# Generate Slide 1: Title
def render_slide_1():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    # Orange vertical accent
    draw.rectangle([(120, 320), (140, 720)], fill=ORANGE)
    draw.text((180, 330), "PLURALSIGHT AUDITION COURSE", font=font_cat, fill=ORANGE)
    draw.text((180, 390), "The Autonomous TDD Loop in OpenAI Codex", font=font_title, fill=WHITE)
    draw.text((180, 480), "From Failing Specifications to Verified Green Code in VS Code", font=font_subtitle, fill=MUTED)
    draw.text((180, 580), "Author: Senior Software Engineer  |  Focus: VS Code Codex Extension GUI", font=font_small, fill=TEAL)
    path = os.path.join(FRAMES_DIR, "slide_1.png")
    img.save(path)
    return path

# Generate Slide 2: Overview / WIIFM
def render_slide_2():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    # Left split block
    draw.rectangle([(0, 0), (450, HEIGHT)], fill=ORANGE)
    draw.text((80, 420), "OVERVIEW", font=font_title, fill=WHITE)
    draw.text((80, 490), "What's in it for the learner?", font=font_subtitle, fill=(255, 230, 220))
    # Right bullets
    y = 260
    bullets = [
        ("The TDD Friction:", "Writing unit tests first guarantees reliability, but implementing repetitive boilerplate slows down velocity."),
        ("The Codex GUI Solution:", "Pinning test specifications (#test_discounts.py) directly into the Codex extension side panel in VS Code."),
        ("Today's Goal:", "Learn to guide Codex through failing tests, review side-by-side diffs, and turn test suites green with one click.")
    ]
    for b_title, b_desc in bullets:
        draw.text((540, y), b_title, font=font_card_title, fill=ORANGE)
        # Word wrap desc
        draw.text((540, y + 40), b_desc, font=font_body, fill=WHITE)
        y += 180
    path = os.path.join(FRAMES_DIR, "slide_2.png")
    img.save(path)
    return path

# Generate Slide 3: Scenario
def render_slide_3():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "The Developer Scenario: Marcus's Discount Engine")
    # Left Card
    draw.rounded_rectangle([(120, 260), (920, 920)], radius=16, fill=CARD_BG, outline=BORDER, width=2)
    draw.text((160, 300), "THE BUSINESS SPECIFICATIONS", font=font_card_title, fill=ORANGE)
    specs = [
        "Tier 1: 10% volume discount on orders $100 - $499.99.",
        "Tier 2: 20% volume discount on orders $500 and above.",
        "Coupon Stacking: Flat '$SAVE15' applied after tier discount.",
        "Financial Precision: All amounts rounded to 2 decimal places."
    ]
    sy = 370
    for s in specs:
        draw.text((160, sy), "• " + s, font=font_body, fill=WHITE)
        sy += 110

    # Right Card
    draw.rounded_rectangle([(1000, 260), (1800, 920)], radius=16, fill=CARD_BG, outline=BORDER, width=2)
    draw.text((1040, 300), "THE STARTING BASELINE", font=font_card_title, fill=TEAL)
    states = [
        "test_discounts.py: 4 comprehensive test cases written.",
        "discount_service.py: Empty skeleton placeholder.",
        "Terminal Status: 'raise NotImplementedError' (RED FAILING).",
        "The Challenge: Implement logic without altering test assertions."
    ]
    sy = 370
    for st in states:
        draw.text((1040, sy), "• " + st, font=font_body, fill=WHITE)
        sy += 110

    path = os.path.join(FRAMES_DIR, "slide_3.png")
    img.save(path)
    return path

# Generate Slide 4: 3-Step GUI Workflow
def render_slide_4():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "The 3-Step Codex GUI Workflow in VS Code")
    steps = [
        ("01", "Context Pinning", "Tag #test_discounts.py in the Codex chat panel to lock assertions as read-only working memory."),
        ("02", "Side-by-Side Diff", "Inspect green line additions directly inside the editor diff view before saving."),
        ("03", "One-Click Accept", "Click 'Accept' in the toolbar and run pytest in the terminal to confirm 100% green.")
    ]
    x = 120
    card_w = 520
    for num, title, desc in steps:
        draw.rounded_rectangle([(x, 260), (x + card_w, 920)], radius=16, fill=CARD_BG, outline=BORDER, width=2)
        draw.text((x + 40, 310), num, font=font_title, fill=ORANGE)
        draw.text((x + 40, 400), title, font=font_card_title, fill=WHITE)
        # Wrap desc
        draw.text((x + 40, 470), desc, font=font_body, fill=MUTED)
        x += card_w + 40
    path = os.path.join(FRAMES_DIR, "slide_4.png")
    img.save(path)
    return path

# Generate Slide 5: Golden Rule
def render_slide_5():
    img = Image.new("RGB", (WIDTH, HEIGHT), TEAL)
    draw = ImageDraw.Draw(img)
    draw.text((140, 240), "THE GOLDEN RULE OF AI-DRIVEN TDD", font=font_card_title, fill=(220, 245, 255))
    draw.text((140, 320), "\"Never allow your AI assistant to modify the test suite to make it pass.\"", font=font_title, fill=WHITE)
    draw.text((140, 470), "Treat your test file as an immutable behavioral contract. Pin tests as read-only context in the Codex GUI,", font=font_subtitle, fill=WHITE)
    draw.text((140, 520), "and only authorize edits to the implementation file.", font=font_subtitle, fill=WHITE)
    path = os.path.join(FRAMES_DIR, "slide_5.png")
    img.save(path)
    return path

# Generate Slide 6: Demo Transition
def render_slide_6():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([(300, 280), (1620, 800)], radius=20, fill=CARD_BG, outline=ORANGE, width=3)
    draw.text((780, 350), "LIVE DEMONSTRATION", font=font_card_title, fill=ORANGE)
    draw.text((440, 430), "Driving the TDD Loop via the Codex Extension GUI", font=font_title, fill=WHITE)
    draw.text((560, 550), "VS Code Editor  •  Codex Side Panel  •  Diff Viewer  •  Pytest Runner", font=font_subtitle, fill=TEAL)
    path = os.path.join(FRAMES_DIR, "slide_6.png")
    img.save(path)
    return path

# Generate Demo Frame 1: Red failing test in VS Code
def render_demo_frame_1():
    img = Image.new("RGB", (WIDTH, HEIGHT), (20, 18, 24))
    draw = ImageDraw.Draw(img)
    # VS Code Title bar
    draw.rectangle([(0, 0), (WIDTH, 45)], fill=(30, 28, 36))
    draw.text((40, 10), "Visual Studio Code - discount_service.py - pluralsight-audition", font=font_small, fill=MUTED)

    # Editor area (test_discounts.py)
    draw.rectangle([(50, 60), (1350, 650)], fill=(24, 22, 30))
    draw.text((70, 75), "test_discounts.py", font=font_card_title, fill=WHITE)
    code_lines = [
        "1  import pytest",
        "2  from discount_service import DiscountEngine",
        "3  ",
        "4  def test_tier_one_volume_discount():",
        "5      engine = DiscountEngine()",
        "6      result = engine.calculate_discount(order_amount=250.00)",
        "7      assert result['discount_amount'] == 25.00",
        "8      assert result['applied_tier'] == 'TIER_1_10_PERCENT'",
        "9  ",
        "10 def test_coupon_stacking_and_rounding():",
        "11     engine = DiscountEngine()",
        "12     result = engine.calculate_discount(order_amount=150.00, coupon_code='SAVE15')",
        "13     assert result['discount_amount'] == 30.00"
    ]
    cy = 130
    for l in code_lines:
        draw.text((70, cy), l, font=font_code, fill=(210, 205, 225))
        cy += 36

    # Codex Panel on right
    draw.rectangle([(1360, 60), (WIDTH, HEIGHT)], fill=(28, 25, 34))
    draw.text((1380, 80), "OPENAI CODEX", font=font_card_title, fill=ORANGE)
    draw.rectangle([(1380, 130), (1890, 800)], fill=(20, 18, 24), outline=BORDER)
    draw.text((1400, 150), "Codex Ready. Type a prompt...", font=font_body, fill=MUTED)

    # Terminal bottom
    draw.rectangle([(50, 670), (1350, HEIGHT - 20)], fill=TERMINAL_BG, outline=BORDER)
    draw.text((70, 685), "TERMINAL - pytest test_discounts.py", font=font_small, fill=TEAL)
    term_lines = [
        "$ pytest test_discounts.py",
        "FAILED test_discounts.py::test_no_discount_under_threshold - NotImplementedError",
        "FAILED test_discounts.py::test_tier_one_volume_discount - NotImplementedError",
        "FAILED test_discounts.py::test_tier_two_volume_discount - NotImplementedError",
        "FAILED test_discounts.py::test_coupon_stacking_and_rounding - NotImplementedError",
        "========================= 4 FAILED in 0.08s ========================="
    ]
    ty = 730
    for tl in term_lines:
        c = RED if "FAILED" in tl else WHITE
        draw.text((70, ty), tl, font=font_code_bold, fill=c)
        ty += 34

    # Post-production CALLOUT BOX around terminal failure
    draw.rectangle([(60, 760), (1340, 950)], outline=ORANGE, width=4)
    draw.text((1050, 780), "[CALLOUT: 4 FAILED (Red)]", font=font_small, fill=ORANGE)

    path = os.path.join(FRAMES_DIR, "demo_1.png")
    img.save(path)
    return path

# Generate Demo Frame 2: Prompting in Codex side panel with #test_discounts.py pinned
def render_demo_frame_2():
    img = Image.new("RGB", (WIDTH, HEIGHT), (20, 18, 24))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (WIDTH, 45)], fill=(30, 28, 36))
    draw.text((40, 10), "Visual Studio Code - discount_service.py - pluralsight-audition", font=font_small, fill=MUTED)

    # Editor area
    draw.rectangle([(50, 60), (1200, HEIGHT - 20)], fill=(24, 22, 30))
    draw.text((70, 75), "discount_service.py (Empty baseline)", font=font_card_title, fill=WHITE)
    draw.text((70, 140), "class DiscountEngine:", font=font_code, fill=WHITE)
    draw.text((100, 180), "def calculate_discount(self, order_amount, coupon_code=None):", font=font_code, fill=WHITE)
    draw.text((140, 220), "raise NotImplementedError('Not implemented')", font=font_code, fill=RED)

    # Codex Panel on right
    draw.rectangle([(1210, 60), (WIDTH, HEIGHT)], fill=(28, 25, 34))
    draw.text((1240, 80), "OPENAI CODEX", font=font_card_title, fill=ORANGE)

    # Pinned Prompt Box
    draw.rectangle([(1230, 130), (1890, 420)], fill=(20, 18, 24), outline=TEAL, width=3)
    draw.rectangle([(1245, 145), (1480, 185)], fill=TEAL)
    draw.text((1255, 150), "#test_discounts.py", font=font_small, fill=WHITE)
    draw.text((1245, 210), "Implement DiscountEngine in", font=font_body, fill=WHITE)
    draw.text((1245, 250), "discount_service.py so all test cases", font=font_body, fill=WHITE)
    draw.text((1245, 290), "pass. Do not modify test_discounts.py.", font=font_body, fill=WHITE)

    # Callout around the pinned chip
    draw.rectangle([(1220, 120), (1900, 430)], outline=ORANGE, width=4)
    draw.text((1500, 370), "[CALLOUT: Pinned Context]", font=font_small, fill=ORANGE)

    path = os.path.join(FRAMES_DIR, "demo_2.png")
    img.save(path)
    return path

# Generate Demo Frame 3: Side-by-side diff in VS Code editor
def render_demo_frame_3():
    img = Image.new("RGB", (WIDTH, HEIGHT), (20, 18, 24))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (WIDTH, 45)], fill=(30, 28, 36))
    draw.text((40, 10), "Visual Studio Code - Working Tree Diff: discount_service.py", font=font_small, fill=MUTED)

    # Split editor
    # Left: Old
    draw.rectangle([(50, 60), (700, HEIGHT - 20)], fill=(24, 22, 30))
    draw.text((70, 75), "discount_service.py (Original)", font=font_card_title, fill=MUTED)
    draw.text((70, 140), "- raise NotImplementedError()", font=font_code, fill=RED)

    # Right: New Green Additions
    draw.rectangle([(710, 60), (1500, HEIGHT - 20)], fill=(22, 28, 24))
    draw.text((730, 75), "discount_service.py (Codex Diff: +32 lines)", font=font_card_title, fill=GREEN)
    new_code = [
        "+ class DiscountEngine:",
        "+     def calculate_discount(self, order_amount, coupon_code=None):",
        "+         discount = 0.0",
        "+         tier = 'NONE'",
        "+         if order_amount >= 500.0:",
        "+             discount = order_amount * 0.20",
        "+             tier = 'TIER_2_20_PERCENT'",
        "+         elif order_amount >= 100.0:",
        "+             discount = order_amount * 0.10",
        "+             tier = 'TIER_1_10_PERCENT'",
        "+         if coupon_code == 'SAVE15':",
        "+             discount += 15.0",
        "+         final = round(order_amount - discount, 2)",
        "+         return {'discount_amount': round(discount, 2),",
        "+                 'final_amount': final,",
        "+                 'applied_tier': tier}"
    ]
    ny = 140
    for nl in new_code:
        draw.text((730, ny), nl, font=font_code, fill=GREEN)
        ny += 38

    # Accept / Reject buttons in top right
    draw.rectangle([(1520, 80), (1890, 150)], fill=CARD_BG, outline=ORANGE, width=3)
    draw.rectangle([(1540, 95), (1700, 135)], fill=GREEN)
    draw.text((1560, 102), "✓ Accept", font=font_card_title, fill=WHITE)
    draw.rectangle([(1720, 95), (1870, 135)], fill=(80, 30, 30))
    draw.text((1740, 102), "✕ Reject", font=font_card_title, fill=WHITE)
    draw.text((1520, 170), "[CALLOUT: Accept Diff]", font=font_small, fill=ORANGE)

    path = os.path.join(FRAMES_DIR, "demo_3.png")
    img.save(path)
    return path

# Generate Demo Frame 4: Accepted & 100% Green pytest in terminal
def render_demo_frame_4():
    img = Image.new("RGB", (WIDTH, HEIGHT), (20, 18, 24))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (WIDTH, 45)], fill=(30, 28, 36))
    draw.text((40, 10), "Visual Studio Code - discount_service.py - [SAVED]", font=font_small, fill=MUTED)

    # Editor area
    draw.rectangle([(50, 60), (1350, 550)], fill=(24, 22, 30))
    draw.text((70, 75), "discount_service.py (Active & Saved)", font=font_card_title, fill=WHITE)
    draw.text((70, 130), "class DiscountEngine: ... [Implementation Complete]", font=font_code, fill=GREEN)

    # Terminal bottom
    draw.rectangle([(50, 580), (1890, HEIGHT - 20)], fill=TERMINAL_BG, outline=BORDER)
    draw.text((70, 600), "TERMINAL - pytest test_discounts.py", font=font_small, fill=TEAL)
    term_lines = [
        "$ pytest test_discounts.py",
        "rootdir: G:/ReplitProjects/pluralsight-openai-codex-auditions/05-gui-autonomous-tdd-loop",
        "collected 4 items",
        "",
        "test_discounts.py ....                                                   [100%]",
        "",
        "========================= 4 PASSED in 0.02s ========================="
    ]
    ty = 650
    for tl in term_lines:
        c = GREEN if "PASSED" in tl else WHITE
        draw.text((70, ty), tl, font=font_code_bold, fill=c)
        ty += 38

    # Callout around 4 passed
    draw.rectangle([(60, 830), (1400, 980)], outline=GREEN, width=4)
    draw.text((1050, 850), "[CALLOUT: 4 PASSED (100% GREEN)]", font=font_small, fill=GREEN)

    path = os.path.join(FRAMES_DIR, "demo_4.png")
    img.save(path)
    return path

# Generate Slide 7: Summary & Practical Takeaways
def render_slide_7():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)
    draw_header(draw, "Summary: Practical Takeaways")
    y = 260
    takeaways = [
        ("Pin Tests as Context Anchors:", "Use #file in the Codex GUI prompt box so the model has exact assertions in its active window."),
        ("Enforce Test Immutability:", "Keep your test file strictly read-only so the model cannot compromise or bypass business logic edge cases."),
        ("Supervise with Visual Diffs:", "Review the side-by-side editor diff in VS Code before clicking 'Accept' to ensure zero hallucinated logic.")
    ]
    for t_title, t_desc in takeaways:
        draw.text((120, y), t_title, font=font_card_title, fill=ORANGE)
        draw.text((120, y + 45), t_desc, font=font_body, fill=WHITE)
        y += 180
    path = os.path.join(FRAMES_DIR, "slide_7.png")
    img.save(path)
    return path

print("Rendering video asset frames...")
s1 = render_slide_1()
s2 = render_slide_2()
s3 = render_slide_3()
s4 = render_slide_4()
s5 = render_slide_5()
s6 = render_slide_6()
d1 = render_demo_frame_1()
d2 = render_demo_frame_2()
d3 = render_demo_frame_3()
d4 = render_demo_frame_4()
s7 = render_slide_7()
print("All frames rendered successfully.")
