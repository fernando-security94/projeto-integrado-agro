import numpy as np


# Criando sets em Python

meu_conjunto = set()

# add elementos no set
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)
meu_conjunto.add(40)
print(f'Meu conjunto: {meu_conjunto}\n')

elemento = 20

if elemento in meu_conjunto:
    print(f'Elemento {elemento} existe no set')
else:
    print(f'Elemento {elemento} não existe no set')

# remove elemento do set
meu_conjunto.remove(20)

# em set, os elementos são exibidos de forma aleatória
print(f'Ordem aleatória do set: {meu_conjunto}')

# exibindo set na ordem com sorted()
print(f'Ordem sorted do set: {sorted(meu_conjunto)}\n')

# dicionario vazio
dici_1 = {}
dici_1 = {'nome':"Fernando", 'idade' : 31}
print(f'Dicionario 1 após adicionar chave e valor: {dici_1}\n')

dici_2 = {'nome': "Maria", 'idade': 25}
print(f'Dicionário 2 após atribuicao direta: {dici_2}\n')

# criando dicionario com dict() e lista de tuplas
dici_3 = dict([('nome', 'Poliane'), ('idade', 44)])
print(f'Dicionário 3 com dict(): {dici_3}\n')

# criando dicionario com dict + buit-in zip() e duas listas
dici_4 = dict(zip(['nome', 'Elvis'], ['idade', 5]))
print(f'Dicionário 4 com zip(): {dici_4}\n')

# criando array numpy
my_array = np.array([1, 2, 3, 4, 5])
print(f'Array numpy: {my_array}\n', sep=', ')

# operações matemáticas com arrays
# eleva ao quadrado
squarred_array = my_array ** 2
print(f'Array elevada ao quadrado: {squarred_array}\n')

# soma os elementos da array
soma_array = np.sum(my_array)
print(f'Soma dos elementos: {soma_array}\n')

# acessando elementos pelo indice
indice_array = my_array[2]
print(f'Índice 2 da array: {indice_array}\n')