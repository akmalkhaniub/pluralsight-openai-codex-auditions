from PIL import Image
import numpy as np

img = Image.open("version3/slides_png/slide_05.png")

# Crop circle 1 (around x=360..675, y=216..530)
crop1 = img.crop((360, 215, 680, 535))
crop1.save("version3/test_circle_1.png")

# Crop circle 2 (around x=1235..1555, y=216..530)
crop2 = img.crop((1235, 215, 1555, 535))
crop2.save("version3/test_circle_2.png")

print("Saved test_circle_1.png and test_circle_2.png!")

# Check if there is a black rectangle in the center of crop1:
arr1 = np.array(crop1)
# Center is around (160, 160)
print(f"Crop 1 center pixel color: {arr1[160, 160]}")
