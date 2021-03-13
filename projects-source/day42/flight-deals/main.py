from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from datetime import datetime, timedelta
import requests
from decouple import config

USERS_SHEET_URL = config('USERS_SHEET_URL')

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data = DataManager()
sheet_data = data.data

# Get users data
response = requests.get(USERS_SHEET_URL)
users = response.json()["users"]

search = FlightSearch()

print("Updating any empty Iata Code cells in the google sheet.")
for row_index in range(len(sheet_data)):
  if sheet_data[row_index]['iataCode'] == '':
    data.update_iata(search.iata_code(sheet_data[row_index]['city']), row_index)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
for destination in sheet_data:
  flight = search.find_flight(
    "LON",
    destination["iataCode"],
    from_time=tomorrow,
    to_time=six_month_from_today
  )
  if flight is None:
    continue
  if flight.price < destination["lowestPrice"]:
    message = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
    if flight.stop_overs > 0:
      message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
      print(message)
    notification_manager.send_sms(message)
    
    # Send the message to user emails
    emails = []
    for user in users:
      emails.append(user['email'])
    notification_manager.send_emails(message, emails)