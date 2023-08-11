import json

import requests


def get_json_file(url):
    response = requests.get(url)

    result = response.json()

    with open("json_obj.json", "w") as file:
        json.dump(result, file, indent=4)
