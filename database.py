<<<<<<< HEAD
import sqlite3

def connect():
    """Conecta ao banco de dados SQLite e retorna a conexão e o cursor."""
    connection = sqlite3.connect('estoque.db')
    cursor = connection.cursor()
    return connection, cursor

def create_table():
    """Cria a tabela 'produtos' no banco de dados, se não existir."""
    conn, cursor = connect()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
=======
import sqlite3

def connect():
    """Conecta ao banco de dados SQLite e retorna a conexão e o cursor."""
    connection = sqlite3.connect('estoque.db')
    cursor = connection.cursor()
    return connection, cursor

def create_table():
    """Cria a tabela 'produtos' no banco de dados, se não existir."""
    conn, cursor = connect()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
>>>>>>> 0b853dd20a0d238227f6ecb2188868975cd6ccae
