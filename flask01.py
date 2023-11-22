# -*- coding: utf-8 -*-

# Importa bibliotecas.
from flask import Flask, jsonify, request, abort, make_response, json, Response
import sqlite3

# Cria aplicativo Flask.
app = Flask(__name__)

# Configura o character set das transações HTTP para UTF-8.
json.provider.DefaultJSONProvider.ensure_ascii = False

# Especifica a base de dados SQLite3.
database = "./temp_db.db"

# Obtém todos os registros válidos de 'item'.
# Request method → GET
# Request endpoint → /items
# Response → JSON


@app.route("/items", methods=["GET"])
def get_all():
    try:
        # Conectar ao banco de dados SQLite.
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Consulta SQL para selecionar todos os itens ativos.
        sql = "SELECT * FROM item WHERE item_status != 'off'"
        cursor.execute(sql)
        rows_data = cursor.fetchall()
        conn.close()

        # Converte os resultados em uma lista de dicionários.
        list_data = []
        for row_data in rows_data:
            list_data.append(dict(row_data))

        # Retorna os dados ou um erro " HTTP 400 - Bad Request" se nenhum item for encontrado.
        if list_data:
            return list_data
        else:
            return {"error": "Nenhum item encontrado"}, 400

    # Tratamento de exceções.
    except sqlite3.Error as error:
        return {"error": f"Erro ao acessar o banco de dados: {str(error)}"}, 500
    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}, 500


@app.route("/items/<int:id>", methods=["GET"])
def get_one(id):
    try:
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        sql = "SELECT * FROM item WHERE item_status != 'off' AND item_id = ?"
        cursor.execute(sql, (id,))
        row_data = cursor.fetchone()
        conn.close()
        if row_data:
            return dict(row_data)
        else:
            return {"error": "Registro não encontrado."}, 400

    except sqlite3.Error as error:
        return {"error": f"Erro ao acessar o banco de dados: {str(error)}"}
    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}


@app.route("/items", methods=["POST"])
def create():
    try:
        post_data = request.get_json()
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        sql = """
            INSERT INTO item 
                (item_name, item_description, item_location, item_owner)
            VALUES
                (?, ?, ?, ?);
            """
        cursor.execute(sql, (
            post_data['item_name'],
            post_data['item_description'],
            post_data['item_location'],
            post_data['item_owner'],
        ))
        conn.commit()
        conn.close()
        return {"sucess": "Item cadastrado com sucesso."}

    except sqlite3.Error as error:
        return {"error": f"Erro ao acessar o banco de dados: {str(error)}"}
    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}


# Roda aplicativo Flask.
if __name__ == "__main__":
    app.run(debug=True)