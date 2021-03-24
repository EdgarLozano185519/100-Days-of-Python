import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep

# Constants
FORM_URL = "YOUR_FORM_URL"
ZILLOW_SEARCH = "?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
url = "https://www.zillow.com/homes/for_rent/1-_beds/"

# Set up drivers
headers = {
  "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
  "ACCEPT-LANGUAGE": "en-US,en;q=0.9"
}
response = requests.get(url=f"{url}{ZILLOW_SEARCH}", headers=headers)
driver = webdriver.Chrome('./chromedriver')

soup = bs(response.text.encode('utf8'), 'html.parser')

# Function to submit form
def submit_form(address_text, price_text, link_text):
  driver.get(FORM_URL)
  
  sleep(2)
  inputs = driver.find_elements_by_css_selector('[type=text]')
  submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
  
  # Fill inputs
  inputs[0].send_keys(address_text)
  inputs[1].send_keys(price_text)
  inputs[2].send_keys(link_text)
  
  # Submit
  submit.click()
  # End function


# Get page number
page_num = int(soup.select('span.Text-c11n-8-27-0__aiai24-0')[-1].get_text().split(' ')[-1])
#print(page_num)

# Put results into dictionary
print("Filling dictionary with data.")
for i in range(2, page_num+1):
  cards = soup.find_all('article')
  for card in cards:
    link = card.find('a')
    
    address = card.find('address').get_text()
    if len(address.split('|')) > 1:
      address = address.split('|')[1][1:]
    
    price = card.select('div.list-card-price')[0].get_text()
    if len(price.split(' ')) > 1:
      price = price.split(' ')[0]
    elif len(price.split('/')) > 1:
      price = price.split('/')[0]
    
    # Submit form
    submit_form(address, price, link['href'])
  # End inner for loop
  
  # Go to next page here
  print(f"Visiting page {i} of {page_num}.")
  response = requests.get(url=f"{url}/{i}_p/{ZILLOW_SEARCH}", headers=headers)
  soup = bs(response.text.encode('utf8'), 'html.parser')

#print(len(houses_array))
driver.close()
