from selenium import webdriver

URL = 'https://en.wikipedia.org/wiki/Main_Page'

driver = webdriver.Chrome('./chromedriver')
driver.get(URL)
result = driver.find_element_by_css_selector('#articlecount > a')
print(f"Number of English Articles: {result.text}")
driver.close()
