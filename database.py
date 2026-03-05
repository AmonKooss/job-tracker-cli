import sqlite3

#conexão com o banco de dados
conexão =sqlite3.connect('vagas.db')

curr = conexão.cursor()

curr.execute("""CREATE TABLE IF NOT EXISTS vagas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            empresa TEXT NOT NULL,
            cargo TEXT NOT NULL,
            link TEXT,
            status TEXT
    )""")