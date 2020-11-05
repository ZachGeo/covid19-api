from bs4 import BeautifulSoup
from datetime import date

import requests
import re
import json

class CovidScraper:
    def __init__(self):
        self.api_url = 'http://127.0.0.1:5000/covidgr'
        self.scrape_url = 'https://www.worldometers.info/coronavirus/country/greece/'
        self.covid_data = []
        self.summary_data= []

    def scrape_data(self):
        soup = self.scrape_page_content()

        if soup:
            self.get_daily_data(soup)
            self.get_summary_data(soup)

            if self.summary_data and self.covid_data:
                self.call_api_put_data(self.covid_data, self.summary_data)

        return

    def scrape_page_content(self):
        page = requests.get(self.scrape_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        return soup
    
    def get_daily_data(self, soup):
        covid_data = []

        daily_covidgr_html_content = soup.find('li', class_='news_li')
        get_daily_covidgr_text = daily_covidgr_html_content.text

        for elem in get_daily_covidgr_text.split():
            regex = '\d*(.|)\d+'
            match = re.findall(regex, elem)
            if match:
                covid_data.append(elem)
        
        self.covid_data = covid_data
    
    def get_summary_data(self, soup):
        summary_data = []

        all_cases_covidgr_html_content = soup.find_all('div', class_='maincounter-number')
        
        for item in range(len(all_cases_covidgr_html_content)):
            regex = r'(\n)|\s'
            all_cases_data = re.sub(regex, '', all_cases_covidgr_html_content[item].text)
            summary_data.append(all_cases_data)
        
        self.summary_data = summary_data

    def call_api_put_data(self, covid_data, summary_data):
        today = date.today()

        headers = {
            'Content-type': 'application/json',
        }

        data = json.dumps(
            {"date": str(today), "cases": covid_data[0], "deaths": covid_data[1]})

        response = requests.post(self.api_url, headers=headers, data=data)
        print(response.json())        

if __name__ == '__main__':
    cs = CovidScraper()
    cs.scrape_data()
