import requests
import json


def get_request(url):
    r = requests.get(url)

    result = r.json()

    with open('json_obj.json', 'w') as file:
        json.dump(result, file, indent=4)
