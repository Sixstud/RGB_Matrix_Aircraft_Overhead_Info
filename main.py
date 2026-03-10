import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import time
import tracker
import radar
import weather
import scroll
import display
import airlines

while True:

    # adjust brightness depending on time
    display.brightness()

    # get nearby aircraft
    planes = tracker.aircraft()

    if planes:

        # display radar sweep animation
        for _ in range(60):
            radar.radar(planes)
            time.sleep(0.05)

        # loop through each aircraft
        for p in planes:

            airline = p["callsign"][:3]
            color = airlines.AIRLINES.get(airline, (0, 255, 0))

            lines = [
                p["callsign"],
                f"{p['dist']}mi",
                f"{p['alt']}ft"
            ]

            # render image
            img = display.render(lines, color)

            # display aircraft info on screen for 10 seconds
            display.matrix.SetImage(img, 0, 0)
            time.sleep(10)

            # then scroll it across the screen
            scroll.scroll(img)

    else:
        # no aircraft nearby: show weather info
        lines = weather.weather()
        img = display.render(lines, (0, 200, 255))

        # hold on screen for a few seconds before scrolling
        display.matrix.SetImage(img, 0, 0)
        time.sleep(5)

        scroll.scroll(img)
