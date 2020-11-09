import requests

url = 'http://127.0.0.1:5000/summary/covidgr'

headers = {
    'Content-type': 'application/json',
}

response = requests.delete(url, headers=headers)
print(response.json())
