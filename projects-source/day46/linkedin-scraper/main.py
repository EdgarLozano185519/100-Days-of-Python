from selenium import webdriver
import time

# Constants (fill in your information here)
RESULTS_URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_L=Austin%2C%20Texas%20Metropolitan%20Area&geoId=90000064&keywords=python%20developer&location=Austin%2C%20Texas%20Metropolitan%20Area"
MAIN_URL = "https://linkedin.com"
L_EMAIL = "test"
L_PASSWORD = "test"

# Initialize driver
driver = webdriver.Chrome("./chromedriver")
driver.get(MAIN_URL)

# Sign in
inputs = driver.find_elements_by_class_name('input__input')
inputs[0].send_keys(L_EMAIL)
inputs[1].send_keys(L_PASSWORD)
sign_in = driver.find_element_by_class_name("sign-in-form__submit-button")
sign_in.click()

driver.get(RESULTS_URL)
time.sleep(5)

# Code to scroll through all the jobs
# All jobs are stored in last element of array
jobs = []
offset_height_all_jobs = driver.execute_script('return document.querySelector(".jobs-search-results").offsetHeight;')
total_height_all_jobs = driver.execute_script('return document.querySelector(".jobs-search-results").scrollHeight;')
new_height = offset_height_all_jobs * 2
while new_height < total_height_all_jobs:
  time.sleep(2)
  driver.execute_script(f'document.querySelector(".jobs-search-results").scrollTo(0, {new_height})')
  new_height += offset_height_all_jobs
job = driver.find_elements_by_class_name("job-card-container__company-name")
jobs.append(job)
all_jobs = jobs[-1]

print(len(all_jobs))
with open("companies.txt", "w") as file:
  for job in all_jobs:
    file.write(job.text+"\n")
driver.close()
