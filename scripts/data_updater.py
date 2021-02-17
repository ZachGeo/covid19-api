from datetime import date

import pickle
import requests
import json

class DataUpdater:
    def __init__(self):
        self.api_greece_daily_url = 'http://127.0.0.1:5000/' \
            'covid19/daily-data/greece'

        self.api_greece_summary_url = 'http://127.0.0.1:5000/' \
            'covid19/summary-data/greece'

        self.api_countires_summary_url = 'http://127.0.0.1:5000/' \
            'covid19/summary-data/country'

        self.api_world_summary_url = 'http://127.0.0.1:5000/' \
            'covid19/summary-data/world'

        self.headers = {'Content-type': 'application/json',}
        self.greece_daily_data = '../data/greece_daily_data.pickle'
        self.countries_summary_data = '../data/countries_summary_data.pickle'
    
    def update_api_data(self):
        
        self.update_daily_data_greece(self.greece_daily_data)

        self.update_summary_data_countries(self.countries_summary_data)

    def update_daily_data_greece(self, data):
        with open(data, 'rb') as f:
            daily_data_greece = pickle.load(f)
        
        daily_data_greece[0]['country'] = daily_data_greece[0].pop('location')
        daily_data_greece[0]['date'] = daily_data_greece[0].pop('last_updated_date')        
        
        response = requests.post(
            self.api_greece_daily_url, 
            headers=self.headers, 
            data=str(json.dumps(daily_data_greece[0]))
        )
            
    def update_summary_data_countries(self, data):
        countries_data = []

        with open(data, 'rb') as f:
            summary_data_countries = pickle.load(f)
        
        for record in summary_data_countries:
            if record['country'] == 'Greece':
                api_url = self.api_greece_summary_url
                greece_data = record
            elif record['country'] == 'World':
                api_url = self.api_world_summary_url
                world_data = record
            else:
                api_url = self.api_countires_summary_url
                countries_data.append(record)

            response = requests.put(
                api_url, 
                headers=self.headers, 
                data=str(json.dumps(record))
            )


if __name__ == '__main__':
    du = DataUpdater()
    du.update_api_data()
