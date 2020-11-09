import requests

url = 'http://127.0.0.1:5000/summary/covid/world'

headers = {
    'Content-type': 'application/json',
}

data = '{"sum_world_cases": "50,828,987", "sum_world_deaths": "1,263,602", "sum_world_recovered": "35,843,265"}'

response = requests.post(url, headers=headers, data=data)
print(response.json())
