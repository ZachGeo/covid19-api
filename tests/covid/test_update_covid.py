import requests
import datetime
import json

url = 'http://127.0.0.1:5000/covidgr/2020-11-02'

headers = {
    'Content-type': 'application/json',
}

data = json.dumps(
    {"date": "2020-11-02", "cases": "1,151", "deaths": "7"})

response = requests.put(url, headers=headers, data=data)
print(response.json())
