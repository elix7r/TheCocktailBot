import json


def ingredients():
    keys = list()

    with open('json_obj.json') as file:
        dict_json = json.load(file)  # dict

    for key in dict_json['drinks'][0]:  # for all values in json
        if dict_json['drinks'][0][key] is not None:
            if key.startswith('strIngredient'):
                keys.append(key)

    return keys


def proportions():
    keys = list()

    with open('json_obj.json') as file:
        dict_json = json.load(file)  # dict

    for key in dict_json['drinks'][0]:  # for all values in json
        if dict_json['drinks'][0][key] is not None:
            if key.startswith('strMeasure'):
                keys.append(key)

    return keys
