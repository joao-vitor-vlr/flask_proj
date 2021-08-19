import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

cur.execute("INSERT INTO tabelas (nome, content) VALUES (?, ?)",
            ('tird Post', 'Content for the first post')
            )

cur.execute("INSERT INTO tabelas (nome, content) VALUES (?, ?)",
            ('fourth Post', 'Content for the second post')
            )

connection.commit()
connection.close()