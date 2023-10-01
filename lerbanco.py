import sqlite3


def LerBanco():

    conn = sqlite3.connect('./storage.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')

    dados = cursor.fetchall()

    return dados


def MontandoJson(dados):
    lista = []
    for i in dados:
        data = {
            'id': i[0],
            'name': i[1],
            'resumo': i[3],
            'nivel': i[3],
            'vila': i[4],
            'tecnicas': i[5],
            'url': i[6]
        }
        lista.append(data)
    return lista
