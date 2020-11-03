from bs4 import BeautifulSoup
from datetime import date

import requests
import re
import json

today = date.today()
current_date = today.strftime("%Y-%m-%d")

page = requests.get(
    'https://www.worldometers.info/coronavirus/country/greece/')

soup = BeautifulSoup(page.content, 'html.parser')
daily_covidgr_html_content = soup.find('li', class_='news_li')
get_html_text = daily_covidgr_html_content.text

covid_data = []
for elem in get_html_text.split():
    regex = '\d*(.|)\d+'
    match = re.findall(regex, elem)
    if match:
        covid_data.append(elem)

url = 'http://127.0.0.1:5000/covidgr'

headers = {
    'Content-type': 'application/json',
}

data = json.dumps(
    {"date": current_date, "cases": covid_data[0], "deaths": covid_data[1]})

response = requests.post(url, headers=headers, data=data)
print(response.json())
