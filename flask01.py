# -*- coding: utf-8 -*-

# Importa bibliotecas.
from flask import Flask, jsonify, request, abort, make_response, json, Response
import sqlite3

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
    try:
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        sql = "SELECT * FROM owner WHERE owner_status != 'off'"
        cursor.execute(sql)
        data = cursor.fetchall()
        conn.close()
        res = []
        for res_temp in data:
            res.append(dict(res_temp))
        if res:
            return res
        else:
            return {"error": "Nenhum item encontrado"}
    except sqlite3.Error as error:
        return {"error": f"Erro ao acessar o banco de dados: {str(error)}"}
    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}


# Roda aplicativo Flask.
if __name__ == "__main__":
    app.run(debug=True)