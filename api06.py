# -*- coding: utf-8 -*-

import json
import sqlite3
import os

database = "./temp_db.db"


def get_all_owners():
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
    return res


def get_one_owner(id):
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    sql = "SELECT * FROM owner WHERE owner_status != 'off' AND owner_id = ?"
    cursor.execute(sql, (id,))
    data = cursor.fetchone()
    conn.close()
    if data:
        return dict(data)
    else:
        return {"error": "Usuário não encontrado."}


os.system("cls")

# print(json.dumps(get_all_owners(), ensure_ascii=False, indent=2))

print(json.dumps(get_one_owner(5), ensure_ascii=False, indent=2))