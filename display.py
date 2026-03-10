from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont
import datetime
import config

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.hardware_mapping = "adafruit-hat"

matrix = RGBMatrix(options=options)

font = ImageFont.load_default()

def brightness():

    hour = datetime.datetime.now().hour

    if hour >= 22 or hour <= 6:
        matrix.brightness = config.NIGHT_BRIGHTNESS
    else:
        matrix.brightness = config.DAY_BRIGHTNESS

def render(lines,color):

    image = Image.new("RGB",(256,32))
    draw = ImageDraw.Draw(image)

    y=0

    for line in lines:

        draw.text((0,y),line,font=font,fill=color)
        y+=10

    return image
