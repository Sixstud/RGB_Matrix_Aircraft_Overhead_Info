import requests
import config

FLIGHT_API_KEY = config.FLIGHT_API_KEY  # your key here
FLIGHT_API_URL = "https://app.goflightlabs.com/flights-with-call-sign"

def get_route_info(callsign):
    """
    Look up a flight with its callsign to get origin and destination.
    Returns (origin, destination) strings.
    If no result or error, returns ("UNK","UNK").
    """
    try:
        params = {
            "access_key": FLIGHT_API_KEY,
            "callsign": callsign
        }
        r = requests.get(FLIGHT_API_URL, params=params, timeout=5)
        data = r.json()
        flights = data.get("data", [])
        if flights:
            flight = flights[0]
            origin = flight.get("origin_airport_iata", "UNK")
            dest = flight.get("destination_airport_iata", "UNK")
            return origin, dest
    except Exception:
        pass

    return "UNK", "UNK"
