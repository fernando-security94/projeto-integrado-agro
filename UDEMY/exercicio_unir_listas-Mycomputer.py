"""
Crie uma função Ziper
O trabalho dessa função será unir duas listas na ordem.
Use todos os valores da menor lista

ex:
['Salvador', 'Ubatuba', 'Belo Horizonte]
['BA', 'SP', 'MG', 'RJ']

"""
'''
list_one = ['Bahia', 'Ubatuba', 'Belo Horizonte']
list_two = ['BA', 'SP', 'MG', 'RJ']
list_one.extend(list_two)

print(list_one)
'''

from itertools import zip_longest

# Solução professor:

def zipper(l1, l2):
    max_range = min(len(l1), len(l2))  # min and max são funções que exibem o menor ou maior intervalo
    return [
        (l1[i], l2[i]) for i in range(max_range)
    ]



list_one = ['Bahia', 'Ubatuba', 'Belo Horizonte']
list_two = ['BA', 'SP', 'MG', 'RJ']

print(zipper(list_one, list_two))

print()

# Ou podemos usar o as funções zip do Python

one_list = ['Bahia', 'Ubatuba', 'Belo Horizonte']
two_list = ['BA', 'SP', 'MG', 'RJ']
final_list = zip(one_list, two_list)
print(list(final_list))

print()
# Utilizando função zip_longest
longest_one = ['Bahia', 'Ubatuba', 'Belo Horizonte']
longest_two = ['BA', 'SP', 'MG', 'RJ'] 
print(list(zip_longest(longest_one, longest_two, fillvalue='Sem cidade')))


"""
Criando função zipper() que receberá dois argumentos, l1 e l2.
Será feito uma média entre l1 e l2 para encontrar a menor lista,
através da função min e len, que retorna o menor índice entre as duas,
e será atribuído a variável max_range.
O return será uma list comprehension de i for i in range(max_range),
mas, precisamos iterar as duas listas, então colocaremos em uma tupla
[
    (l1[i], l2[i] for i in range(max_range))
]

Isso é o mesmo que dizer que um índice de l1 está para um 
índice de l2.

Duas listas serão criadas e atribuídas à variáveis contendo
nome das cidades e seus estados.

por fim, exibir a função zipper(list_one, list_two) executada,
com as duas variáveis como argumentos. 

Podemos também, de forma mais simples, utilizar duas funções
do Python, sendo a primeira zip().
Duas listas contendo os valores de cidade e estado, respectivamente.
Podemos criar uma final_list que receberá ambas listas compactadas e 
proporcionais com zip(one_list, two_list) e para exibir, converter
essa variável em lista com type casting:
print(list(final_list))


E também, podemos criar a forma reversa com zip_longest, sendo
o primeiro passo from itertools import zip_longest,
 e utilizando a lista com maior índice.
Nesse caso, sobrára um valor, que será atribuído 
None automaticamente, ou podemos definir por padrão com 
a função fillvalue='Sem cidade'

Duas listas atribuídas à duas variáveis, e podemos exibir
e converter com typecasting diretamente, sem atribuir à
uma variável final:
print(list(zip_longest(longest_one, longest_two)))
"""