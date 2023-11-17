# -*- coding: utf-8 -*-

# Importa bibliotecas.
from flask import Flask, jsonify, request, abort, make_response, json, Response


# Cria aplicativo Flask.
app = Flask(__name__)

# Configura o character set das transações HTTP para UTF-8.
json.provider.DefaultJSONProvider.ensure_ascii = False

# Define o banco de dados.
database = "./temp_db.db"

# Obtém todos os registros válidos de 'item'.
# Request method → GET
# Request endpoint → /items
# Response → JSON


@app.route("/items", methods=["GET"])
def get_all():
    return {"olá": "mundo"}


# Roda aplicativo Flask.
if __name__ == "__main__":
    app.run(debug=True)