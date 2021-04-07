import json

tournaments = {
    'aeriflot': 2010,
    'fide': 2018,
    'pros': 2016
}

json_data = json.dumps(tournaments, indent=3)
print(type(json_data))
print(json_data)

loaded = json.loads(json_data)
print(type(loaded))
print(loaded)