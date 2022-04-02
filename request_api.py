import requests
import json

url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'

def get_request(url):
    r = requests.get(url)

    result = r.json()

    with open('json_obj.json', 'w') as file:
        json.dump(result, file, indent=4)
