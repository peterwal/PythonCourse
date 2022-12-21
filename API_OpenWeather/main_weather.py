import requests
import pprint

api_key = "b01bac24ceea6c048c6b4135ab2045d7"

parameters = {
    "q": "Vienna",
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
data = response.json()
# let's use pprint to pretty print the data dictionary (converted from JSON)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data)
