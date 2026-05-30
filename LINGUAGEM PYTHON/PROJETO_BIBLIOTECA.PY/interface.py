# Criação da lógica da interface 
# exibição interativa para o usuario com tkinter

import tkinter as tk
from tkinter import messagebox
import sistema_biblioteca as sb
from sistema_biblioteca import adicionar_livro, listar_livros, alugar_livro, devolver_livro, cadastro_usuario, relatorio_geral
from tkinter import ttk



# Janela para adicionar livro no db
def adicionar_livro_interface():
    def salvar():
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        ano = entry_ano.get()
    
        try:
            estoque = int(entry_estoque.get())
        except ValueError:
            messagebox.showerror("Erro", "O estoque deve ser um número inteiro!")
            return
    
        sb.adicionar_livro(titulo, autor, ano, estoque)
        messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")
        janela.destroy()

    janela = tk.Toplevel()
    janela.title("Adicionar Livro")

    tk.Label(janela, text="Título:").pack()
    entry_titulo = tk.Entry(janela)
    entry_titulo.pack()

    tk.Label(janela, text="Autor").pack()
    entry_autor = tk.Entry(janela)
    entry_autor.pack()

    tk.Label(janela,text="Ano").pack()
    entry_ano = tk.Entry(janela)
    entry_ano.pack()

    tk.Label(janela, text="Estoque").pack()
    entry_estoque = tk.Entry(janela)
    entry_estoque.pack()

    tk.Button(janela, text="Adicionar Livro", command=salvar).pack(pady=5)

# Função de listar livros na interface do usuario
# Vamos utilizar treeview para ter uma visualização agradável
def listar_livros_interface():
    livros = sb.listar_livros()

    janela = tk.Toplevel()
    janela.title("Livros Listados")

    # Definição das colunas
    colunas = ('Título', 'Autor', 'Ano', 'Estoque')
    tree = ttk.Treeview(janela, columns=colunas, show='headings')
    tree.heading('Título', text='Título')
    tree.heading('Autor', text='Autor')
    tree.heading('Ano', text='Ano')
    tree.heading('Estoque', text='Estoque')

    # Criando cabeçalho
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    
    
    for livro in livros:
        tree.insert('', 'end', values=livro)
    
    tree.pack(padx=10, pady=10)

    



# Criação da função de aluguel livro na interface
def alugar_livro_interface():
    def confirmar():
        usuario_id = entry_usuario.get()
        nome_livro = entry_nome_livro.get()

        if not usuario_id or not nome_livro:
            messagebox.showerror("ERROR!", 'PREENCHA TODOS OS CAMPOS!')
            return
        
        try:
            sb.alugar_livro(usuario_id, nome_livro)
            messagebox.showinfo("SUCESSO!", "LIVRO ALUGADO COM SUCESSO!")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("UNKNOWN ERROR!", str(e))

    janela = tk.Toplevel()
    janela.title("Alugar Livro")

    tk.Label(janela, text="ID do Usuário").pack()
    entry_usuario = tk.Entry(janela)
    entry_usuario.pack()

    tk.Label(janela, text='Nome do Livro:').pack()
    entry_nome_livro = tk.Entry(janela)
    entry_nome_livro.pack()

    tk.Button(janela, text='Confirmar', command=confirmar).pack(pady=5)


# criação da função de devolução de livro na interface
def devolver_livro_interface():
    def confirmar():
        usuario_id = entry_usuario.get()
        nome_livro = entry_nome_livro.get()

        if not usuario_id or not nome_livro:
            messagebox.showerror("UNKNOWN ERROR!", 'PREENCHA TODOS OS CAMPOS!')
            return
        
        try:
            sb.devolver_livro(usuario_id, nome_livro)
            messagebox.showinfo("SUCESSO!", "LIVRO DEVOLVIDO!")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("UNKNOWN ERROR!", str(e))
    
    janela = tk.Toplevel()
    janela.title("Devolver Livro")

    tk.Label(janela, text="ID do usuário").pack()
    entry_usuario = tk.Entry(janela)
    entry_usuario.pack()

    tk.Label(janela, text="Título do Livro:").pack()
    entry_nome_livro = tk.Entry(janela)
    entry_nome_livro.pack()

    tk.Button(janela, text="Confirmar", command=confirmar).pack(pady=5)


# Criação da função que cadastra o usuario na interface
def cadastro_usuario_interface():
    def salvar():
        nome= entry_nome.get()
        email = entry_email.get()

        if not nome or not email:
            messagebox.showerror("ERROR!", "PREENCHA TODOS OS CAMPOS")
            return
        
        try:
            sb.cadastro_usuario(nome, email)
            messagebox.showinfo("SUCESSO!", "USUÁRIO CADASTRADO COM SUCESSO!")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("UNKNOW ERROR", str(e))

    janela = tk.Toplevel()
    janela.title("Cadastrar Usuário")

    tk.Label(janela, text="Nome do Usuário:").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text='Email:').pack()
    entry_email = tk.Entry(janela)
    entry_email.pack()

    tk.Button(janela, text='Cadastrar', command=salvar).pack(pady=5)

# Função do relatório geral na interface
def relatorio_geral_interface():
    dados = sb.relatorio_geral()

    janela = tk.Toplevel()
    janela.title("Relatório Geral")

    texto = tk.Text(janela, wrap='word', width=80, height=25)
    texto.pack(padx=10, pady=10)

    texto.insert('end', dados)
    texto.config(state='disabled')


# Função que irá iniciar a interface principal
def interface_principal():
    root = tk.Tk()
    root.title("Sistema de Biblioteca")

    tk.Label(root, text="Menu Biblioteca", font=("Times New Roman", 16)).pack(pady=10)

    # Adicionando botões correspondentes para cada opção do usuário
    tk.Button(root, text="Adicionar Livro", width=30, command=adicionar_livro_interface).pack(pady=5)
    tk.Button(root, text="Listar Livros", width=30, command=listar_livros_interface).pack(pady=5)
    tk.Button(root, text="Alugar Livro", width=30, command=alugar_livro_interface).pack(pady=5)
    tk.Button(root, text="Devolver Livro", width=30, command=devolver_livro_interface).pack(pady=5)
    tk.Button(root, text="Cadastrar Usuário", width=30, command=cadastro_usuario_interface).pack(pady=5)
    tk.Button(root, text="Relatório Geral", width=30, command=relatorio_geral_interface).pack(pady=5)
    tk.Button(root, text="Sair", width=30, command=root.destroy).pack(pady=20)

    root.mainloop()