'''
groupby - Agrupando valores (itertools)
'''

from itertools import groupby

students = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordenate(student):
    return student['nota']

# group_students = sorted(students, key=lambda a: a['nota'])  # não é recomendado haver repetição de código
# groups = groupby(group_students, key=lambda a: a['nota'])   # portanto, uma função com a chave nota foi criada

group_students = sorted(students, key=ordenate)
groups = groupby(group_students, key=ordenate)


for key, group in groups:
    print(key)
    for student in group:
        print(student)



"""
O módulo groupby from itertools foi utilizado
nesse código, com o objetivo de separar os valores dos alunos
por nota, através da chave "nota".

Primeiro uma lista recebe vários dicionários. Esses dicionários
possuem as chaves "nome" e "nota.

Foram feitas duas formas diferentes 
de separar por nota e depois agrupar, só que a primeira não
é muito recomendada por haver repetição de código.

A primeira forma foi feita definindo uma nova variável
que recebe sorted(students, key=lambda a: a['nota']) = a lista
com dicionários de estudantes sorted, a função lambda e o iterator
a : a que irá acessar a chave 'nota' no dicionário.

Depois, em outra variável, receberá groupby, a variável que recebeu
sorted, e a mesma função lambda para acessar a chave 'nota', também.

A segunda forma foi feita através de uma def que acessa a chave 'nota'.
Então criamos a def ordenate que recebe um argumento, e irá retornar
o argumento acessando 'nota'

Vamos usar as mesmas variáveis criadas para sorted e groupby,
só que ao invés de usar key=lambda, vamos usar,
key=ordenate, que é o nome da def. A primeira variável irá 
sorted a lista de alunos, e a segunda variável irá groupby a
primeira variável.

Por fim, dentro de um laço for, uma variável e um iterator
key, group farão a iteração na variável que
fez o groupby e dentro desse laço e será exibida.
E a variável student irá iterar no 
iterator group, e também será exibida.

Resultado:
Grupos separados por nota (maior para o menor) com seus 
respectivos alunos, separados em dicionários, com chave
'nome' e 'nota'.




"""