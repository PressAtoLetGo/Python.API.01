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
    }, {
        "id": 4,
        "name": "Objeto",
        "description": "Objeto aleatorio",
        "location": "Numa gaveta"
    }, {
        "id": 5,
        "name": "Algo",
        "description": "Alguma coisa",
        "location": "Em algum lugar"
    }, {
        "id": 6,
        "name": "Isto",
        "description": "Isso mesmo",
        "location": "Esta ali"
    }, {
        "id": 7,
        "name": "Aquilo",
        "description": "Ali mesmo",
        "location": "Naquele canto"
    },
]


def get_all():
    return json.dumps(items, indent=2)


def get_one(id):
    try:
        id = int(id)
    except:
        print("ID inválido!")
        return False
    for item in items:
        if item.get("id") == id:
            return json.dumps(item, indent=2)


# print(get_all())
input_id = (input("Digite o ID do item: "))
#print(get_one(input_id))