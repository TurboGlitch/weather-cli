from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("API_KEY")
# print(f"Key being used: '{api_key}'")

city=input("Enter a city: ")
api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
r = requests.get(api_url)
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


# Every git command

# # 1. Initialize a git repository in your project folder
# git init

# # 2. Check what files are staged/unstaged
# git status

# # 3. Stage all files
# git add .

# # 4. Save a snapshot with a message
# git commit -m "your message here"

# # 5. Connect your local repo to GitHub
# git remote add origin https://github.com/username/repo-name.git

# # 6. Rename branch to main
# git branch -M main

# # 7. Push to GitHub for the first time
# git push -u origin main

# # 8. After the first push, just use this to push
# git push


# For adding on later

# git add .
# git commit -m "what you changed"
# git push