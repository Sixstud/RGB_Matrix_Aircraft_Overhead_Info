import time
import config
import display

def scroll(image):

    width=image.size[0]

    for x in range(width):

        display.matrix.SetImage(image,-x,0)

        time.sleep(config.SCROLL_SPEED)
