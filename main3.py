from selenium import webdriver

path = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(path)


browser.get('https://www.weather.go.kr/weather/forecast/mid-term_02.jsp')
print(browser.title)


browser.close()