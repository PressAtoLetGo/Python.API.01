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
    var_json = json.dumps(items, indent=2)
    print(var_json)

def get_one(id):
    var_json = json.dumps(items[id], indent=2)
    print(var_json)
    
get_all()
get_one(0)