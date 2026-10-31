import sys
from pptx import Presentation

sys.stdout.reconfigure(encoding='utf-8')
prs = Presentation('version3/Audition Slides - Akmal Khan - Code Review v3.pptx')

print("--- SLIDE 4 SHAPES ---")
for i, s in enumerate(prs.slides[3].shapes):
    if s.has_text_frame:
        print(f"Shape {i} ({s.name}): {repr(s.text[:50])}")

print("\n--- SLIDE 5 SHAPES ---")
for i, s in enumerate(prs.slides[4].shapes):
    if s.has_text_frame:
        print(f"Shape {i} ({s.name}): {repr(s.text[:50])}")

print("\n--- SLIDE 9 SHAPES ---")
for i, s in enumerate(prs.slides[8].shapes):
    if s.has_text_frame:
        print(f"Shape {i} ({s.name}): {repr(s.text[:50])}")
