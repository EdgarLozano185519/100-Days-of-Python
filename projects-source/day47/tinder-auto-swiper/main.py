from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

# Constants
URL = "http://tinder.com"
USER = "test"
PASSWORD = "test"

driver = webdriver.Chrome('./chromedriver')
driver.get(URL)

# Find login button
time.sleep(3)
buttons = driver.find_elements_by_tag_name('button')
buttons[1].click()

# Find Facebook login button
time.sleep(3)
buttons = driver.find_elements_by_tag_name('button')
buttons[8].click()

# Log in to Facebook
time.sleep(3)
# Switch to Facebook window
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
#print(driver.title)
# Now find inputs and fill them in
time.sleep(3)
email = driver.find_element_by_id('email')
password = driver.find_element_by_id('pass')
login = driver.find_element_by_name('login')
email.send_keys(USER)
password.send_keys(PASSWORD)
login.click()

# Switch back to main window
base_window = driver.window_handles[0]
driver.switch_to.window(base_window)

# Dismiss popups
time.sleep(5)
button = driver.find_element_by_css_selector('[aria-label=Allow]')
button.click()
time.sleep(3)
button = driver.find_element_by_css_selector('[aria-label="Not interested"]')
button.click()

# Dislikes now
for i in range(100):
  print("Attempting dislike.")
  try:
    dislike = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
    dislike.click()
  except ElementClickInterceptedException:
    try:
      match_popup = driver.find_element_by_css_selector(".itsAMatch a")
      match_popup.click()
    except NoSuchElementException:
      time.sleep(2)
  print("done")

driver.close()
