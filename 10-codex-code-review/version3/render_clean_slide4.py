import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

img = Image.open("version3/slides_png/slide_04.png")
arr = np.array(img)

# Let's find the vertical bounds of the code card:
# The card background color is rgb(234, 235, 240)
bg_color = (234, 235, 240)

# In the original PPTX:
# destination = AVATAR_DIR ... y=1691640 EMU (out of 6858000 EMU total slide height = 1080px)
# 1691640 / 6858000 * 1080 = 266px
# with destination.open... y=2066544 / 6858000 * 1080 = 325px
# line spacing = 374904 / 6858000 * 1080 = ~59px
# Line 3 (try:) was at 325 + 59 = 384px
# Line 4..7 were at 443px, 502px, 561px, 620px
# The card left margin is around x=135, right is around x=850.

# Let's inspect where pixels are dark below y=360 down to y=650:
# Fill from y=360 to y=660, x=130 to x=860 with bg_color!
draw = ImageDraw.Draw(img)
draw.rectangle([130, 360, 860, 660], fill=bg_color)

# Now draw: "    copyfileobj(file, target)"
font_path = "C:/Windows/Fonts/consolab.ttf" if os.path.exists("C:/Windows/Fonts/consolab.ttf") else "C:/Windows/Fonts/consola.ttf"
# In the original, font size in EMU was sz="1500" (15pt). 15pt at 96dpi is 20px, at 1080p is ~24-25px.
font = ImageFont.truetype(font_path, 25)

# Text color in slide is #33333D = (51, 51, 61)
text_color = (51, 51, 61)
# Draw line 3 at x=145, y=384
draw.text((145, 384), "    copyfileobj(file, target)", font=font, fill=text_color)

img.save("version3/slides_png/slide_04.png")
img.save("version3/slide4_preview.png")
print("Clean Slide 4 generated and saved!")
