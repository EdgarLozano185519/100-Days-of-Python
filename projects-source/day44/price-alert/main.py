import requests
import lxml
from bs4 import BeautifulSoup as bs
import smtplib

# Constants for email
EMAIL = "test"
PASSWORD = "test"

url = "https://www.amazon.com/Razer-Blade-Base-Gaming-Laptop/dp/B086MFZBM9/ref=sr_1_4?dchild=1&keywords=gaming+laptop&qid=1615928759&sr=8-4"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
  'Accept-Language': 'en-US,en;q=0.9'
}
response = requests.get(url=url, headers=headers)
soup = bs(response.text, 'lxml')
price = soup.find_all("span", class_="a-color-price")[0]
product_name = soup.find("span", id="productTitle").get_text()
print(f"Product: {product_name}")
print(price.get_text())
compare_price = price.get_text()
compare_price = compare_price.replace("$", "")
compare_price = compare_price.replace(",", "")

# Send an email with the item
if float(compare_price) < 1500:
  msg = "Subject: Product Deal\n\n"
  msg += f"Product: {product_name}"
  msg += f"Price: {price.get_text()}"
  msg += "\n\nCome buy it before it goes off the shelves."
  msg += f"\nURL: {url}"
  mail = smtplib.SMTP(host="smtp.gmail.com")
  mail.starttls()
  mail.login(EMAIL, PASSWORD)
  mail.sendmail(EMAIL, EMAIL, msg)
  mail.close()
  print("An email was sent since it is lower than the specified price.")