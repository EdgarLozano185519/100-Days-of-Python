import requests
from twilio.rest import Client
from decouple import config

# Constants
STOCK = config('STOCK')
COMPANY_NAME = config('COMPANY_NAME')
API_KEY = config('API_KEY')
NEWS_API = config('NEWS_API')
URL = config('URL')
NEWS_URL = config('NEWS_URL')
ACCOUNT_SID = config('ACCOUNT_SID')
AUTH_TOKEN = config('AUTH_TOKEN')

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# Params for call
params = {
  'function': 'TIME_SERIES_DAILY',
  'symbol': STOCK,
  'apikey': API_KEY
}
print("Getting stock information for Tesla.")
response = requests.get(URL, params)
#print(response.json())
data = response.json()["Time Series (Daily)"]
counter = 0
prices = []
for date in data:
  prices.append(float(data[date]["4. close"]))
  counter += 1
  if counter > 1:
    break

# Calculate percentage
# Also determine if increasing or decreasing
percent = 0
increase_decrease = ""
if prices[0] < prices[1]:
  percent = ((prices[1]/prices[0])*100)-100
  increase_decrease = "increase"
else:
  percent = 100-((prices[1]/prices[0])*100)
  increase_decrease = "decrease"

# Round and formatted output
rounded = round(percent, 2)
print(f"There was a {rounded} {increase_decrease} between last two days.")
msg = f"TSLA: {increase_decrease} {rounded}%"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if percent >= 5:
  params = {
    'language': 'en',
    'apiKey': NEWS_API,
    'q': STOCK
  }
  print("Since percentage more than 5%, fetching 3 news articles.")
  response = requests.get(NEWS_URL, params)
  data = response.json()
  articles = data['articles'][0:3]
  for article in articles:
    title = article['title']
    brief = article["description"]
    #print(f"Headline: {title}\nBrief: {brief}")
    msg += f"\nHeadline: {title}\nBrief: {brief}"

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
print(f"Sending following message:\n{msg}")
# Set up Twilio
client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages.create(
  to="+15126454491",
  from_="+12065650893",
  body=msg
  )
print("Message sent.")

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

