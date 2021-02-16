from bs4 import BeautifulSoup
from datetime import date, timedelta
from lxml import html

import pandas as pd
import requests
import re
import json
import pickle

class CovidGreeceScraper:
    def __init__(self):
        self.worldmeters_url = """
            https://www.worldometers.info/coronavirus/country/greece/"""

        self.owid_tests_url = 'https://raw.githubusercontent.com/owid/' \
            'covid-19-data/master/public/data/testing/' \
            'covid-testing-all-observations.csv'

        self.owid_vaccinations_url = 'https://raw.githubusercontent.com/' \
            'owid/covid-19-data/master/public/data/' \
            'vaccinations/vaccinations.csv'

    def get_data(self):
        data = []
        today = date.today()
        date_of_requested_data = today - timedelta(days=3)

        soup = self.scrape_worldmeteres_content(self.worldmeters_url)

        if soup:
            main_data = self.get_daily_main_data(soup)

        tests_data = self.scrape_owid_tests_content(
            date_of_requested_data, self.owid_tests_url)
    
        vaccinations_data = self.scrape_owid_vaccinations_content(
            date_of_requested_data, self.owid_vaccinations_url)
        
        data = self.store_data(main_data, tests_data, vaccinations_data)

        return data

    def scrape_worldmeteres_content(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        return soup
            
    def get_daily_main_data(self, soup):
        main_data_keys = ['cases', 'deaths']
        main_data_values = []

        daily_covidgr_html_content = soup.find('li', class_='news_li')
        get_daily_covidgr_text = daily_covidgr_html_content.text

        for elem in get_daily_covidgr_text.split():
            regex = '\d*(.|)\d+'
            match = re.findall(regex, elem)
            if match:
                main_data_values.append(int(elem))
        
        main_data = dict(zip(main_data_keys, main_data_values))

        return main_data
    
    def scrape_owid_tests_content(self, date, url):

        data_key = ['tests']
        str_date = date.strftime("%Y-%m-%d")

        selected_columns = ['ISO code', 'Date', 'Daily change in cumulative total']
        selected_country = ['GRC']
        selected_date = [str_date]

        specific_cols_data = pd.read_csv(
            url, usecols=selected_columns, low_memory=True)

        select_specific_data = specific_cols_data[
            (specific_cols_data['Date'].isin(selected_date)) &
            (specific_cols_data['ISO code'].isin(selected_country))
        ]

        requested_data = select_specific_data.to_dict('list')
        tests_value = int(requested_data['Daily change in cumulative total'][0])

        tests_data = {'tests': tests_value}

        return tests_data
    
    def scrape_owid_vaccinations_content(self, date, url):
        
        data_key = ['vaccinations']
        str_date = date.strftime("%Y-%m-%d")

        selected_columns = ['iso_code', 'date', 'daily_vaccinations_raw']
        selected_country = ['GRC']
        selected_date = [str_date]

        specific_cols_data = pd.read_csv(
            url, usecols=selected_columns, low_memory=True)
        
        select_specific_data = specific_cols_data[
            (specific_cols_data['date'].isin(selected_date)) &
            (specific_cols_data['iso_code'].isin(selected_country))
        ]

        requested_data = select_specific_data.to_dict('list')

        vaccinations_value = int(requested_data['daily_vaccinations_raw'][0])
        vaccinations_data = {'vaccinations': vaccinations_value}
        
        return vaccinations_data
    
    def store_data(self, main_data, tests_data, vaccinations_data):
        data = {**main_data, **tests_data, **vaccinations_data}
        
        print(data)
        return data
    
if __name__ == '__main__':
    cgs = CovidGreeceScraper()
    cgs.get_data()
