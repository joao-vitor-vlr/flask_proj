from flask import Flask, render_template
from flask import request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    tabela = conn.execute('SELECT * FROM tabelas').fetchall()
    conn.close()
    return render_template('dashboard.html', tabela=tabela)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
