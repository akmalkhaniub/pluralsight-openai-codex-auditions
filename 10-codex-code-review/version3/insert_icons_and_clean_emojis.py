import os
import shutil
import win32com.client
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

pptx_path = "version3/Audition Slides - Akmal Khan - Code Review v3.pptx"
prs = Presentation(pptx_path)

# ==============================================================================
# 1. SLIDE 5: Clear emoji text from Oval 2 and Oval 5, insert crisp PNG icons
# ==============================================================================
slide5 = prs.slides[4]

# Oval 2: Developer circle
sp_circle1 = slide5.shapes[1]
sp_circle1.text = "" # Clear emoji character!
# Circle 1 coordinates: left=2286000, top=1371600, width=2011680, height=2011680
# Place icon in center: width=1.3 inches (1188720 EMU)
icon_dev_path = os.path.abspath("version3/icon_developer.png")
icon_w = Inches(1.3)
icon_h = Inches(1.3)
left1 = sp_circle1.left + (sp_circle1.width - icon_w) // 2
top1 = sp_circle1.top + (sp_circle1.height - icon_h) // 2
pic1 = slide5.shapes.add_picture(icon_dev_path, left1, top1, icon_w, icon_h)

# Oval 5: Reviewer circle
sp_circle2 = slide5.shapes[4]
sp_circle2.text = "" # Clear emoji character!
# Circle 2 coordinates: left=7863840, top=1371600
icon_rev_path = os.path.abspath("version3/icon_reviewer.png")
left2 = sp_circle2.left + (sp_circle2.width - icon_w) // 2
top2 = sp_circle2.top + (sp_circle2.height - icon_h) // 2
pic2 = slide5.shapes.add_picture(icon_rev_path, left2, top2, icon_w, icon_h)

# ==============================================================================
# 2. SLIDE 9: Clean header text without emoji characters that cause tofu squares
# ==============================================================================
slide9 = prs.slides[8]
# Shape 1: Feature Dev only
slide9.shapes[1].text = "Feature Dev only"
p1 = slide9.shapes[1].text_frame.paragraphs[0]
p1.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A) # Bold dark black
p1.font.bold = True
p1.font.size = Pt(18)

# Shape 5: Feature Dev + Senior Reviewer
slide9.shapes[5].text = "Feature Dev + Senior Reviewer"
p2 = slide9.shapes[5].text_frame.paragraphs[0]
p2.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A) # Bold dark black
p2.font.bold = True
p2.font.size = Pt(18)

prs.save(pptx_path)
print("SUCCESS: Real icons inserted into Slide 5 and clean text applied to Slide 9!")
