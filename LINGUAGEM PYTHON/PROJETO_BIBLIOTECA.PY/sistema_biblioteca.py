# Nesse arquivo vamos criar funções que vão 
# interagir diretamente com o banco de dados
import sqlite3


# Criação de uma função que adiciona tabelas automaticamente
# ao executar iniciar
def criar_tabelas():
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER NOT NULL,
            ano INTEGER NOT NULL,
            estoque INTEGER NOT NULL,
            status TEXT DEFAULT 'dispnivel'
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            contato TEXT NOT NULL    
        )
    ''')

    conexao.commit()
    conexao.close()


# função que adiciona livros à biblioteca e realiza a
# conexão com banco e 
# executa os comandos SQL
def adicionar_livro(titulo, autor, ano, estoque):
    conexao_com_banco = sqlite3.connect("biblioteca.db")
    cursor = conexao_com_banco.cursor()

    # execução que insere livros com INSERT
    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano, estoque, status)
        VALUES (?, ?, ?, ?, 'disponivel')
    ''', (titulo, autor, ano, estoque))

    # Seguindo boas práticas de salvar
    # e encerrar a conexão
    conexao_com_banco.commit()
    conexao_com_banco.close()

    print(f'Livro {titulo} adicionado à biblioteca!')

# criando função que retorna todos
# os livros disponíveis na biblioteca
def listar_livros():
    conectar_banco_dados = sqlite3.connect("biblioteca.db")
    cursor = conectar_banco_dados.cursor()

    # Percorre todos os índices dos livros cadastrados
    cursor.execute("SELECT titulo, autor, ano, estoque FROM livros")
    
    # return TODOS os resultados da consulta
    livros = cursor.fetchall()

    # condicional para checar
    # se há livros antes de print
    # Os valores entre [] como índices são as colunas da tabela
    if livros:
        print("\nLivros disponíveis:\n")
        for livro in livros:
            print(f'\nTitulo: {livro[0]}.\nAutor: {livro[1]}.\nAno: {livro[2]}.\nEstoque: {livro[3]}\n')
    else:
        print("Nenhum livro cadastrado.")

    conectar_banco_dados.close()
    return livros

# criando uma função que simula o aluguel de um livro
# ao ser executada, ela será basicamente uma função que
# remove o livro do banco de dados
def alugar_livro(id_usuario, nome_livro):
    conectar_banco_dados = sqlite3.connect("biblioteca.db")
    cursor = conectar_banco_dados.cursor()

    # verifica se o livro esta disponível
    cursor.execute("SELECT id, titulo, estoque FROM livros WHERE titulo = ? AND estoque > 0", (nome_livro,))
    livro = cursor.fetchone()

    if livro:
        livro_id, titulo, estoque = livro
        cursor.execute("UPDATE livros SET estoque = estoque - 1 WHERE id = ?", (livro_id,))
        
        if estoque == 1:
            cursor.execute("UPDATE livros SET status = 'alugado' WHERE id = ?", (livro_id,))
        
        # Confirma o aluguel do livro    
        conectar_banco_dados.commit()
        print("Livro alugado com sucesso!")
    else:
        print("Estoque indisponível!")

    # encerra a conexão com o banco de dados 
    conectar_banco_dados.close()


def devolver_livro(id_usuario, nome_livro):
    conectar_banco_dados = sqlite3.connect("biblioteca.db")
    cursor = conectar_banco_dados.cursor()

    # Busca o livro alugado pelo nome
    cursor.execute("SELECT id, titulo, estoque FROM livros WHERE titulo = ?", (nome_livro,))
    resultado = cursor.fetchone()

    if resultado:
        livro_id, titulo, estoque = resultado

        # Atualiza o estoque e status do livro
        cursor.execute("UPDATE livros SET estoque = estoque + 1 WHERE id = ?", (livro_id,))
        cursor.execute("UPDATE livros SET status = 'disponivel' WHERE id = ? AND estoque > 0", (livro_id,))

        # Confirma a devolução do livro
        conectar_banco_dados.commit()
        print(f'O livro "{titulo}" foi devolvido com sucesso. Obrigado!')
    else:
        print("Nenhum livro correspondente encontrado para devolução.")

    conectar_banco_dados.close()


def cadastro_usuario(nome, contato):
    conexao_com_banco = sqlite3.connect("biblioteca.db")
    cursor = conexao_com_banco.cursor()

    cursor.execute('''
        INSERT INTO usuarios (nome, contato) VALUES (?, ?) ''', 
        (nome, contato))
    
    conexao_com_banco.commit()
    conexao_com_banco.close()
    print("Usuário cadastrado com sucesso")


# Criação de uma função que exibe o relatório
# com qtde de livros disponíveis, livros emprestados
# e usuários cadastrados
def relatorio_geral():
    conexao_com_banco = sqlite3.connect('biblioteca.db')
    cursor = conexao_com_banco.cursor()

    relatorio = ""
    # exibição dos livros disponíveis
    relatorio += "LIVROS DISPONÍVEIS:\n"
    cursor.execute('SELECT id, titulo, autor, ano FROM livros WHERE status = "disponivel"')
    livros_disponiveis = cursor.fetchall()
    if livros_disponiveis:
        for livro in livros_disponiveis:
            relatorio += f'ID: {livro[0]}, {livro[1]} - {livro[2]} ({livro[3]})'
    else:
        relatorio += "\nNENHUM LIVRO DISPONÍVEL!"

    relatorio += "\n--------------------------------------\n"

    # exibição dos livros alugados
    relatorio += "\nLIVROS ALUGADOS:"
    cursor.execute("SELECT id, titulo, autor, ano FROM livros WHERE status = 'alugado'")
    livros_alugados = cursor.fetchall()
    if livros_alugados:
        for livro in livros_alugados:
            relatorio += f'ID: {livro[0]}, {livro[1]} - {livro[2]} ({livro[3]})'
    else:
        relatorio += "\nNENHUM LIVRO ALUGADO!"   

    relatorio += "\n--------------------------------------\n"

    # exibição dos usuários cadastrados
    cursor.execute("SELECT * FROM usuarios")  # ou SELECT *
    usuarios = cursor.fetchall()
    if usuarios:
        for usuario in usuarios:
            relatorio += f'ID: {usuario[0]}, Nome: {usuario[1]}, contato: {usuario[2]}\n'
    else:
        relatorio += "\nNENHUM USUÁRIO CADASTRADO!"
    
    conexao_com_banco.close()
    return relatorio
    

# Chamando a função que cria as tabelas
# na execução do módulo
criar_tabelas()
