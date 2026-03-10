import requests
import math
import config

def distance(lat1,lon1,lat2,lon2):

    R=6371

    dlat=math.radians(lat2-lat1)
    dlon=math.radians(lon2-lon1)

    a=math.sin(dlat/2)**2+math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)**2

    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))

    return (R*c)*0.621

def aircraft():

    url="https://opensky-network.org/api/states/all"

    r=requests.get(url,timeout=10)

    planes=[]

    for s in r.json()["states"]:

        if s[5] is None or s[6] is None:
            continue

        lat=s[6]
        lon=s[5]

        d=distance(config.LAT,config.LON,lat,lon)

        if d<=config.RADIUS_MILES:

            dx=(lon-config.LON)/0.3
            dy=(lat-config.LAT)/0.3

            planes.append({

                "callsign":s[1].strip(),
                "alt":int(s[7] or 0),
                "dist":round(d,1),
                "dx":dx,
                "dy":dy

            })

    return planes
