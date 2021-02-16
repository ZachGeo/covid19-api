from urllib.request import Request, urlopen

import pandas as pd
import requests
import re
import json
import pickle

class AccessGreeceDailyData:
    def __init__(self):

        self.scrape_ourworldindata_url = 'https://raw.githubusercontent.com/' \
            'owid/covid-19-data/master/public/data/latest' \
            '/owid-covid-latest.csv'

    def get_data(self):
        data = []

        content = self.request_page(self.scrape_ourworldindata_url)

        requested_data = self.request_daily_data_of_greece(content)

        manipulated_data = self.manipulate_data(requested_data)

        self.store_data(manipulated_data)

    def request_page(self, url):
        headers = requests.utils.default_headers()
        user_agent = headers['User-Agent']

        req = Request(url)
        req.add_header('User-Agent', user_agent)
        content = urlopen(req)

        return content
    
    def request_daily_data_of_greece(self, url):

        data_key = ['tests']

        selected_columns = [
            'location', 'last_updated_date', 'new_cases', 'new_deaths', 
            'new_tests', 'new_vaccinations']
        selected_country = ['Greece']

        specific_cols_data = pd.read_csv(
            url, usecols=selected_columns, low_memory=True)

        select_specific_data = specific_cols_data[
            (specific_cols_data['location'].isin(selected_country))
        ]

        requested_data = select_specific_data.to_dict('records')

        return requested_data
    
    def manipulate_data(self, requested_data):

        for key, value in requested_data[0].items():
            if type(value) == float:
                if not pd.isna(value):
                    requested_data[0][key] = int(value)

        return requested_data

    def store_data(self, data):
    
        filepath = f'../data/greece_daily_data.pickle'

        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
    
if __name__ == '__main__':
    add = AccessGreeceDailyData()
    add.get_data()
