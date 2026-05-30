"""
Dicionarios em Python

Dicionários são estruturas de dados do tipo par de "chave" e "valor".
Chaves podem ser consideradas como o "índice" que vimos nas listas
e podem ser de tipos imutáveis, como str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves {} ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list

Exemplo de dicionário:

"""
pessoa = {
    'nome': 'Fernando',
    'sobrenome': 'Ribeiro',
    'idade': 29,
    'altura': 1.82,
    'endereços': [       # lista que contém dicionários dentro do dicionário,  com chaves 'rua' e 'numero'
        {'rua': 'BLABLA', 'numero': 123},
        {'rua': 'outroblabla', 'numero': 123},
    ],
}

print(pessoa['nome'], type(pessoa))
print()


# Iteração sobre as chaves e valores. 
for chave in pessoa:
    print(chave, pessoa[chave], sep=': ')

