from PIL import Image,ImageDraw
import math
import display

angle=0

def radar(planes):

    global angle

    image=Image.new("RGB",(64,32))
    draw=ImageDraw.Draw(image)

    cx=32
    cy=16
    r=14

    draw.ellipse((cx-r,cy-r,cx+r,cy+r),outline=(0,255,0))

    for p in planes:

        px=int(cx+(p["dx"]*r))
        py=int(cy+(p["dy"]*r))

        draw.rectangle((px,py,px+1,py+1),fill=(255,0,0))

    x=cx+r*math.cos(math.radians(angle))
    y=cy+r*math.sin(math.radians(angle))

    draw.line((cx,cy,x,y),fill=(0,255,0))

    display.matrix.SetImage(image)

    angle=(angle+8)%360
