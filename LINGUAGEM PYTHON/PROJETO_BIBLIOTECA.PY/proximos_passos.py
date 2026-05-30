# funcao para cadastrar usuarios
"""def cadastrar_usuario(nome, contato):
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO usuarios (nome, contato)
        VALUES (?, ?)
    ''', (nome, contato))

    conexao.commit()
    conexao.close()
    print("Usuário cadastrado com sucesso!")
"""


# funcao de relatorio geral
"""import sqlite3

def relatorio_geral():
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()

    print("\n=== 📗 LIVROS DISPONÍVEIS ===")
    cursor.execute("SELECT id, titulo, autor, ano FROM livros WHERE status = 'disponivel'")
    livros_disponiveis = cursor.fetchall()
    if livros_disponiveis:
        for livro in livros_disponiveis:
            print(f"ID: {livro[0]} | {livro[1]} - {livro[2]} ({livro[3]})")
    else:
        print("Nenhum livro disponível.")

    print("\n=== 📕 LIVROS EMPRESTADOS ===")
    cursor.execute("SELECT id, titulo, autor, ano FROM livros WHERE status = 'emprestado'")
    livros_emprestados = cursor.fetchall()
    if livros_emprestados:
        for livro in livros_emprestados:
            print(f"ID: {livro[0]} | {livro[1]} - {livro[2]} ({livro[3]})")
    else:
        print("Nenhum livro emprestado.")

    print("\n=== 👤 USUÁRIOS CADASTRADOS ===")
    cursor.execute("SELECT id, nome, contato FROM usuarios")
    usuarios = cursor.fetchall()
    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Contato: {usuario[2]}")
    else:
        print("Nenhum usuário cadastrado.")

    conexao.close()
"""


# criacao do menu interativo

"""from banco_de_dados import (
    criar_banco, adicionar_livro, listar_livros,
    alugar_livro, devolver_livro, cadastrar_usuario,
    relatorio_geral
)"""

"""criar_banco()

def menu():
    while True:
        print("\n=== SISTEMA DA BIBLIOTECA ===")
        print("[1] Adicionar livro")
        print("[2] Listar livros")
        print("[3] Alugar livro")
        print("[4] Devolver livro")
        print("[5] Cadastrar usuário")
        print("[6] Relatório - Livros disponíveis")
        print("[7] Relatório - Livros emprestados")
        print("[8] Relatório - Usuários cadastrados")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            estoque = int(input("Quantidade: "))
            adicionar_livro(titulo, autor, estoque)
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            livro_id = int(input("ID do livro a alugar: "))
            alugar_livro(livro_id)
        elif opcao == '4':
            livro_id = int(input("ID do livro a devolver: "))
            devolver_livro(livro_id)
        elif opcao == '5':
            nome = input("Nome do usuário: ")
            contato = input("Contato: ")
            cadastrar_usuario(nome, contato)
        elif opcao == '6':
            relatorio_livros_disponiveis()
        elif opcao == '7':
            relatorio_livros_emprestados()
        elif opcao == '8':
            relatorio_usuarios()
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
"""



# elaboração da interface
"""biblioteca/
├── banco_de_dados.py  ✅
├── interface.py       🆕 (Tkinter GUI aqui)
└── app.py             ✅ (opcional: menu terminal)
"""


"""
import tkinter as tk
from tkinter import messagebox, simpledialog
from banco_de_dados import (
    criar_banco,
    adicionar_livro,
    listar_livros,
    cadastrar_usuario,
    alugar_livro,
    devolver_livro,
    relatorio_geral
)

criar_banco()  # Garante que o banco está criado

# Funções que serão ligadas aos botões
def func_adicionar_livro():
    titulo = simpledialog.askstring("Título", "Digite o título do livro:")
    autor = simpledialog.askstring("Autor", "Digite o autor do livro:")
    ano = simpledialog.askinteger("Ano", "Digite o ano de publicação:")
    if titulo and autor and ano:
        adicionar_livro(titulo, autor, ano)

def func_listar_livros():
    listar_livros()

def func_cadastrar_usuario():
    nome = simpledialog.askstring("Nome", "Digite o nome do usuário:")
    contato = simpledialog.askstring("Contato", "Digite o contato:")
    if nome:
        cadastrar_usuario(nome, contato)

def func_alugar_livro():
    livro_id = simpledialog.askinteger("Alugar Livro", "ID do livro para alugar:")
    if livro_id:
        alugar_livro(livro_id)

def func_devolver_livro():
    livro_id = simpledialog.askinteger("Devolver Livro", "ID do livro para devolver:")
    if livro_id:
        devolver_livro(livro_id)

def func_relatorio():
    relatorio_geral()

# Janela principal
janela = tk.Tk()
janela.title("Sistema da Biblioteca")
janela.geometry("300x400")
janela.config(bg="white")

# Título
titulo = tk.Label(janela, text="📚 Biblioteca Virtual", font=("Arial", 16, "bold"), bg="white")
titulo.pack(pady=10)

# Botões
botoes = [
    ("Adicionar Livro", func_adicionar_livro),
    ("Listar Livros", func_listar_livros),
    ("Cadastrar Usuário", func_cadastrar_usuario),
    ("Alugar Livro", func_alugar_livro),
    ("Devolver Livro", func_devolver_livro),
    ("Relatório Geral", func_relatorio)
]

for texto, comando in botoes:
    tk.Button(janela, text=texto, command=comando, width=25, height=2, bg="lightblue").pack(pady=5)

# Inicia o loop da interface
janela.mainloop()


"""



"""
Garantir que as seguintes funções existam no sistema_biblioteca
from sistema_biblioteca import (
    criar_banco,
    adicionar_livro,
    listar_livros,
    cadastrar_usuario,
    alugar_livro,
    devolver_livro,
    relatorio_geral
)



"""


# rodar interface
"""
python interface.py


"""