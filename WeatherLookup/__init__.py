import re
import string
import requests
__version__ = "1.0.0"
import json

token = "101d9b88089c209d67d9ae493ba1f4c7"
def temperature(location):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={token}")
    
    weather = res.text
    dict=json.loads(weather)
    betterdict = dict["main"]
    temperature = betterdict["temp"]
    farhenhiettemp = 9 / 5 * (temperature - 273) + 32
    return int(farhenhiettemp)
    
def condition(location):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={token}")
    
    weather = res.text
    dict=json.loads(weather)
    betterdict = dict["weather"]
    objectzero = betterdict[0]
    description = objectzero["description"]

    return description.title()

