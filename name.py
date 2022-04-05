import json


def ingredients():
    keys = list()

    with open('json_obj.json') as file:
        dict_json = json.load(file)  # dict


    for key in dict_json['drinks'][0]:  # для всех значений в файле json
        if dict_json['drinks'][0][key] != None:
            if key.startswith('strIngredient'):
                keys.append(key)

    return keys


def proportions():
    keys = list()

    with open('json_obj.json') as file:
        dict_json = json.load(file)  # dict


    for key in dict_json['drinks'][0]:  # для всех значений в файле json
        if dict_json['drinks'][0][key] != None:
            if key.startswith('strMeasure'):
                keys.append(key)

    return keys
