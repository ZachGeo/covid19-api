import requests

url = 'http://127.0.0.1:5000/summary/covid/world'

headers = {
    'Content-type': 'application/json',
}

response = requests.get(url, headers=headers)
print(response.json())
