"""
Filtragem de dados em list comprehension

"""
import pprint

def p(valor):
    pprint.pprint(valor, sort_dicts=False, width=40)

lista = []
for numero in range(10):
    lista.append(numero)

print(lista)



produtos = [
    {'nome': 'p1', 'preco' : 20, },
    {'nome': 'p2', 'preco' : 10, },
    {'nome': 'p3', 'preco' : 30, },

]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto} 
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10 # filtragem sempre à direita do laço for e não possui else após o if
    
]  

p(novos_produtos)

# print(novos_produtos)
# print(*novos_produtos, sep='\n')
# p(novos_produtos)

# lista = [numero for numero in range(10) if numero >= 4]  # Filtragem exibirá a partir de 4
# print(lista)