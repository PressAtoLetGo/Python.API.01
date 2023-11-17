# -*- coding: utf-8 -*-

# Importa as bibliotecas de dependências.
import json
import sqlite3
import os

# Define o banco de dados.
database = "./temp_db.db"

# Obtém todos os 'item' válidos do banco de dados.
# Retorna como uma 'list' de 'dict'.


def get_all_items():
    try:
        # Cria uma conexão com o banco de dados SQLite.
        conn = sqlite3.connect(database)

        # Define que a troca de dados entre Python e SQQLite acontece na forma de Row.
        conn.row_factory = sqlite3.Row

        # Um cursor que aponta para a(s) linha(s) do SQLite.Row que está(ão) sendo acessadas.
        cursor = conn.cursor()

        # Query para consultar os registros na tabela 'item'.
        sql = "SELECT * FROM item WHERE item_status != 'off'"

        # Executa o SQL acima no banco de dados.
        cursor.execute(sql)

        # "Puxa" os dados do cursor para o Python.
        data = cursor.fetchall()

        # Desconecta do banco de dados.
        # Guardar recursos, aumenta a segurança, evita corrupção de dados.
        conn.close()

        # Uma 'list' para armazenar as SQLite.Row na forma de 'dict'.
        res = []

        # Loop que obtém cada SQLite.Row da memória (data).
        for res_temp in data:

            # Converte a SQLite.Row em 'dict' e adiciona no final de 'res' (list).
            res.append(dict(res_temp))

        # Retornar os dados ou um erro se nenhum item for encontrado.
        if res:
            return res
        else:
            return {"error": "Nenhum item encontrado"}

    # Tratamento de exceções.
    except sqlite3.Error as error:
        return {"error": f"Erro ao acessar o banco de dados: {str(error)}"}
    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}


# Obtém apenas um item válido do banco de dados.


def get_one_item(id):
    try:
        # Cria uma conexão com o banco de dados SQLite.
        conn = sqlite3.connect(database)

        # Define que a troca de dados entre Python e SQQLite acontece na forma de Row.
        conn.row_factory = sqlite3.Row

        # Um cursor que aponta para a(s) linha(s) do SQLite.Row que está(ão) sendo acessadas.
        cursor = conn.cursor()

        # Query para consultar os registros na tabela 'item'.
        sql = "SELECT * FROM item WHERE item_status != 'off' AND item_id = ?"

        # Executa o código passando o valor do ID.
        cursor.execute(sql, (id,))
        data = cursor.fetchone()
        conn.close()

        # Se o registro existir...
        if data:
            # Retorna o registro em um 'dict'.
            return dict(data)
        # Se o registro não existir...
        else:
            # Retorna um erro.
            return {"error": "Registro não encontrado."}

    # Tratamento de exceções.
    except sqlite3.Error as error:
        return {"error": f"Erro ao acessar o banco de dados: {str(error)}"}
    except Exception as error:
        return {"error": f"Erro inesperado: {str(error)}"}


# Limpa o console.
os.system("cls")

# Exibe no console no formato JSON itens obtidos da função usando a tabela UTF-8.
print(json.dumps(get_all_items(), ensure_ascii=False, indent=2))
print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+')
print(json.dumps(get_one_item(4), ensure_ascii=False, indent=2))