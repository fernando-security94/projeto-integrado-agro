# criando sistema de biblioteca
# que lista e adiciona livros
# e cria dataviz

import matplotlib.pyplot as plt
from collections import Counter
import csv

# Classe que representa o livro e 
# seus atributos
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    
    def __str__(self):
        return f'Titulo: {self.titulo} por {self.autor}, publicado em {self.ano_publicacao}.'
    
# cria uma lista de vazia
# na qual os livros serão adicionados 
biblioteca = []

# lista vazia 
# para adicionar os anos dos livros
anos = []

# função que add os livros na biblioteca
# com a funcao append()
def adicionar_livro(titulo, autor, ano_publicacao):
    novo_livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    anos.append(ano_publicacao)
    print(f'O livro {titulo} foi adicionado à biblioteca.')

# função que lista todos os livros da biblioteca
# com laço for, iterando em todos os elementos
def listar_livros():
    print()
    for livro in biblioteca:
        print(livro)

# função que busca o livro na biblioteca
# por autor
def buscar_autor(autor):
    print("\nDigite o nome do autor: ")

    # por ser case sensitive, a funcao lower() irá retornar o autor, mesmo se
    # escrito com letra maiuscula.
    livro_autor = [livro for livro in biblioteca if livro.autor.lower() == autor.lower()]
    for livro in livro_autor:
        print(livro)
    if not livro_autor:
        print("Nenhum livro desse autor foi encontrado")
    print()


# funcao que busca o livro por ano
def buscar_ano(ano):
    print(f'Buscando livros publicados em {ano}')
    livro_ano = [livro for livro in biblioteca if livro.ano_publicacao == ano]
    for livro in livro_ano:
        print(livro)
    if not livro_ano:
        print("Nenhum livro encontrado!")

# função que remove livro da biblioteca
# podendo simular uma compra ou empréstimo
def remover_livro(titulo):
    for livro in biblioteca:
        if livro.titulo.lower() == titulo.lower():
            biblioteca.remove(livro)
            anos.remove(livro.ano_publicacao)
            print(f'O livro {titulo} foi removido!')
        else:
            print(f'Livro {titulo} não encontrado!')

# salvando em arquivo csv para poder analisar em tableau
# sql
def salvar_csv(nome_arquivo="biblioteca.csv"):
    with open(nome_arquivo, mode="w", newline='', encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Título", "Autor", "Ano de Publicação"])
        for livro in biblioteca:
            escritor.writerow([livro.titulo, livro.autor, livro.ano_publicacao])
        print(f'Dados salvos no arquivo "{nome_arquivo}".')



# execucao da função adiciona_livro
# passando seus respectivos atributos
adicionar_livro("Biblia Sagrada", "King James", 1400)
adicionar_livro("Até que nada mais importe", "Leandro Subirá", 2005)
adicionar_livro("Abusados", "Caco Bacellos", 1998)
adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)
adicionar_livro("Código Limpo", "Robert C. Martin", 2008)

# execução da função listar_livros
listar_livros()

# criar gráfico que exibe e conta livros
# por ano e remove anos duplicados
anos = list(set(anos))
anos.sort()

# contagem de livros por ano
contagem_por_ano = [anos.count(ano) for ano in anos]

# cria grafico de linhas com os
# dados anos e contagem_por_ano
plt.plot(anos, contagem_por_ano, color='royalblue', marker='o', linestyle='-')
plt.xlabel('Ano de Publicação')
plt.ylabel('Número de Livros')
plt.title('Distribuição de Livros por Ano de Publicação')

# Adiciona rótulos aos pontos de dados
for i, valor in enumerate(contagem_por_ano):
    plt.text(anos[i], valor, str(valor), ha='center', va='bottom')

# adiciona linha de grades no gráfico
plt.grid(True)

# exibe o gráfico
plt.show()


# testando funcao de buscar por autor
buscar_autor("Machado de Assis")
buscar_ano(2000)
# testando funcao de buscar por ano

# executando função que salva o arquivo em csv
salvar_csv()

# criando menu interativo da biblioteca que:
# adiciona, remove e lista os livros
# busca por autor e por ano, ou se nenhuma dessas opções
# escolhe sair.

while True:
    print("\nBem-vindo à Biblioteca Virtual!\n")
    print("Escolha uma das opções abaixo:\n")
    print("1 - Adicionar livro")
    print("2 - Remover livro")
    print("3 - Listar livros")
    print("4 - Buscar livro por autor")
    print("5 - Buscar livro por ano")
    print("6 - Sair\n")

    opcao = input("Qual opção você deseja: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        try:
            ano = int(input("Ano de publicação: "))
            adicionar_livro(titulo, autor, ano)
        except ValueError:
            print("Digite apenas números para o ano de publicação!")

    elif opcao == "2":
        titulo = input("Título do livro que deseja remover: ")
        remover_livro(titulo)

    elif opcao == "3":
        listar_livros()

    elif opcao == "4":
        autor = input("Buscar livro por autor: ")
        buscar_autor(autor)

    elif opcao == "5":
        try:
            ano = int(input("Buscar livro por ano: "))
            buscar_ano(ano)
        except ValueError:
            print("Digite um número válido para o ano!")

    elif opcao == "6":
        print("Encerrando o sistema. Obrigado!")
        break

    else:
        print("Opção inválida! Tente novamente.")

