import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tracker
import radar
import weather
import display
import airlines
from flight_api import get_route_info  # optional: dynamic O/D lookup

# Time to hold aircraft info before scrolling (seconds)
HOLD_TIME = 10

while True:
    display.brightness()

    planes = tracker.aircraft()

    if planes:
        # prepare planes with colors and labels
        plane_list = []
        for p in planes:
            airline_code = p["callsign"][:3]
            color = airlines.AIRLINES.get(airline_code,(0,255,0))
            origin,dest = get_route_info(p["callsign"])
            label = f"{p['callsign']} {origin}->{dest}"
            plane_list.append({
                "dx": p["dx"],
                "dy": p["dy"],
                "heading": p.get("heading",0),
                "label": label,
                "color": color,
                "alt": p["alt"],
                "dist": p["dist"]
            })

        # Radar sweep animation for ~3 seconds
        for _ in range(60):
            radar.radar(plane_list)
            time.sleep(0.05)

        # display aircraft info and scroll
        for p in plane_list:
            lines = [
                f"{p['label']}",
                f"{p['dist']}mi {p['alt']}ft"
            ]
            img = display.render(lines, p["color"])
            # hold info on screen
            display.matrix.SetImage(img,0,0)
            time.sleep(HOLD_TIME)
            # then scroll
            display.scroll.scroll(img)

    else:
        # No aircraft: show weather
        lines = weather.weather()
        img = display.render(lines,(0,200,255))
        display.matrix.SetImage(img,0,0)
        time.sleep(5)
        display.scroll.scroll(img)
