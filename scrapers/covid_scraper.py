from bs4 import BeautifulSoup
from datetime import date
from lxml import html

import requests
import re
import json

class CovidScraper:
    def __init__(self):
        self.api_url = 'http://127.0.0.1:5000/covidgr'
        self.api_sum_url = 'http://127.0.0.1:5000/summary/covidgr'
        self.api_test_url = 'http://127.0.0.1:5000/covidgr/tests'
        self.scrape_url = 'https://www.worldometers.info/coronavirus/country/greece/'
        self.scrape_tests_url = 'https://github.com/owid/covid-19-data/blob/master/public/data/testing/covid-testing-latest-data-source-details.csv'
        self.today = ''
        self.covid_data = []
        self.summary_data= []

    def scrape_data(self):
        data = []
        self.today = str(date.today())

        soup = self.scrape_page_content()
        soup_test_page = self.scrape_page_content_contains_tests()

        if soup:
            self.get_daily_data(soup)
            self.get_summary_data(soup)

            if self.summary_data and self.covid_data:
                post_daily_and_sum_covid_data = self.call_api_put_data(
                    self.today, self.covid_data, self.summary_data)
                data.append(post_daily_and_sum_covid_data)
        
        if soup_test_page:
            tests_data = self.get_tests_per_day(soup_test_page)

            if tests_data[0]:
                post_daily_tests_covid_data = self.call_api_post_tested_covid_data(
                    tests_data[0], tests_data[1])
                data.append(post_daily_tests_covid_data)

        return data

    def scrape_page_content(self):
        page = requests.get(self.scrape_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        return soup
    
    def scrape_page_content_contains_tests(self):
        page = requests.get(self.scrape_tests_url)
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

        all_cases_covidgr_html_content = soup.find_all(
            'div', class_='maincounter-number')
        
        for item in range(len(all_cases_covidgr_html_content)):
            regex = r'(\n)|\s'
            all_cases_data = re.sub(
                regex, '', all_cases_covidgr_html_content[item].text)
            summary_data.append(all_cases_data)
        
        self.summary_data = summary_data
    
    def get_tests_per_day(self, tree):

        html_content = tree.find('tr', id='LC34').find_all('td')
        country_code = html_content[1]
        date_test = html_content[3].text

        if country_code.text == 'GRC':
            today_tests = html_content[10].text
            total_tests = html_content[8].text
        
        return [date_test, today_tests]
    
    def call_api_post_tested_covid_data(self, today, tests):
        headers = {
            'Content-type': 'application/json',
        }

        data = json.dumps({"date": today, "daily_test": tests})

        response_tests = requests.post(
            self.api_test_url, headers=headers, data=data)

        return response_tests.json()

    def call_api_put_data(self, today, covid_data, summary_data):
        headers = {
            'Content-type': 'application/json',
        }

        data = json.dumps(
            {"date": today, "cases": covid_data[0], "deaths": covid_data[1]})

        sum_data = json.dumps(
            {"sum_cases": summary_data[0], "sum_deaths": summary_data[1], "sum_recovered": summary_data[2]})

        response = requests.post(self.api_url, headers=headers, data=data)

        response_sum = requests.put(
            self.api_sum_url, headers=headers, data=sum_data)

        return [response.json(), response_sum.json()]

if __name__ == '__main__':
    cs = CovidScraper()
    results = cs.scrape_data()
    print(results)
