import json


def ingredients():
    strIngredient = list()
    strMeasure = list()

    with open("json_obj.json") as file:
        dict_json = json.load(file)  # dict

    for key in dict_json["drinks"][0]:  # for all values in json
        if dict_json["drinks"][0][key] is not None:
            if key.startswith("strIngredient"):
                strIngredient.append(key)
            elif key.startswith("strMeasure"):
                strMeasure.append(key)

    sum_measure_and_ingredient = list()

    # summing 2 values json
    for i in range(len(strIngredient)):
        try:
            sum_measure_and_ingredient.append(
                dict_json["drinks"][0][strMeasure[i]]
                + dict_json["drinks"][0][strIngredient[i]]
            )
        except IndexError:
            pass
            sum_measure_and_ingredient.append(dict_json["drinks"][0]["strIngredient3"])

    return sum_measure_and_ingredient
