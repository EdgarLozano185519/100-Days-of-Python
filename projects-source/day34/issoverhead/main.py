import requests
from datetime import datetime
import smtplib
import time

# Constants
MY_LAT = 30.264980
MY_LONG = -97.746597
EMAIL = 'test'
PASSWORD = 'test'

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_close():
  lat_close = MY_LAT-5 <= iss_latitude <= MY_LAT+5
  long_close = MY_LONG-5 <= iss_longitude <= MY_LONG+5
  return lat_close and long_close

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def is_dark():
  return time_now.hour >= sunset or time_now.hour < sunrise

while True:
  time.sleep(60)
  if is_dark() and is_close():
    mail = smtplib.SMTP('smtp.gmail.com')
    mail.starttls()
    mail.login(EMAIL, PASSWORD)
    mail.sendmail(EMAIL, EMAIL, 'Subject: ISS Is Over Your Position\n\nAlert! You can now see the ISS orbit above you!')
    print('Email sent as the ISS is above you.')
  else:
    print('ISS is not above you.')
