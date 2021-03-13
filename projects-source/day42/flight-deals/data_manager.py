import requests
from decouple import config

class DataManager:
  #This class is responsible for talking to the Google Sheet.
  def __init__(self):
    self.url = config('SHEET_URL')
    response = requests.get(self.url)
    self.data = response.json()["prices"]
  
  def update_iata(self, code, row):
    self.data[row]['iataCode'] = code
    body = {'price': self.data[row]}
    id = self.data[row]['id']
    response = requests.put(f"{self.url}/{id}", json=body)
    #print(self.data)