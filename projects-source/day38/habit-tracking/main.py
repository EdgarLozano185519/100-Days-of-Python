import requests

# Create user using post request (done)
# Constants
#URL = "https://pixe.la/v1/users"
#params = {
#  "token": "at91ikaitheiwkai",
#  "username": 'edgarlozano19485768',
#  "agreeTermsOfService": "yes",
#  "notMinor": "yes"
#}
#response = requests.post(URL, json=params)
#print(response.text)

# Create graph definition (done)
# Constants
#USER = "edgarlozano19485768"
#TOKEN = "at91ikaitheiwkai"
#url = f"https://pixe.la/v1/users/{USER}/graphs"
# Body params used when sending post request
#params = {
#  "id": "askitheitjkt",
#  "name": "Coding Time",
#  "unit": "hour",
#  "type": "int",
#  "color": "sora"
#}
# Header params
#header = {"X-USER-TOKEN": TOKEN}
#response = requests.post(url=url, json=params, headers=header)
#print(response.text)

# Record a new entry in graph
# Constants
#ID = "askitheitjkt"
#USER = "edgarlozano19485768"
#TOKEN = "at91ikaitheiwkai"
#url = f"https://pixe.la/v1/users/{USER}/graphs/{ID}"
#header = {"X-USER-TOKEN": TOKEN}
#body = {
#  "date": "20210308",
#  "quantity": "1"
#}
#response = requests.post(url=url, json=body, headers=header)
#print(response.text)

# Delete an entry in graph
# Constants
ID = "askitheitjkt"
USER = "edgarlozano19485768"
TOKEN = "at91ikaitheiwkai"
url = f"https://pixe.la/v1/users/{USER}/graphs/{ID}"
header = {"X-USER-TOKEN": TOKEN}
body = {
#  "date": "20210803"
}
response = requests.delete(url=url, json=body, headers=header)
print(response.text)