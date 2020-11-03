import requests

url = 'http://127.0.0.1:5000/covidgr'

headers = {
    'Content-type': 'application/json',
}

data = '{"date": "20201031", "cases": "2,055", "deaths": "6"}'

response = requests.post(url, headers=headers, data=data)
print(response.json())
