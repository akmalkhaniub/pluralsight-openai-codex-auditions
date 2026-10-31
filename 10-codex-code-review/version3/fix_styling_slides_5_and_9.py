import sys
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

pptx_path = "version3/Audition Slides - Akmal Khan - Code Review v3.pptx"
prs = Presentation(pptx_path)

# ==============================================================================
# 1. FIX SLIDE 5
# ==============================================================================
slide5 = prs.slides[4]

# Shape 1: Oval 2 (💻 icon)
sp_pc = slide5.shapes[1]
sp_pc.fill.solid()
sp_pc.fill.fore_color.rgb = RGBColor(0xEB, 0xF3, 0xFB) # Soft light tech blue
p_pc = sp_pc.text_frame.paragraphs[0]
p_pc.alignment = PP_ALIGN.CENTER
p_pc.font.size = Pt(56) # Make icon large and prominent!

# Shape 4: Oval 5 (🔍 icon)
sp_search = slide5.shapes[4]
sp_search.fill.solid()
sp_search.fill.fore_color.rgb = RGBColor(0xEB, 0xF3, 0xFB) # Matching soft blue
p_search = sp_search.text_frame.paragraphs[0]
p_search.alignment = PP_ALIGN.CENTER
p_search.font.size = Pt(56) # Make icon large and prominent!

# Shape 8: Rounded Rectangle 9 ("Codex wears both hats. Never in the same prompt.")
sp_banner = slide5.shapes[8]
sp_banner.fill.solid()
sp_banner.fill.fore_color.rgb = RGBColor(0xF1, 0xF5, 0xF9) # Clean modern slate light background
sp_banner.line.color.rgb = RGBColor(0xCB, 0xD5, 0xE1) # Subtle clean border
p_banner = sp_banner.text_frame.paragraphs[0]
p_banner.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A) # Crisp black / dark charcoal text
p_banner.font.bold = True
p_banner.font.size = Pt(20)

# ==============================================================================
# 2. FIX SLIDE 9
# ==============================================================================
slide9 = prs.slides[8]

# Shape 1: Rounded Rectangle 2 ("💻 Feature Dev only")
sp_feat = slide9.shapes[1]
sp_feat.fill.solid()
sp_feat.fill.fore_color.rgb = RGBColor(0xDB, 0xEA, 0xFE) # Clean soft sky blue (looks great with black text)
sp_feat.line.color.rgb = RGBColor(0x93, 0xC5, 0xFD)
p_feat = sp_feat.text_frame.paragraphs[0]
p_feat.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A) # Pure black / dark text
p_feat.font.bold = True
p_feat.font.size = Pt(18)

# Shape 5: Rounded Rectangle 6 ("💻 + 🔍 Feature Dev + Senior Reviewer")
sp_both = slide9.shapes[5]
sp_both.fill.solid()
sp_both.fill.fore_color.rgb = RGBColor(0xDC, 0xFC, 0xE7) # Clean soft mint green (looks great with black text)
sp_both.line.color.rgb = RGBColor(0x86, 0xEF, 0xAC)
p_both = sp_both.text_frame.paragraphs[0]
p_both.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A) # Pure black / dark text
p_both.font.bold = True
p_both.font.size = Pt(18)

# Save presentation
prs.save(pptx_path)
print("SUCCESS: Slide 5 and Slide 9 styling completely revamped and polished!")
