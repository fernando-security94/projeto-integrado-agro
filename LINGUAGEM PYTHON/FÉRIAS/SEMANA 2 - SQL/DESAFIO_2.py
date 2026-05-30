'''🔸 Desafio 2 – SQL na Prática (Terça)
🎯 Contexto:
Você trabalha com uma base de dados de vendas. Precisa responder perguntas usando SQL.

🧠 Você vai treinar:
Criação de banco com SQLite

Escrita de queries SQL para análise

💻 Desafio:
Crie uma tabela vendas com as colunas: id, data, produto, quantidade, preco_unitario

Insira pelo menos 5 registros fictícios

Responda:

Qual o total vendido por produto?

Quais vendas aconteceram depois de uma data X?
'''
import sqlite3

# # Conectar ao banco
# conn = sqlite3.connect('vendas.db')
# cursor = conn.cursor()

# # Criar tabela
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS vendas (
#     id INTEGER PRIMARY KEY,
#     data TEXT,
#     produto TEXT,
#     quantidade INTEGER,
#     preco_unitario REAL
# )
# ''')

# # Inserir dados
# cursor.execute('''
# INSERT INTO vendas (data, produto, quantidade, preco_unitario)
# VALUES ('2025-06-01', 'Camiseta', 5, 50.00)
# ''')

# conn.commit()

# cursor.execute('''
# INSERT OR IGNORE INTO vendas (data, produto, quantidade, preco_unitario)
# VALUES ('2025-07-01', 'Calça', 3, 100.00)
# ''')

# conn.commit()

# cursor.execute('''
# INSERT OR IGNORE INTO vendas (data, produto, quantidade, preco_unitario)
# VALUES ('2025-08-01', 'Boné', 34, 30.00)
# ''')

# conn.commit()


# cursor.execute('''
# INSERT OR IGNORE INTO vendas (data, produto, quantidade, preco_unitario)
# VALUES ('2025-09-01', 'Camiseta', 1, 100.00)
# ''')

# conn.commit()

# cursor.execute('''
# INSERT OR IGNORE INTO vendas (data, produto, quantidade, preco_unitario)
# VALUES ('2025-10-01', 'Calça', 7, 100.00)
# ''')

# conn.commit()


# # Qual o total vendido por produto?
# cursor.execute('''
#     SELECT produto, SUM(quantidade * preco_unitario) AS total_vendido
#     FROM vendas
#     GROUP BY produto          
# ''')
# resultados = cursor.fetchall()

# for produto, total in resultados:
#     print(f'Produto: {produto} | Total vendido: R${total:.2f}')

# conn.close()

# # conn = sqlite3.connect('vendas.db')
# # cursor = conn.cursor()

# # cursor.execute('DELETE FROM vendas')
# # conn.commit()
# # conn.close()

# # print("Valores excluídos com sucesso!")


# # Função para limpar tabela 
# def limpar_tabela(nome_tabela):
#     cursor.execute(f'DELETE FROM {nome_tabela}')
#     cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{nome_tabela}"')
#     conn.commit()
#     print(f'Tabela "{nome_tabela}" limpa e ID resetado.')


# Versão otimizada
import sqlite3

# Conectar
conn = sqlite3.connect('vendas.db')
cursor = conn.cursor()

# Criar tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    produto TEXT,
    quantidade INTEGER,
    preco_unitario REAL
)
''')

# Função para limpar tabela e resetar ID
def limpar_tabela(nome_tabela):
    try:    
        cursor.execute(f'DELETE FROM {nome_tabela}')
        # Tentar resetar o autonicrement, se existit
        cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{nome_tabela}"')
        conn.commit()
        print(f'Tabela "{nome_tabela}" limpa e ID resetado.')
    except sqlite3.OperationalError as error:
        if 'no such table: sqlite_sequence' in str(error):
            print(f'Tabela "{nome_tabela}" limpa, mas sqlite_sequence não existe (ID não resetado).')
        else:
            raise error
# Limpar antes de inserir
limpar_tabela('vendas')

# Inserir dados
dados = [
    ('2025-06-01', 'Camiseta', 5, 50.00),
    ('2025-07-01', 'Calça', 3, 100.00),
    ('2025-08-01', 'Boné', 34, 30.00),
    ('2025-09-01', 'Camiseta', 1, 100.00),
    ('2025-10-01', 'Calça', 7, 100.00)
]

cursor.executemany('''
    INSERT INTO vendas (data, produto, quantidade, preco_unitario)
    VALUES (?, ?, ?, ?)
''', dados)

conn.commit()

# Consulta: total vendido por produto
cursor.execute('''
    SELECT produto, SUM(quantidade * preco_unitario) AS total_vendido
    FROM vendas
    GROUP BY produto
''')

resultados = cursor.fetchall()

for produto, total in resultados:
    print(f'Produto: {produto} | Total vendido: R${total:.2f}')

conn.close()
