import json
with open('music.json') as data_file:
    specifications = json.load(data_file)
type=specifications["type"]
print(type)
