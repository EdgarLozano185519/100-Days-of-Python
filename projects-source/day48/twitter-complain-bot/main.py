from selenium import webdriver
from time import sleep

URL = "https://www.speedtest.net"
PROMISED_SPEED = 900
TWITTER_USER = "test"
TWITTER_PASSWORD = "test"

driver = webdriver.Chrome('chromedriver')
driver.get(URL)

# Click the start button
sleep(5)
button = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
button.click()

# Get download and upload speeds
sleep(60)
download_element = driver.find_element_by_class_name('download-speed')
upload_element = driver.find_element_by_class_name('upload-speed')
download_text = download_element.text
upload_text = upload_element.text

if float(download_text) < PROMISED_SPEED:
  msg = f"Download speed and upload speed is less than promised by my ISP.\n "
  msg += f"Download speed: {download_text}\n "
  msg += f"Upload speed: {upload_text}"
  print(msg)
  
  # Tweet it out
  # First login
  driver.get('https://twitter.com/login')
  sleep(5)
  email_input = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
  password_input = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
  login_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
  email_input.send_keys(TWITTER_USER)
  password_input.send_keys(TWITTER_PASSWORD)
  login_button.click()
  sleep(3)
  
  # Verify account with phone number
  verification = input("Enter verification code: ")
  verify_input = driver.find_element_by_xpath('//*[@id="challenge_response"]')
  login_button = driver.find_element_by_xpath('//*[@id="email_challenge_submit"]')
  verify_input.send_keys(verification)
  login_button.click()
  
  # Now tweet
  sleep(5)
  tweet_box = driver.find_element_by_css_selector('[aria-label="Tweet text"]')
  tweet_button = driver.find_element_by_css_selector('[data-testid=tweetButtonInline]')
  msg = msg.replace('\n', '')
  tweet_box.send_keys(msg)
  tweet_button.click()
  sleep(5)

driver.close()
