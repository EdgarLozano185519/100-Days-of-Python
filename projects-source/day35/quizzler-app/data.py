import requests

params = {
  "amount": 10,
  "type": "boolean"
}
response = requests.get('https://opentdb.com/api.php', params)
question_data = response.json()['results']