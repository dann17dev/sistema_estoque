import sqlite3
import csv

def connect():
    """Conecta ao banco de dados SQLite e retorna o objeto de conexão e o cursor."""
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    return conn, cursor

def adicionar_produto(nome, preco, quantidade):
    """Adiciona um novo produto ao banco de dados."""
    conn, cursor = connect()
    cursor.execute('INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)', 
                   (nome, preco, quantidade))
    conn.commit()
    conn.close()

def remover_produto(produto_id):
    """Remove um produto do banco de dados com base no ID."""
    conn, cursor = connect()
    cursor.execute('DELETE FROM produtos WHERE id = ?', (produto_id,))
    conn.commit()
    conn.close()

def editar_produto(produto_id, nome=None, preco=None, quantidade=None):
    """Edita as informações de um produto no banco de dados."""
    conn, cursor = connect()
    
    if nome:
        cursor.execute('UPDATE produtos SET nome = ? WHERE id = ?', (nome, produto_id))
    if preco:
        cursor.execute('UPDATE produtos SET preco = ? WHERE id = ?', (preco, produto_id))
    if quantidade:
        cursor.execute('UPDATE produtos SET quantidade = ? WHERE id = ?', (quantidade, produto_id))
    
    conn.commit()
    conn.close()

def listar_produtos():
    """Exibe todos os produtos cadastrados no banco de dados."""
    conn, cursor = connect()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if produtos:
        print("\n=== Produtos no Estoque ===")
        for produto in produtos:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}, Quantidade: {produto[3]}")
        print("============================\n")
    else:
        print("\nNão há produtos cadastrados.\n")

    conn.close()

def pesquisar_produto(criterio, valor):
    """Pesquisa um produto pelo ID ou pelo Nome."""
    conn, cursor = connect()
    
    if criterio == 'id':
        cursor.execute('SELECT * FROM produtos WHERE id = ?', (valor,))
    elif criterio == 'nome':
        cursor.execute('SELECT * FROM produtos WHERE nome LIKE ?', ('%' + valor + '%',))
    
    produtos = cursor.fetchall()
    
    if produtos:
        print("\n=== Resultado da Pesquisa ===")
        for produto in produtos:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}, Quantidade: {produto[3]}")
        print("============================\n")
    else:
        print("\nNenhum produto encontrado.\n")
    
    conn.close()

def exportar_para_csv():
    """Exporta os produtos cadastrados para um arquivo CSV."""
    conn, cursor = connect()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    
    with open('relatorio_estoque.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Nome', 'Preço', 'Quantidade'])  # Cabeçalhos do CSV
        
        for produto in produtos:
            writer.writerow(produto)  # Escreve cada produto no CSV
    
    print("Relatório exportado com sucesso para 'relatorio_estoque.csv'.")
    
    conn.close()
