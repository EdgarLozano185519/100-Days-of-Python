import requests
from decouple import config

USERS_SHEET_URL = config('USERS_SHEET_URL')

first = input("First name: ")
last = input("Last name: ")
email = input("Email: ")
confirm = input("Confirm email: ")

if email == confirm:
  body = {
    "user": {
      "firstName": first,
      "lastName": last,
      "email": email
    }
  }
  response = requests.post(USERS_SHEET_URL, json=body)
  print("Success. You're now part of the Flight Club!")
else:
  print("Sorry, emails did not match. You're not part of the flight club yet.")