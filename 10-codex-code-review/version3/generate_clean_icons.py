import math
from PIL import Image, ImageDraw

def create_laptop_icon():
    size = 512
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Primary colors
    frame_color = (30, 41, 59, 255)   # #1E293B Dark Slate
    screen_color = (224, 242, 254, 255) # #E0F2FE Soft Ice Blue
    bracket_color = (37, 99, 235, 255) # #2563EB Royal Tech Blue
    base_color = (71, 85, 105, 255)    # #475569 Slate
    notch_color = (148, 163, 184, 255) # #94A3B8

    # 1. Screen Outer Frame (Rounded Rectangle)
    # x: 96..416, y: 110..330
    draw.rounded_rectangle([96, 110, 416, 330], radius=24, fill=frame_color)

    # 2. Screen Glass
    draw.rounded_rectangle([116, 130, 396, 310], radius=12, fill=screen_color)

    # 3. Code symbol inside screen: < / >
    # Left bracket '<'
    draw.line([(200, 180), (160, 220), (200, 260)], fill=bracket_color, width=16, joint="curve")
    # Slash '/'
    draw.line([(240, 265), (272, 175)], fill=bracket_color, width=16)
    # Right bracket '>'
    draw.line([(312, 180), (352, 220), (312, 260)], fill=bracket_color, width=16, joint="curve")

    # 4. Laptop Base
    # x: 60..452, y: 330..365
    draw.rounded_rectangle([60, 330, 452, 365], radius=14, fill=base_color)
    # Notch in middle of base
    draw.rounded_rectangle([220, 330, 292, 342], radius=6, fill=notch_color)

    img.save("version3/icon_developer.png", "PNG")
    print("Created version3/icon_developer.png")

def create_reviewer_icon():
    size = 512
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    teal_color = (13, 148, 136, 255)  # #0D9488 Teal
    glass_color = (204, 251, 241, 255) # #CCFBF1 Soft Mint Teal
    accent_color = (15, 118, 110, 255) # #0F766E
    handle_color = (30, 41, 59, 255)   # #1E293B Slate

    # Lens Circle (Outer ring)
    # Center at (210, 210), radius=120
    cx, cy, r = 210, 210, 120
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=teal_color)

    # Lens Glass (Inner circle)
    ri = 96
    draw.ellipse([cx - ri, cy - ri, cx + ri, cy + ri], fill=glass_color)

    # Checkmark inside glass (verified inspection)
    draw.line([(165, 210), (195, 240), (265, 170)], fill=accent_color, width=18, joint="curve")

    # Handle (thick rounded angled bar)
    # From (295, 295) down to (410, 410)
    draw.line([(290, 290), (415, 415)], fill=handle_color, width=42)
    # Rounded end cap for handle
    draw.ellipse([390, 390, 436, 436], fill=handle_color)

    img.save("version3/icon_reviewer.png", "PNG")
    print("Created version3/icon_reviewer.png")

if __name__ == "__main__":
    create_laptop_icon()
    create_reviewer_icon()
