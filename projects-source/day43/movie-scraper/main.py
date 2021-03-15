from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time

url = 'https://www.empireonline.com/movies/features/best-movies-2'
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
time.sleep(5)
html = driver.page_source
soup = bs(html, 'html.parser')
movies = soup.find_all('h3')
movies.reverse()
with open('movies.txt', 'w') as file:
  for movie in movies:
    file.write(movie.get_text()+'\n')