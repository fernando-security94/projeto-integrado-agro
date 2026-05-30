# criando sistema de biblioteca
# que lista e adiciona livros
# e cria dataviz

# importando as bibliotecas necessarias para a atividade
import matplotlib.pyplot as plt
from collections import Counter


# Classe que representa o livro e 
# seus atributos
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade
    
    def __str__(self):
        return f'Titulo: {self.titulo} por {self.autor}. Gênero: {self.genero}. Quantidade: {self.quantidade} .'
    
# cria uma lista de vazia
# na qual os livros serão adicionados 
biblioteca = []

# lista vazia 
# para adicionar os anos dos livros
genero_livro = []

# lista vazia pafa adicionar a quantidade
quantidade_livros = []

# função que add os livros na biblioteca
# com a funcao append()
def adicionar_livro(titulo, autor, genero, quantidade):
    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    genero_livro.append(genero)
    quantidade_livros.append(quantidade)
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
def buscar_genero(genero):
    print(f'Buscando livros por gênero: {genero}')
    livro_genero = [livro for livro in biblioteca if livro.genero.lower() == genero.lower()]
    for livro in livro_genero:
        print(livro)
    if not livro_genero:
        print("Nenhum livro encontrado!")

# função que remove livro da biblioteca
# podendo simular uma compra ou empréstimo
def remover_livro(titulo):
    for livro in biblioteca:
        if livro.titulo.lower() == titulo.lower():
            biblioteca.remove(livro)
            genero_livro.remove(livro.genero)
            print(f'O livro {titulo} foi removido!')
            break
        else:
            print(f'Livro {titulo} não encontrado!')



# execucao da função adiciona_livro
# passando seus respectivos atributos
adicionar_livro("Biblia Sagrada", "King James","Religioso", 10)
adicionar_livro("Até que nada mais importe", "Leandro Subirá","Religioso", 5)
adicionar_livro("Abusados", "Caco Bacellos","Drama", 3)
adicionar_livro("Dom Casmurro", "Machado de Assis", "Romance", 5)
adicionar_livro("Código Limpo", "Robert C. Martin", "Tecnologia", 4)

# execução da função listar_livros
listar_livros()

# criar gráfico que exibe e conta livros
# por gênero e remove generos duplicados
genero_livro = list(set(genero_livro))
genero_livro.sort()

# contagem de livros por genero diretamente da lista biblioteca
contagem_por_genero = Counter([livro.genero for livro in biblioteca])

# separa os dados do gráfico
generos = list(contagem_por_genero.keys())
quantidades = list(contagem_por_genero.values()) 



# cria grafico de barras com os
# dados gênero e quantidade
plt.bar(generos, quantidades, color='royalblue')
plt.xlabel('Gênero do livro')
plt.ylabel('Número de Livros')
plt.title('Distribuição de Livros por Gênero')

# Adiciona rótulos aos pontos de dados
for i, valor in enumerate(quantidades):
    plt.text(i, valor, str(valor), ha='center', va='bottom')


# exibe o gráfico
plt.show()


# testando funcao de buscar por autor
buscar_autor("Machado de Assis")
buscar_genero("Religioso")
# testando funcao de buscar por ano



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
    print("5 - Buscar livro por gênero")
    print("6 - Sair\n")

    opcao = input("Qual opção você deseja: ")

    if opcao == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Gênero: ")
        try:
            quantidade = int(input("Quantidade de livros: "))
            adicionar_livro(titulo, autor, genero, quantidade)
        except ValueError:
            print("Digite apenas números para a quantidade!")

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
            genero = input("Buscar livro por gênero: ")
            buscar_genero(genero)
        except ValueError:
            print("Digite um número válido para o ano!")

    elif opcao == "6":
        print("Encerrando o sistema. Obrigado!")
        break

    else:
        print("Opção inválida! Tente novamente.")



'''
Melhorias futuras
Jogar a criacao do grafico em uma função
para facilitar a reutilização


def exibir_grafico_genero():
    contagem_por_genero = Counter([livro.genero for livro in biblioteca])
    generos = list(contagem_por_genero.keys())
    quantidades = list(contagem_por_genero.values()) 

    plt.bar(generos, quantidades, color='royalblue')
    plt.xlabel('Gênero do livro')
    plt.ylabel('Número de Livros')
    plt.title('Distribuição de Livros por Gênero')
    for i, valor in enumerate(quantidades):
        plt.text(i, valor, str(valor), ha='center', va='bottom')
    plt.show()


    

'''