import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

img = Image.open("version3/slides_png/slide_04.png")
arr = np.array(img)

# Find where the background of the code box is.
# In slide 4, app/profile.py is at the top of the box.
# Let's inspect coordinates around x=90..900, y=240..700
# Let's find background color of the code card:
sample_bg = arr[250, 150]
print(f"Code card background color: {sample_bg}")

# Let's check the lines of text in the card:
# Line 1: destination = AVATAR_DIR / f"{uuid4().hex}{suffix}"
# Line 2: with destination.open("xb") as target:
# Line 3:     try:
# Line 4:         copyfileobj(file, target)
# Line 5:     except Exception:
# Line 6:         destination.unlink()
# Line 7:         raise

# We want:
# Line 1: destination = AVATAR_DIR / f"{uuid4().hex}{suffix}"
# Line 2: with destination.open("xb") as target:
# Line 3:     copyfileobj(file, target)
# And the rest of the card is clean background!
