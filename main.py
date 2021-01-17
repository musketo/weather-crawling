import requests
from bs4 import BeautifulSoup
import sys

url = requests.get('https://www.weather.go.kr/weather/forecast/mid-term_02.jsp')

soup = BeautifulSoup(url.content, 'html.parser')

data1 = soup.select_one("table.table_midterm")
data2 = soup.find_all('table')
data3 = soup.select('table.table_midterm')[1]
print(data3)

with open('/Users/danny/Python/weather-crawling/weather-crawling/text.txt','w') as f:
    f.write(str(data3))
