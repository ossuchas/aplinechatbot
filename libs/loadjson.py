import json


def loadjsonfile():

    with open('static/json/stringlist.json') as json_file:
        data = json.load(json_file)

    print(data)
    return data
