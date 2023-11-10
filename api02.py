import json

items = [
    {
        "id": 1,
        "name": "Coisa",
        "description": "Apenas uma coisa",
        "location": "Em uma caixa"
    }, {
        "id": 2,
        "name": "Tranqueira",
        "description": "Apenas uma tranqueira",
        "location": "Em um gaveteiro"
    }, {
        "id": 3,
        "name": "Coisinha",
        "description": "Apenas uma coisinha",
        "location": "Na esquina"
    }
]

def get_all():
    return json.dumps(items, indent=2)

def get_one(id):
    var_json = json.dumps(items[id], indent=2)
    return var_json
    
print(get_all())
print(get_one(0))