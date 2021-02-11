from datetime import date

import pickle
import requests
import json

class DataUpdater:
    def __init__(self):
        self.api_sum_url = 'http://127.0.0.1:5000/covid19-greece/summary-data'
        self.api_url = 'http://127.0.0.1:5000/covid19-greece/data'
        self.headers = {'Content-type': 'application/json',}
        self.covid19_greece_sum_filepath = './covid19_greece_summary_data.pickle'
        self.covid19_greece_data = './covid19_greece_data.pickle'

    def update_greece_sum_data(self):
        with open(self.covid19_greece_sum_filepath, 'rb') as f:
            sum_data = pickle.load(f)

        response = requests.put(
            self.api_sum_url, headers=self.headers, data=str(json.dumps(sum_data)))
    
    def update_greece_data(self):
        with open(self.covid19_greece_data, 'rb') as f:
            data = pickle.load(f)
        
        response = requests.post(
            self.api_url, headers=self.headers, data=str(json.dumps(data)))


if __name__ == '__main__':
    du = DataUpdater()
    du.update_greece_sum_data()
    du.update_greece_data()
