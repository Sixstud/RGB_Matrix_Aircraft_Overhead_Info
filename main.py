import time
import tracker
import radar
import weather
import scroll
import display
import airlines

while True:

    display.brightness()

    planes=tracker.aircraft()

    if len(planes)>0:

        for i in range(60):

            radar.radar(planes)

            time.sleep(0.05)

        for p in planes:

            airline=p["callsign"][:3]

            color=airlines.AIRLINES.get(airline,(0,255,0))

            lines=[

                p["callsign"],
                f"{p['dist']}mi",
                f"{p['alt']}ft"

            ]

            img=display.render(lines,color)

            scroll.scroll(img)

    else:

        lines=weather.weather()

        img=display.render(lines,(0,200,255))

        scroll.scroll(img)

        time.sleep(5)
