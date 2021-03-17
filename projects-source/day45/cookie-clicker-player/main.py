from selenium import webdriver
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome('./chromedriver')
driver.get(URL)
cookie = driver.find_element_by_id('cookie')
five_seconds = time.time()+5
while True:
  cookie.click()

driver.close()
