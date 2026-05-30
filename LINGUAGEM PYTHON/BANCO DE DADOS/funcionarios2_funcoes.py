# criar ou conectar banco de dados, adicionar funcionarios
# com id, nome, cargo e salario

import sqlite3

# conectar ou criar banco de dados se nao existir
conn = sqlite3.connect("funcionarios2.db")

# criar cursor que vai percorrer o banco de dados
cursor = conn.cursor()

# criar tabelas no banco de dados
# criar tabelas no banco de dados
cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cargo TEXT,
        salario REAL
    )               
''')



# Inserir novo funcionario na tabela com seus atributos
novo_func1 = (1, "Fernando", "Analista", 5000)

cursor.execute("INSERT or IGNORE INTO funcionarios(id, nome, cargo, salario) VALUES(?, ?, ?, ?)", novo_func1)
conn.commit()

# Consultar funcionarios
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()
print("Funcionários cadastrados:")
for funcionario in funcionarios:
    print(funcionario)

conn.commit()

novo_salario = (7500, 1)
cursor.execute("UPDATE funcionarios SET salario=? WHERE id = ?", novo_salario)
conn.commit()


novo_func2 = (2,"Poliane", "Gerente", 12000)
cursor.execute("INSERT OR IGNORE into funcionarios(id, nome, cargo, salario) VALUES(?,?,?,?)", novo_func2)
conn.commit()


cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()
print("Funcionarios cadastrados:\n")
for funcionario in funcionarios:
    print(funcionario)

conn.commit()

novo_salario_2 = (15000, 2)
cursor.execute("UPDATE funcionarios SET salario=? WHERE id = ?", novo_salario_2)
conn.commit()
print()

id = 2
cursor.execute("SELECT * FROM funcionarios WHERE id =?", (id,))
funcionario = cursor.fetchone()
print("Funcionario com id 2:")
if funcionario:
    print(funcionario)
else:
    print("Não foi encontrado nenhum funcionário com esse ID")
conn.commit()
print()

id_10 = 10
cursor.execute("SELECT * FROM funcionarios WHERE id =?", (id_10,))
funcionario = cursor.fetchone()
print("Funcionario com id 10:")
if funcionario:
    print(funcionario)
else:
    print("Não foi encontrado nenhum funcionário com esse ID")

conn.commit()
