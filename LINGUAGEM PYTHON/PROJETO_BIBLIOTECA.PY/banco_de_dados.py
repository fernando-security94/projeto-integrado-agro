# Criando banco de dados com sqlite3
import sqlite3

# Criando o banco de dados e sua conexão com .connect()
# e executa os comandos SQL
# Vou modular a criação da tabela em uma função
def criar_banco():
    conectar_banco_dados = sqlite3.connect("biblioteca.db")
    cursor = conectar_banco_dados.cursor()

# Criando a tabela de livros com os atributos
# titulo, autor, ano e se está disponível
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano INTEGER NOT NULL,
        status TEXT DEFAULT 'disponivel'
    )
    ''')

    # Criar tabela de usuario com ID, nome e contato
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        contato TEXT
        )
    ''')


# Salva as alterações no banco de dados
    conectar_banco_dados.commit()
    conectar_banco_dados.close()

    print("O banco de dados e suas respectivas tabelas foram criados com sucesso!")

