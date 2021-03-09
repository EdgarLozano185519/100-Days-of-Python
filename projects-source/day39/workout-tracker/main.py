import requests
import datetime as dt
from decouple import config

current = dt.datetime.now()
API_KEY = config('API_KEY')
API_ID = config('API_ID')
URL = config('URL')
SHEETY_URL = config('SHEETY_URL')
TOKEN = config('TOKEN')

headers = {
  'x-app-id': API_ID,
  'x-app-key': API_KEY
}

sentence = input("Enter what you did today: ")
body = {
  "query": sentence
}

print("Sending data to Exercise API.")
response = requests.post(URL, json=body, headers=headers)
data = response.json()['exercises'][0]

body = {
  "workout": {
    "date": current.strftime("%d/%m/%Y"),
    "time": current.strftime("%H:%M:%S"),
    "exercise": data["name"],
    "duration": data["duration_min"],
    "calories": data["nf_calories"]
  }
}
header = {"authorization": f"Bearer {TOKEN}"}
print("Sending data to Google Sheets.")
response = requests.post(SHEETY_URL, json=body, headers=header)
print(response.json())
