"""
Utilizaremos uma árvore para representar as faixas etárias 
e os filmes recomendados para cada faixa. 
Cada nó da árvore representará uma faixa etária e 
seus filhos representarão os filmes recomendados.
Criaremos uma classe Node para representar cada nó da árvore. 
Cada Node terá um atributo para armazenar a faixa etária 
ou o nome do filme e uma lista para armazenar os nós filhos.

"""

class Node:
    """
    Classe para representar cada nó na arvore.
    Cada nó pode ser uma faixa etaria ou um filme
    """
    def __init__(self, value):
        self.value = value   # Pode ser faixa etaria
        self.children = []   # Lista de nós filhos

    def add_child(self, child_node):
        # adiciona um nó filho
        self.children.append(child_node)

    def get_children(self):
        # retorna lista de filhos
        return self.children


# Funções de recomendação

def obter_idade_minima(faixa_etaria):
    """
    Extrai a idade minima de uma faixa etaria em formato de string.
    Ex: 'Livre' -> 0, '10+' -> 10, '+12' -> 12
    """
    if faixa_etaria.lower() == "livre":
        return 0
    else:
        # remove o + e converte para inteiro
        return int(faixa_etaria.replace("+", ""))
    
def recomendar_filmes(raiz, idade_usuario):
    """
    Retorna a lista de filmes que podem ser assistidos pelo usuario
    de acordo com a sua idade.
    """
    recomendacoes = []

    # Percorre cada faixa etária
    for faixa in raiz.get_children():
        idade_min = obter_idade_minima(faixa.value)
        if idade_usuario >= idade_min:
            # adiciona todos os filmes dessa faixa
            for filme in faixa.get_children():
                recomendacoes.append(filme.value)
    return recomendacoes
    
# Criando a arvore
root = Node("Faixas Etárias")  # Raiz da árvore

# Nós para cada faixa etária
livre = Node("Livre")
dez_anos = Node("10+")
doze_anos = Node("12+")
quatorze_anos = Node("14+")
dezesseis_anos = Node("16+")
dezoito_anos = Node("18+")

# Adicionando as faixas à raiz
root.add_child(livre)
root.add_child(dez_anos)
root.add_child(doze_anos)
root.add_child(quatorze_anos)
root.add_child(dezesseis_anos)
root.add_child(dezoito_anos)

# Adicionando filmes a cada faixa etaria
livre.add_child(Node("Toy Story"))
livre.add_child(Node("Procurando Nemo"))
livre.add_child(Node("Meu Malvado Favorito"))

dez_anos.add_child(Node("Harry Potter e a Pedra Filosofal"))
dez_anos.add_child(Node("Matilda"))
dez_anos.add_child(Node("Esqueceram de Mim"))

doze_anos.add_child(Node("Jogos Vorazes"))
doze_anos.add_child(Node("Percy Jackson"))
doze_anos.add_child(Node("A Culpa é das Estrelas"))

quatorze_anos.add_child(Node("Maze Runner"))
quatorze_anos.add_child(Node("Divergente"))

dezesseis_anos.add_child(Node("Vingadores"))
dezesseis_anos.add_child(Node("Homem de Ferro"))

dezoito_anos.add_child(Node("Clube da Luta"))
dezoito_anos.add_child(Node("Pulp Fiction"))

# Testes
idade_usuario = 20
print(f'Filmes recomendados para usuários de {idade_usuario} anos: ')
print(recomendar_filmes(root, idade_usuario))
print()

idade_usuario2 = 13
print(f'Filmes recomendados para usuarios de {idade_usuario2} anos: ')
print(recomendar_filmes(root, idade_usuario2))
print()

idade_usuario3 = 16
print(f'Filmes recomendados para usuarios de {idade_usuario3} anos: ')
print(recomendar_filmes(root, idade_usuario3))
print()

idade_usuario4 = 10
print(f'Filmes recomendados para usuarios de {idade_usuario4} anos: ')
print(recomendar_filmes(root, idade_usuario4))
print()

