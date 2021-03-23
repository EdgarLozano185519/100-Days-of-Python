from selenium import webdriver
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException

# Constants
USER = "user"
PASSWORD = "password"
ACCOUNT_URL = "https://www.instagram.com/user"
INSTAGRAM_URL = "http://instagram.com"

# Start driver
driver = webdriver.Chrome('./chromedriver')
driver.get(INSTAGRAM_URL)

# Login
sleep(3)
user = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
user.send_keys(USER)
password.send_keys(PASSWORD)
login_button.click()

# Visit desired account page
sleep(3)
driver.get(ACCOUNT_URL)

# Click on link for people following
sleep(3)
following = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
num_following = int(following.text.split(' ')[0])
following.click()

# Follow people on account
sleep(2)
# Scrolling code
dialog = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
for i in range(10):
  driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
  sleep(1)

buttons = dialog.find_elements_by_css_selector('li button')
for button in buttons:
  try:
    button.click()
    sleep(1)
  except ElementClickInterceptedException:
    cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
    cancel_button.click()
print(f"{len(buttons)} follow buttons.")

# Close driver
driver.close()
