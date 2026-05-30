"""
Utilizando shallow copy e deep copy em Python

"""

import copy

d1 ={
    'c1': 1,
    'c2': 2,
    'l1': [0, 1 , 2]
}

# Com esse sinal de atribuição, mostra que d2 aponta para o mesmo dicionário que d1.
# Portanto, ao manipular d2, d1 também será alterado (no caso de dados mutáveis) pois apontam para o mesmo lugar da memória.
d2 = d1

d2['c1'] = 100
d2['l1'][1] = 99999

print(d1, d2)

# Utilizando a função copy(), uma shallow copy será criada e não afetará o valor do primeiro dicionário (em caso de dados imutáveis)
d3 ={
    'c3': 200,
    'c4': 400,
}
d4 = d3.copy()  # Shallow copy criada, permitindo alterar a cópia sem influenciar na original (somente para dados imutáveis).
d4['c3'] = 300

print(d3, d4)


"""
Exemplo de deepcopy
Antes de tudo é preciso import copy

A função deepcopy() explora cada chave, mesmo que haja uma lista dentro do dicionário, etc.
E tudo o que voce alterar na deepcopy, não infuenciará no valor da original, tanto para
dados mutáveis quanto para imutáveis. Os dicionários apontarão para lugares diferentes na memória
"""

dicionario1 ={
    'chave1': 100,
    'chave2': 200,
    'lista': [1, 2, 3],
}

dicionario2 = copy.deepcopy(dicionario1)

dicionario2['lista'][1] = 'Fábio'

print(dicionario1, dicionario2)