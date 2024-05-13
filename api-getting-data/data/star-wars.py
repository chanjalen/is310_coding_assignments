import requests
import json
r = requests.get('https://swapi.dev/api/starships/9/')
data = r.json()

with open('starships.json', 'w') as f:
    json.dump(data, f)