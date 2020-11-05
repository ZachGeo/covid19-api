import requests

url = 'http://127.0.0.1:5000/covidgr/2020-11-03'

headers = {
    'Content-type': 'application/json',
}

data = '{"date": "2020-11-02", "cases": "1,151", "deaths": "7"}'

response = requests.put(url, headers=headers, data=data)
print(response.json())
