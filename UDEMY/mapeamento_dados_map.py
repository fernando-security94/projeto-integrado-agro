
"""
Mapeamento de dados
"""



lista = []
for numero in range(10):
    lista.append(numero)

print(lista)

lista = [numero * 2 for numero in range(10)]
print(lista)

# Mapeamento em list comprehension
# Significa que posso pegar elementos de uma lista e colocar em outra diferente, alterando ou não seus valores

produtos = [
    {'nome': 'p1', 'preco' : 20, },
    {'nome': 'p2', 'preco' : 10, },
    {'nome': 'p3', 'preco' : 30, },

]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto} for produto in produtos]  # mapeamento sempre à esquerda do laço for

# print(novos_produtos)
print(*novos_produtos, sep='\n')

