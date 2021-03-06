import requests
from twilio.rest import Client
from decouple import config

# Constants for OpenWeatherMap
API_KEY = config('API_KEY')
URL = config('URL')
LAT = config('LAT')
LON = config('LON')
# Twilio constants
ACCOUNT_SID = config('ACCOUNT_SID')
AUTH_TOKEN = config('AUTH_TOKEN')

# Set up Twilio
client = Client(ACCOUNT_SID, AUTH_TOKEN)

params = {
  'lat': LAT,
  'lon': LON,
  'units': 'imperial',
  'exclude': 'current,minutely,daily,alerts',
  'APPID': API_KEY
}

response = requests.get(URL, params).json()
data = response["hourly"][0:12]

umbrella = False
for hour in data:
  condition = hour["weather"][0]["id"]
  if condition < 700:
    umbrella = True

if umbrella:
  message = client.messages.create(
    to="+15126454491",
    from_="+12065650893",
    body="From Edgar's Rain Alert app - You might consider bringing an umbrella."
  )

