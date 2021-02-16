from bs4 import BeautifulSoup
from datetime import date, timedelta

import pandas as pd
import requests
import re
import json
import pickle

class AccessSummaryData:
    
    def __init__(self):

        self.scrape_ourworldindata_url = """
            https://covid.ourworldindata.org/data/owid-covid-data.csv"""
    
    def get_data(self):

        today = date.today()
        date_of_requested_data = today - timedelta(days=2)

        requested_data = self.request_countries_data(
            date_of_requested_data, self.scrape_ourworldindata_url)

        self.store_data(requested_data)
            
    def request_countries_data(self, date_of_requested_data, url):

        str_date = date_of_requested_data.strftime("%Y-%m-%d")

        selected_columns = [
            'location', 'date', 'total_cases', 'total_deaths', 
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
            (specific_cols_data['date'] == str_date) &
            (specific_cols_data.location.isin(selected_countries))
        ]
        
        requested_data = select_specific_data.set_index(
            'location').T.to_dict(orient='dict')

        return requested_data

    def store_data(self, requested_data):
        
        for country_data in requested_data.items():
            filepath = f'../data/{country_data[0]}_summary_data.pickle'

            data = {
                "country": country_data[0],
                **country_data[1]
            }

            with open(filepath, 'wb') as f:
                pickle.dump(data, f)

if __name__ == '__main__':
    sd = AccessSummaryData()
    sd.get_data()
