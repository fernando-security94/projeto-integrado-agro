# criar um banco de dados que contenha contatos telefonicos

import sqlite3

# criacao do banco de dados caso nao exista
conn = sqlite3.connect("contatos.db")
cursor = conn.cursor()

# executa comando de criacao da tabela e suas 
# colunas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Contatos(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT,
      email TEXT,
      telefone TEXT
                                
        )

""")

dados_exemplo = [
    ('Fernando', 'fernando@email.com', '12349999'),
    ('Poliane', 'poliane@email.com', '12348888'),
    ('Fernando', 'fernando@email.com', '12347777')
]

# insere todos os contatos de dados_exemplo atraves de executemany()
# cursor.executemany('INSERT INTO Contatos(nome, email, telefone) VALUES(?, ?, ?)', dados_exemplo)

# conn.commit()
# conn.close

# Leitura de exibicao
cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()
print("Contatos: ")

for contato in contatos:
    print(contato)

# update contato com id 2
novo_numero = '99991234'
contato_id = 2


cursor.execute('UPDATE Contatos SET telefone = ? WHERE id = ?', (novo_numero, contato_id))



cursor.execute('SELECT * FROM Contatos')
contatos = cursor.fetchall()

print("Contatos atualizados: ")
for contato in contatos:
    print(contato)


conn.commit()
conn.close()


conn = sqlite3.connect("contatos.db")
cursor = conn.cursor()

# exclui os contatos de id entre 4 e 18
cursor.execute("DELETE from Contatos WHERE id BETWEEN 4 and 24")

cursor.execute('SELECT * From Contatos')
contatos = cursor.fetchall()

print("Tabela de contatos incial:")
for contato in contatos:
    print(contato)

conn.commit()
conn.close

