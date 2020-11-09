import requests

url = 'http://127.0.0.1:5000/summary/covidgr'

headers = {
    'Content-type': 'application/json',
}

data = '{"sum_cases": "56,698", "sum_deaths": "784", "sum_recovered": "9,989"}'

response = requests.put(url, headers=headers, data=data)
print(response.json())
