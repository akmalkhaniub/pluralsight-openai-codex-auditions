import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # 16:9 widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Color Palette (Pluralsight signature dark theme)
    BG_DARK = RGBColor(27, 24, 30)         # Charcoal Dark #1B181E
    CARD_BG = RGBColor(38, 35, 43)         # Lighter Card #26232B
    ORANGE_ACCENT = RGBColor(241, 91, 42)  # Pluralsight Orange #F15B2A
    TEAL_ACCENT = RGBColor(0, 180, 216)    # Pluralsight Teal #00B4D8
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(176, 172, 186)
    BORDER_COLOR = RGBColor(60, 56, 68)

    blank_layout = prs.slide_layouts[6]

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text="OPENAI CODEX FOR DEVELOPERS"):
        # Category tracker
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.5), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = "Segoe UI"
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = ORANGE_ACCENT

        # Title
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.5), Inches(0.8))
        tf = t_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = "Segoe UI"
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

    # ==========================================
    # SLIDE 1: TITLE SLIDE
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, BG_DARK)

    # Accent bar
    bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(2.2), Inches(0.15), Inches(2.8))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ORANGE_ACCENT
    bar.line.fill.background()

    # Title box
    tb = s1.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(11.0), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "PLURALSIGHT AUDITION COURSE"
    p0.font.name = "Segoe UI"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = ORANGE_ACCENT
    p0.space_after = Pt(12)

    p1 = tf.add_paragraph()
    p1.text = "The Autonomous TDD Loop in OpenAI Codex"
    p1.font.name = "Segoe UI"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(8)

    p2 = tf.add_paragraph()
    p2.text = "From Failing Specifications to Verified Green Code in VS Code"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(20)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_after = Pt(24)

    p3 = tf.add_paragraph()
    p3.text = "Author: [Your Name]  |  Senior Software Engineer"
    p3.font.name = "Segoe UI"
    p3.font.size = Pt(14)
    p3.font.color.rgb = TEAL_ACCENT

    # ==========================================
    # SLIDE 2: OVERVIEW / WIIFM
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, BG_DARK)

    # Left accent block (Pluralsight style)
    left_block = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(3.6), prs.slide_height)
    left_block.fill.solid()
    left_block.fill.fore_color.rgb = ORANGE_ACCENT
    left_block.line.fill.background()

    left_tb = s2.shapes.add_textbox(Inches(0.4), Inches(2.5), Inches(2.8), Inches(3.0))
    left_tf = left_tb.text_frame
    left_tf.word_wrap = True
    lp1 = left_tf.paragraphs[0]
    lp1.text = "OVERVIEW"
    lp1.font.name = "Segoe UI"
    lp1.font.size = Pt(26)
    lp1.font.bold = True
    lp1.font.color.rgb = TEXT_WHITE
    lp2 = left_tf.add_paragraph()
    lp2.text = "What's in it for the learner?"
    lp2.font.name = "Segoe UI"
    lp2.font.size = Pt(16)
    lp2.font.color.rgb = RGBColor(255, 230, 220)

    # Right Content Box
    rc_box = s2.shapes.add_textbox(Inches(4.2), Inches(1.5), Inches(8.4), Inches(5.0))
    rc_tf = rc_box.text_frame
    rc_tf.word_wrap = True

    bullets = [
        ("The TDD Friction:", "Writing unit tests first guarantees reliability, but implementing repetitive boilerplate code slows down velocity."),
        ("The Codex GUI Solution:", "Pinning test specifications (#test_discounts.py) directly into the Codex extension side panel in VS Code."),
        ("Today's Goal:", "Learn to guide Codex through failing tests, review side-by-side diffs, and turn test suites green with one click.")
    ]

    for title, desc in bullets:
        bp = rc_tf.add_paragraph() if rc_tf.paragraphs[0].text else rc_tf.paragraphs[0]
        run1 = bp.add_run()
        run1.text = title + " "
        run1.font.name = "Segoe UI"
        run1.font.size = Pt(17)
        run1.font.bold = True
        run1.font.color.rgb = ORANGE_ACCENT

        run2 = bp.add_run()
        run2.text = desc
        run2.font.name = "Segoe UI"
        run2.font.size = Pt(16)
        run2.font.color.rgb = TEXT_WHITE
        bp.space_after = Pt(24)

    # ==========================================
    # SLIDE 3: TWO TEXT CHUNKING (The Scenario)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, BG_DARK)
    add_header(s3, "The Developer Scenario: Marcus's Discount Engine")

    # Left Card
    c1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = BORDER_COLOR
    c1_tf = c1.text_frame
    c1_tf.word_wrap = True
    c1_tf.margin_top = Inches(0.4)
    c1_tf.margin_left = Inches(0.4)
    c1_tf.margin_right = Inches(0.4)

    p = c1_tf.paragraphs[0]
    p.text = "THE BUSINESS SPECIFICATIONS"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ORANGE_ACCENT
    p.space_after = Pt(14)

    specs = [
        "Tier 1: 10% volume discount on orders $100 - $499.99.",
        "Tier 2: 20% volume discount on orders $500 and above.",
        "Coupon Stacking: Flat '$SAVE15' applied after tier discount.",
        "Financial Precision: All amounts rounded to 2 decimal places."
    ]
    for s in specs:
        sp = c1_tf.add_paragraph()
        sp.text = "• " + s
        sp.font.name = "Segoe UI"
        sp.font.size = Pt(14)
        sp.font.color.rgb = TEXT_WHITE
        sp.space_after = Pt(10)

    # Right Card
    c2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8))
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = BORDER_COLOR
    c2_tf = c2.text_frame
    c2_tf.word_wrap = True
    c2_tf.margin_top = Inches(0.4)
    c2_tf.margin_left = Inches(0.4)
    c2_tf.margin_right = Inches(0.4)

    p = c2_tf.paragraphs[0]
    p.text = "THE STARTING BASELINE"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = TEAL_ACCENT
    p.space_after = Pt(14)

    states = [
        "test_discounts.py: 4 comprehensive test cases written.",
        "discount_service.py: Empty skeleton file.",
        "Terminal Status: 'raise NotImplementedError' (RED FAILING).",
        "The Challenge: Implement logic without altering test assertions."
    ]
    for st in states:
        sp = c2_tf.add_paragraph()
        sp.text = "• " + st
        sp.font.name = "Segoe UI"
        sp.font.size = Pt(14)
        sp.font.color.rgb = TEXT_WHITE
        sp.space_after = Pt(10)

    # ==========================================
    # SLIDE 4: THREE TEXT CHUNKING (The GUI Workflow)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, BG_DARK)
    add_header(s4, "The 3-Step Codex GUI Workflow in VS Code")

    steps = [
        ("01", "Context Pinning", "Tag #test_discounts.py in the Codex chat panel to lock test assertions as read-only working memory."),
        ("02", "Side-by-Side Diff", "Inspect green line additions directly inside the editor diff view before any code is saved."),
        ("03", "One-Click Accept", "Click 'Accept' in the toolbar and run pytest in the integrated terminal to confirm 100% green.")
    ]

    card_width = Inches(3.64)
    gap = Inches(0.4)
    start_x = Inches(0.8)

    for i, (num, title, desc) in enumerate(steps):
        x = start_x + (i * (card_width + gap))
        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), card_width, Inches(4.8))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = BORDER_COLOR

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_top = Inches(0.4)
        ctf.margin_left = Inches(0.3)
        ctf.margin_right = Inches(0.3)

        p_num = ctf.paragraphs[0]
        p_num.text = num
        p_num.font.name = "Segoe UI"
        p_num.font.size = Pt(36)
        p_num.font.bold = True
        p_num.font.color.rgb = ORANGE_ACCENT

        p_t = ctf.add_paragraph()
        p_t.text = title
        p_t.font.name = "Segoe UI"
        p_t.font.size = Pt(18)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE
        p_t.space_after = Pt(12)

        p_d = ctf.add_paragraph()
        p_d.text = desc
        p_d.font.name = "Segoe UI"
        p_d.font.size = Pt(13)
        p_d.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 5: IMPORTANT STATEMENT (The Golden Rule)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, TEAL_ACCENT)

    stmt_box = s5.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(10.9), Inches(3.5))
    stmt_tf = stmt_box.text_frame
    stmt_tf.word_wrap = True

    sp0 = stmt_tf.paragraphs[0]
    sp0.text = "THE GOLDEN RULE OF AI-DRIVEN TDD"
    sp0.font.name = "Segoe UI"
    sp0.font.size = Pt(14)
    sp0.font.bold = True
    sp0.font.color.rgb = RGBColor(220, 245, 255)
    sp0.space_after = Pt(16)

    sp1 = stmt_tf.add_paragraph()
    sp1.text = "\"Never allow your AI assistant to modify the test suite to make it pass.\""
    sp1.font.name = "Segoe UI"
    sp1.font.size = Pt(32)
    sp1.font.bold = True
    sp1.font.color.rgb = TEXT_WHITE
    sp1.space_after = Pt(20)

    sp2 = stmt_tf.add_paragraph()
    sp2.text = "Treat your test file as an immutable behavioral contract. Pin tests as read-only context in the Codex GUI and only authorize edits to the implementation file."
    sp2.font.name = "Segoe UI"
    sp2.font.size = Pt(16)
    sp2.font.color.rgb = RGBColor(240, 252, 255)

    # ==========================================
    # SLIDE 6: DEMO TRANSITION SLIDE
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, BG_DARK)

    # Center card
    dc = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.2), Inches(1.8), Inches(8.9), Inches(4.0))
    dc.fill.solid()
    dc.fill.fore_color.rgb = CARD_BG
    dc.line.color.rgb = ORANGE_ACCENT
    dc_tf = dc.text_frame
    dc_tf.word_wrap = True
    dc_tf.margin_top = Inches(0.8)

    dp0 = dc_tf.paragraphs[0]
    dp0.alignment = PP_ALIGN.CENTER
    dp0.text = "LIVE DEMONSTRATION"
    dp0.font.name = "Segoe UI"
    dp0.font.size = Pt(14)
    dp0.font.bold = True
    dp0.font.color.rgb = ORANGE_ACCENT
    dp0.space_after = Pt(12)

    dp1 = dc_tf.add_paragraph()
    dp1.alignment = PP_ALIGN.CENTER
    dp1.text = "Driving the TDD Loop via the Codex Extension GUI"
    dp1.font.name = "Segoe UI"
    dp1.font.size = Pt(26)
    dp1.font.bold = True
    dp1.font.color.rgb = TEXT_WHITE
    dp1.space_after = Pt(14)

    dp2 = dc_tf.add_paragraph()
    dp2.alignment = PP_ALIGN.CENTER
    dp2.text = "VS Code Editor  •  Codex Side Panel  •  Side-by-Side Diff  •  Pytest Runner"
    dp2.font.name = "Segoe UI"
    dp2.font.size = Pt(15)
    dp2.font.color.rgb = TEAL_ACCENT

    # ==========================================
    # SLIDE 7: SUMMARY & PRACTICAL TAKEAWAYS
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, BG_DARK)
    add_header(s7, "Summary: Practical Takeaways")

    sum_box = s7.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
    sum_tf = sum_box.text_frame
    sum_tf.word_wrap = True

    takeaways = [
        ("Pin Tests as Context Anchors:", "Use #file in the Codex GUI prompt box so the model has exact assertions in its active window."),
        ("Enforce Test Immutability:", "Keep your test file strictly read-only so the model cannot compromise or bypass business logic edge cases."),
        ("Supervise with Visual Diffs:", "Review the side-by-side editor diff in VS Code before clicking 'Accept' to ensure zero hallucinated logic.")
    ]

    for title, desc in takeaways:
        tp = sum_tf.add_paragraph() if sum_tf.paragraphs[0].text else sum_tf.paragraphs[0]
        r1 = tp.add_run()
        r1.text = title + " "
        r1.font.name = "Segoe UI"
        r1.font.size = Pt(18)
        r1.font.bold = True
        r1.font.color.rgb = ORANGE_ACCENT

        r2 = tp.add_run()
        r2.text = desc
        r2.font.name = "Segoe UI"
        r2.font.size = Pt(16)
        r2.font.color.rgb = TEXT_WHITE
        tp.space_after = Pt(24)

    output_path = "g:/ReplitProjects/pluralsight-openai-codex-auditions/05-gui-autonomous-tdd-loop/autonomous_tdd_loop_presentation.pptx"
    prs.save(output_path)
    print(f"Successfully generated PowerPoint presentation at: {output_path}")

if __name__ == "__main__":
    create_presentation()
