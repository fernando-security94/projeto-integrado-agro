"""
Exercício Somando duas listas
"""
from itertools import zip_longest

list_one = [1, 2, 3, 4, 5, 6, 7]
list_two = [1, 2, 3, 4]
list_sum = []


# Resolução sem recursos do Python, serve para maioria
# da linguagens de programação

"""
for i in range(len(list_two)):
    list_sum.append(list_one[i] + list_two[i])
print(list_sum)
"""

# Resolução com recursos Python, mas não a melhor
'''
for i, _ in enumerate(list_two):
    list_sum.append(list_one[i] + list_two[i])
print(list_sum)
'''


# Resolução com recursos Python e mais simples, com list comprehension
# list_sum = [x + y for x, y in zip(list_one, list_two)]  - O restante dos valores ficam de fora

list_sum = [x + y for x, y in zip_longest(list_one, list_two, fillvalue=0)]  # Com zip_longest nenhum valor fica de fora
print(list_sum)


"""
Esse exercício de soma de valores de listas é parecido 
com o de uni-las. Foram feitas quatro formas, sendo a primeira
mais universal para outras linguagens.

Após as listas com valores serem criadas, criaremos uma lista
vazia (list_sum) que receberá os valores somados, e será usada em todas
as resoluções.

A primeira solução será através de um laço for em um range
com len da menor lista (list_two).
E então na lista vazia (list_sum) utilizaremos a função append
com as duas listas iteradas = list_one[i] + list[i], e
por fim, print(list_sum).

A segunda forma, com recursos Python, mas não tão simples,
vamos usar o mesmo laço for, mas ao invés de range, será com
enumerate na menor lista com um _ antes do iterável
para exibir somente os valores e não os índices, 
e não usaremos len()

A terceira forma, com recursos Python e mais simples, será
com função zip() e list comprehension, sendo 
x + y for x, y in zip(list_one, list_two).

A quarta e última forma, na minha opinião a mais completa,
pois nenhum valor ficará de fora, evitando possíveis erros,
será feita com zip_longest e list comprehension.
Lembrando que é necessario from itertools import zip_longest,
e fillvalue=0 ao final para que não levante uma exceção entre
None and int.




"""
