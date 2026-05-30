from dotenv import load_dotenv
import os
import requests
import json


load_dotenv()

api_key = os.getenv("API_KEY")
# print(f"Key being used: '{api_key}'")

cityweather=input("Enter a city: ")
api_url = f"https://api.openweathermap.org/data/2.5/weather?q={cityweather}&appid={api_key}&units=metric"

try:
    r = requests.get(api_url)
except requests.exceptions.ConnectionError:
    print("No connection")

else:

    if r.status_code == 404:
        print("City not found, try again")
    else:

        ret = (r.json())
        # print(ret)
        city = ret["name"]
        temp = ret["main"]["temp"]
        feeltemp = ret["main"]["feels_like"]
        weather = ret["weather"][0]["description"]
        humid = ret["main"]["humidity"]

        print(f"City: {city}")
        print(f"Temperature: {int(temp)}°C")
        print(f"Feels like: {int(feeltemp)}°C")
        print(f"Weather: {weather}")
        print(f"Humidity: {humid}%")

        data = {
            "city" : city,
            "temp" : temp,
            "weather" : weather
        } 
        try:
        
            with open("weather/weather.json", "r") as file:
                history = json.load(file)


        except FileNotFoundError:
            history = []

        history.append(data)

        with open("weather/weather.json", "w") as file:
            json.dump(history, file, indent=2)

