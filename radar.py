import math
from PIL import Image, ImageDraw
import display

angle = 0  # radar sweep angle

def radar(planes):
    global angle

    cx, cy = 32, 16  # center of 64x32 panel
    max_radius = 14  # radius for 15 miles

    # create a new frame
    image = Image.new("RGB", (64,32))
    draw = ImageDraw.Draw(image)

    # Draw distance rings (5 / 10 / 15 miles)
    for r in [5, 10, 15]:
        pixel_r = int(r / 15 * max_radius)
        draw.ellipse((cx-pixel_r, cy-pixel_r, cx+pixel_r, cy+pixel_r), outline=(0,128,0))

    # Draw aircraft
    for p in planes:
        # position scaled to panel
        px = int(cx + p["dx"] * max_radius)
        py = int(cy + p["dy"] * max_radius)

        # aircraft blip
        draw.ellipse((px-1, py-1, px+1, py+1), fill=p.get("color",(255,0,0)))

        # heading arrow
        if "heading" in p:
            arrow_len = 3
            hx = px + arrow_len * math.cos(math.radians(p["heading"]))
            hy = py + arrow_len * math.sin(math.radians(p["heading"]))
            draw.line((px, py, hx, hy), fill=p.get("color",(255,0,0)))

        # callsign label
        if "label" in p:
            draw.text((px+2, py-2), p["label"], font=display.font, fill=p.get("color",(255,0,0)))

    # Radar sweep line
    sweep_x = cx + max_radius * math.cos(math.radians(angle))
    sweep_y = cy + max_radius * math.sin(math.radians(angle))
    draw.line((cx, cy, sweep_x, sweep_y), fill=(0,255,0))

    # Send image to the matrix
    display.matrix.SetImage(image)

    # increment sweep angle
    angle = (angle + 5) % 360
