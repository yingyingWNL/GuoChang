import json

with open('x.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)