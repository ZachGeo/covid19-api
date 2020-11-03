import requests

url = 'http://127.0.0.1:5000/covidgr/20201103'

headers = {
    'Content-type': 'application/json',
}

response = requests.delete(url, headers=headers)
print(response.json())
