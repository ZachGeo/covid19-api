import requests
import datetime
import json

url = 'http://127.0.0.1:5000/covidgr/2020-11-07'

headers = {
    'Content-type': 'application/json',
}

data = json.dumps(
    {"date": "2020-11-07", "cases": "2,555", "deaths": "34"})

response = requests.put(url, headers=headers, data=data)
print(response.json())
