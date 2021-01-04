import requests
from bs4 import BeautifulSoup
import sys

wp = requests.get('https://www.weather.go.kr/weather/forecast/mid-term_02.jsp')

soup = BeautifulSoup(wp.content, 'html.parser')
f = open('/Users/danny/PycharmProjects/pythonProject/text.txt','w',encoding='utf-8')
data = soup.find_all("li")
f.write(data)
f.close()

# for child in soup.tbody.children:
#     print(child)
