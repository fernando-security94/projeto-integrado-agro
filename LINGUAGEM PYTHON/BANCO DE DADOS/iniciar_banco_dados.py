# exemplo de criacao de banco de dados
import sqlite3

# conectar ao banco de dados ou criar se nao existe
conn = sqlite3.connect("exemplo.db")

# cria cursor que percorre o banco de dados
cursor = conn.cursor()

# definir o comando SQL para criar a tabela
create_table = """
    CREATE TABLE IF NOT EXISTS Produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER

)
"""
# executar o comando SQL para criar tabela
cursor.execute(create_table)

# confirmar os comandos
conn.commit()

# encerrar a conexao com o banco de dados
conn.close()

# Operação CRUD(CREATE, READ, UPDATE, DELETE)

conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

# criando novo produto
novo_produto = ('camiseta', 19.55, 50)

# comando SQL para inserir novo produto na tabela
# inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)"

# cursor.execute(inserir_produto, (novo_produto))

# conn.commit()
# conn.close()


# Recuperar todos os produtos da tabela produtos com fetchall

conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

# comando para selecionar os produtos
selecionar_produtos = "SELECT * FROM Produtos"
cursor.execute(selecionar_produtos)
produtos = cursor.fetchall()

for produto in produtos:
    print(produto)

conn.close()

# exemplo de atualizar preço de produto
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

# novo preco e id do produto que sera atualizado
novo_preco = 10
produto_id = 2
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco, produto_id))

# novo preco e id do produto que sera atualizado
novo_preco3 = 20
produto_id = 3
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco3, produto_id))

# novo preco e id do produto que sera atualizado
novo_preco4 = 20
produto_id = 4
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco4, produto_id))


# novo preco e id do produto que sera atualizado

novo_preco5 = 30
produto_id = 5
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco5, produto_id))


# novo preco e id do produto que sera atualizado

novo_preco6 = 20
produto_id = 6
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco6, produto_id))


# novo preco e id do produto que sera atualizado
novo_preco7 = 40.25
produto_id = 7
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco7, produto_id))

# novo preco e id do produto que sera atualizado

novo_preco8 = 50
produto_id = 8
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco8, produto_id))



novo_preco9 = 50
produto_id = 9
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco9, produto_id))



novo_preco10 = 50
produto_id = 10
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco10, produto_id))



novo_preco11 = 50
produto_id = 11
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco11, produto_id))


novo_preco12 = 50
produto_id = 12
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
cursor.execute(atualizar_preco, (novo_preco12, produto_id))

conn.commit()
conn.close()

# recuperar todos os produtos da Tabela produtos
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

selecionar_produtos = "SELECT * FROM Produtos"
cursor.execute(selecionar_produtos)

for produto in produtos:
    print(produto)

conn.commit
conn.close

# excluindo produto pelo id
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

produto_id = 12
excluir_produto = "DELETE from Produtos WHERE id = ?"
cursor.execute(excluir_produto, (produto_id,))

conn.commit()
conn.close()


# exibir produtos após a exclusao
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

selecionar_produtos = "SELECT * FROM Produtos"
cursor.execute(selecionar_produtos)

for produto in produtos:
    print(produto)

conn.commit()
conn.close()
