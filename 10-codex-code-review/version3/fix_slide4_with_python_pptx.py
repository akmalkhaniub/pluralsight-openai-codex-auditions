import sys
from pptx import Presentation

sys.stdout.reconfigure(encoding='utf-8')
prs = Presentation("version2/Audition Slides - Akmal Khan - Code Review v2.pptx")
slide4 = prs.slides[3] # Slide 4

# Shape 5 was '    try:'
# We set Shape 5 to '    copyfileobj(file, target)'
slide4.shapes[5].text = "    copyfileobj(file, target)"

# Shapes 6, 7, 8, 9 are emptied
slide4.shapes[6].text = ""
slide4.shapes[7].text = ""
slide4.shapes[8].text = ""
slide4.shapes[9].text = ""

# Make sure the font style matches Consolas
p = slide4.shapes[5].text_frame.paragraphs[0]
p.font.name = "Consolas"

out_pptx = "version3/Audition Slides - Akmal Khan - Code Review v3.pptx"
prs.save(out_pptx)
print("Saved cleanly with python-pptx!")
