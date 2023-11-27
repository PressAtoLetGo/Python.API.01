# -*- coding: utf-8 -*-


from flask import Flask, jsonify, request, abort, make_response, json, Response
import sqlite3


app = Flask(__name__)

json.provider.DefaultJSONProvider.ensure_ascii = False

database = "./temp_db.db"


def prefix_remove(prefix, data):
    new_data = {}
    
    for key, value in data.items():
        if key.startswith(prefix):
            new_key = key[len(prefix):]
            new_data[new_key] = value
            
        else:
            new_data[key] = value
    return new_data


@app.route("/owners", methods=["GET"])
def get_all():
    try:
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM owner WHERE owner_status != 'off' ORDER BY owner_name")
        owners_rows = cursor.fetchall()
        conn.close()
        owners = []
        
        for owner in owners_rows:
            owners.append(dict(owner))

        if owners:
            new_owners = [prefix_remove('owner_', owner) for owner in owners]
            return new_owners, 200

        else:
            return {"error": "Nenhum usuário encontrado"}, 404

    except sqlite3.Error as e:
        return {"error": f"Erro ao acessar o banco de dados: {str(e)}"}, 500

    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}, 500


@app.route("/owners/<int:id>", methods=["GET"])
def get_one(id):
    try:
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM owner WHERE owner_id = ? AND owner_status != 'off'", (id,))
        owner_row = cursor.fetchone()
        conn.close()

        if owner_row:
            owner = dict(owner_row)
            new_owner = prefix_remove('owner_', owner)
            return new_owner, 200

        else:
            return {"error": "Usuário não encontrado"}, 404

    except sqlite3.Error as e:
        return {"error": f"Erro ao acessar o banco de dados: {str(e)}"}, 500

    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}, 500


@app.route("/owners", methods=["POST"])
def create():
    try:
        new_owner = request.get_json()
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT owner_email FROM owner WHERE owner_email = ? AND owner_status != 'off'", (new_owner['email'],))
        owner_row = cursor.fetchone()

        if owner_row:
            conn.close()
            return {"error": "Registro já existe"}, 200

        else:
            sql = "INSERT INTO owner (owner_name, owner_email, owner_password, owner_birth) VALUES (?, ?, ?, ?)"
            sql_data = (
                new_owner['name'],
                new_owner['email'],
                new_owner['password'],
                new_owner['birth']
            )
            cursor.execute(sql, sql_data)
            inserted_id = int(cursor.lastrowid)
            conn.commit()
            conn.close()
            return {"success": "Registro criado com sucesso", "id": inserted_id}, 201

    except json.JSONDecodeError as e:
        return {"error": f"Erro ao decodificar JSON: {str(e)}"}, 500

    except sqlite3.Error as e:
        return {"error": f"Erro ao acessar o banco de dados: {str(e)}"}, 500

    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}, 500


@app.route("/owners/<int:id>", methods=["PUT", "PATCH"])
def edit(id):
    try:
        owner_json = request.get_json()
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT owner_id FROM owner WHERE owner_id = ? AND owner_status != 'off'", (id,))
        owner_row = cursor.fetchone()

        if owner_row:
            set_clause = ', '.join(
                [f"owner_{key} = ?" for key in owner_json.keys()])

            sql = f"UPDATE owner SET {set_clause} WHERE owner_id = ? AND owner_status = 'on'"
            cursor.execute(sql, (*owner_json.values(), id))
            conn.commit()
            conn.close()
            return {"success": "Registro atualizado com sucesso", "id": id}, 201

        else:
            conn.close()
            return {"error": "Registro não existe"}, 404

    except json.JSONDecodeError as e:
        return {"error": f"Erro ao decodificar JSON: {str(e)}"}, 500

    except sqlite3.Error as e:
        return {"error": f"Erro ao acessar o banco de dados: {str(e)}"}, 500

    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}, 500


@app.route("/owners/<int:id>", methods=["DELETE"])
def delete(id):
    try:
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT owner_id FROM owner WHERE owner_id = ? AND owner_status != 'off'", (id,))
        owner_row = cursor.fetchone()

        if owner_row:
            cursor.execute(
                "UPDATE owner SET owner_status = 'off' WHERE owner_id = ?", (id,))
            conn.commit()
            conn.close()
            return {"success": "Registro apagado com sucesso", "id": id}, 200

        else:
            conn.close()
            return {"error": "Usuário não existe"}, 404

    except sqlite3.Error as e:
        return {"error": f"Erro ao acessar o banco de dados: {str(e)}"}, 500

    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}, 500


@app.route("/items_by_owner/<int:id>", methods=["GET"])
def get_items(id):
    try:
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM item WHERE item_status != 'off' AND item_owner = ? ORDER BY item_date DESC", (id,))
        items_rows = cursor.fetchall()
        conn.close()
        items = []

        for item in items_rows:
            items.append(dict(item))

        if items:
            new_items = [prefix_remove('item_', item) for item in items]
            return new_items, 200

        else:
            return {"error": "Usuário não encontrado"}, 404

    except sqlite3.Error as e:
        return {"error": f"Erro ao acessar o banco de dados: {str(e)}"}, 500

    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}, 500


if __name__ == "__main__":
    app.run(debug=True)
