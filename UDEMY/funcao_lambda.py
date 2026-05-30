"""
Introdução à função lambda + list.sort sorted
A função lambda é uma função como qualquer outra em Python.
Porém, são funções anônimas que contém apenas uma linha. Ou seja, 
tudo deve ser contido dentro de uma única expressão.

lista = [
    {'nome': 'Fernando', 'sobronome': 'Ribeiro'}
    {'nome': 'Poliane', 'sobronome': 'Novaes'}
    {'nome': 'Felipe', 'sobronome': 'Ribeiro'}
    {'nome': 'Edna', 'sobronome': 'Giovanini'}
]


"""

lista1 = [12, 56, 801, 1, 0, -2, 76]
# lista.sort()  # Ordena em ordem crescente
# lista.sort(reverse=True)  # Ordena em ordem reversa

print(sorted(lista1))  # Ou aplicar diretamente no print, porém ao utilizar sorted()
print(sorted(lista1, reverse=True))  # uma cópia rasa da lista original é criada


# Utilizando sort com dicionarios

lista =[
    {'nome': 'Fernando', 'sobrenome': 'Ribeiro'},
    {'nome': 'Poliane', 'sobrenome': 'Novaes'},
    {'nome': 'Felipe', 'sobrenome': 'Ribeiro'},
    {'nome': 'Edna', 'sobrenome': 'Giovanini'},
]

# def ordena(item):
#     return item['nome']

# lista.sort(key=ordena)

# for item in lista:
#     print('PRINT', item)


# Utilizando função lambda

# lista.sort(key = lambda item: item['nome'])

# for item in lista:
#     print('PRINT', item)

# ou

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)


"""
Para utilizar a função lambda é necessário usar uma key = lambda e depois a passagem 
do parâmetro escolhido, como no caso da função acima
key=lambda o executor item:, pq lambda não utiliza return e receberá item com valor ['nome']

Porém, a função lambda não tem nome e nem usa parênteses

"""