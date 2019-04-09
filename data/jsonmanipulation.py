import json

with open("data/examplerole.json") as jsontest:
    data = jsontest.read()
    roles = json.loads(data)