import requests
import datetime
import config

def weather():

    url=f"https://api.openweathermap.org/data/2.5/weather?lat={config.LAT}&lon={config.LON}&units=metric&appid={config.OPENWEATHER_KEY}"

    r=requests.get(url)

    data=r.json()

    temp=int(data["main"]["temp"])
    desc=data["weather"][0]["main"]

    now=datetime.datetime.now()

    return [

        "Weather",
        f"{temp}C {desc}",
        now.strftime("%H:%M %d %b")

    ]
