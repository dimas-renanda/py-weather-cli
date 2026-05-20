#!/usr/bin/env python3
"""Fetch weather from wttr.in — no API key needed."""
import sys, urllib.request, json

def get_weather(location=""):
    url = f"https://wttr.in/{urllib.parse.quote(location)}?format=j1"
    try:
        import urllib.parse
        url = f"https://wttr.in/{urllib.parse.quote(location)}?format=j1"
        with urllib.request.urlopen(url, timeout=10) as r:
            data = json.load(r)
        cur = data["current_condition"][0]
        area = data["nearest_area"][0]
        city = area["areaName"][0]["value"]
        country = area["country"][0]["value"]
        temp_c = cur["temp_C"]
        feels = cur["FeelsLikeC"]
        desc = cur["weatherDesc"][0]["value"]
        humidity = cur["humidity"]
        wind = cur["windspeedKmph"]
        print(f"\n🌍 {city}, {country}")
        print(f"   {desc}")
        print(f"   🌡  {temp_c}°C  (feels like {feels}°C)")
        print(f"   💧 Humidity: {humidity}%")
        print(f"   💨 Wind: {wind} km/h\n")
    except Exception as e:
        print(f"Error: {e}")

import urllib.parse
location = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else ""
get_weather(location)
