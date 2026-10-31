import cv2
from PIL import Image, ImageDraw, ImageFont

img = Image.open("version3/slides_png/slide_04.png")
w, h = img.size
print(f"Slide 4 size: {w}x{h}")

# The code box is on the left side of Slide 4.
# Let's crop around the code area and find the exact coordinates.
# Typical slide layout:
# Top: Title "Codex built it. The tests pass. Ship it?"
# Left: code block with background #F4F4F6 or similar
# Let's inspect pixel colors around x=100..800, y=200..700
crop = img.crop((80, 200, 950, 750))
crop.save("version3/slide4_crop.png")
print("Saved slide4_crop.png")
