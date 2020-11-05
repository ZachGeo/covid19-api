import requests

url = 'http://127.0.0.1:5000/covidgr'

headers = {
    'Content-type': 'application/json',
}

data = '{"date": "2020-11-04", "cases": "2,646", "deaths": "18"}'

response = requests.post(url, headers=headers, data=data)
print(response.json())
