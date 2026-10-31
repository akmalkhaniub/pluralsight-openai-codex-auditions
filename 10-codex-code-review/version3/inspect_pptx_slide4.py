import pptx
from pptx import Presentation

prs = Presentation('version3/Audition Slides - Akmal Khan - Code Review v3.pptx')
slide4 = prs.slides[3] # 0-indexed slide 4
print(f"Slide 4 shape count: {len(slide4.shapes)}")
for i, shape in enumerate(slide4.shapes):
    if shape.has_text_frame:
        print(f"Shape {i} ({shape.name}): {repr(shape.text[:50])}")
