#if u want to scrap a website 
#1. use the API
#2. HTML web scraping tool like bs4

import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com/"

r=requests.get(url)
content=requests.get(url)
htmlcontent=r.content
# print(htmlcontent)

soup=BeautifulSoup(htmlcontent,'html.parser')
# print(soup)