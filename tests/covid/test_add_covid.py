import requests

url = 'http://127.0.0.1:5000/covidgr'

headers = {
    'Content-type': 'application/json',
}

data = '{"date": "2020-11-08", "cases": "1,889", "deaths": "35"}'

response = requests.post(url, headers=headers, data=data)
print(response.json())
