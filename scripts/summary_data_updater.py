from urllib.request import Request, urlopen

import pandas as pd
import requests
import re
import json
import pickle

class AccessSummaryData:
    
    def __init__(self):

        self.scrape_ourworldindata_url = 'https://raw.githubusercontent.com/' \
            'owid/covid-19-data/master/public/data/latest' \
            '/owid-covid-latest.csv'
    
    def get_data(self):

        content = self.request_page(self.scrape_ourworldindata_url)
        
        requested_data = self.request_countries_data(content)

        manipulated_data = self.maniulate_data(requested_data)

        self.store_data(manipulated_data)
    
    def request_page(self, url):
        headers = requests.utils.default_headers()
        user_agent = headers['User-Agent']

        req = Request(url)
        req.add_header('User-Agent', user_agent)
        content = urlopen(req)

        return content

    def request_countries_data(self, url):

        selected_columns = [
            'location', 'last_updated_date', 'total_cases', 'total_deaths', 
            'people_fully_vaccinated', 'population'
        ]

        selected_countries = [
            'World', 'Greece', 'France', 'Germany', 'United Kingdom',
            'Japan', 'United States', 'Canada', 'Russia', 'China',
            'India', 'Austalia', 'South Africa', 'United Arab Emirates', 
            'European Union']

        specific_cols_data = pd.read_csv(
            url, usecols = selected_columns, low_memory=True)

        select_specific_data = specific_cols_data[
            (specific_cols_data.location.isin(selected_countries))
        ]
        
        requested_data = select_specific_data.set_index(
            'location').T.to_dict(orient='dict')

        return requested_data

    def maniulate_data(self, requested_data):
        manipulated_data = []

        for country_data in requested_data.items():

            data = {
                "country": country_data[0],
                **country_data[1]
            }

            for key, value in data.items():
                if type(value) == float:
                    if not pd.isna(value):
                        data[key] = int(value)
            
            manipulated_data.append(data)

        return manipulated_data

    def store_data(self, data):

        filepath = f'../data/countries_summary_data.pickle'

        with open(filepath, 'wb') as f:
            pickle.dump(data, f)

if __name__ == '__main__':
    sd = AccessSummaryData()
    sd.get_data()
