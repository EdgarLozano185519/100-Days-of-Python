import requests
from flight_data import FlightData
from decouple import config

API = config('API')
URL = config('URL')
SEARCH_URL = config('SEARCH_URL')

class FlightSearch:
  #This class is responsible for talking to the Flight Search API.
  def iata_code(self, city_name):
    header = {'apikey': API}
    body = {'term': city_name}
    response = requests.get(URL, headers=header, params=body)
    code = response.json()['locations'][0]['code']
    return code
  
  def find_flight(self, origin_city_code, destination_city_code, from_time, to_time):
    body = {
      "fly_from": origin_city_code,
      "fly_to": destination_city_code,
      "date_from": from_time.strftime("%d/%m/%Y"),
      "date_to": to_time.strftime("%d/%m/%Y"),
      "nights_in_dst_from": 7,
      "nights_in_dst_to": 28,
      "flight_type": "round",
      "one_for_city": 1,
      "max_stopovers": 0,
      "curr": "USD"
    }
    header = {'apikey': API}
    response = requests.get(url=SEARCH_URL, headers=header, params=body)
    try:
      data = response.json()["data"][0]
    except IndexError:
      print(f"No flights found for {destination_city_code}.")
      return None
    flight_data = FlightData(
      price=data["price"],
      origin_city=data["route"][0]["cityFrom"],
      origin_airport=data["route"][0]["flyFrom"],
      destination_city=data["route"][0]["cityTo"],
      destination_airport=data["route"][0]["flyTo"],
      out_date=data["route"][0]["local_departure"].split("T")[0],
      return_date=data["route"][1]["local_departure"].split("T")[0]
    )
    print(f"{flight_data.destination_city}: ${flight_data.price}")
    return flight_data