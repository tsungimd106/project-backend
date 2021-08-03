import requests
from bs4 import BeautifulSoup
import json

response = requests.get(
    "https://www.cec.gov.tw/central/cmsList/110news?order=asc&offset=0&limit=10&begin=&end=&title=")


soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())  #輸出排版後的HTML內容

result = soup.find_all('title')
    
print(result)