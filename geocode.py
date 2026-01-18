import requests
import time

CACHE = {}

def geocode(place):
    if place in CACHE:
        return CACHE[place]

    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"{place}, India",
        "format": "json",
        "limit": 1
    }

    r = requests.get(url, params=params, headers={"User-Agent": "women-safety-app"})
    data = r.json()

    if data:
        lat, lon = float(data[0]["lat"]), float(data[0]["lon"])
    else:
        lat, lon = 28.6139, 77.2090  # Delhi fallback

    CACHE[place] = (lat, lon)
    time.sleep(1)  # be polite
    return lat, lon
