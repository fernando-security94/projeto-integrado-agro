"""
List comprehension com mais de um for

"""

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

print(lista)

print()

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)

]

print(lista)

"""
Dissertando list comprehension com mais de um for
No primeiro exemplo, foi atribuído uma lista vazia à variável
lista. 
No primeiro laço for, com a variável x teremos uma iteração com 
range(3). Dentro do laço for x, teremos outro, o laço for y,
também in range(3).
Para que de fato os valores sejam adicionados à lista,
após o for y, usaremos lista.append(iterável)
Isso siginifica que para cada volta do laço for y, ou seja
de 0 à 2, o laço x terá também de 0 à 2. 0 para 0, 0 para 1 e 0 para 2.
E assim até o final do range.
Esse resultado será apresentado em uma tupla


Esse mesmo exemplo pode ser feito com list comprehension

Nesse caso, ao invés de receber uma lista vazia,
vamos utilizar list comprehension, utilizando mapeamento de dados
que serão adicionados a lista a cada laço, para isso,
a tupla com iteráveis (x, y) será posicionada
à esquerda do laço for. Para executar tanto x quanto y,
é necessário que sejam feitos dois laços for:
for x in range(3)
for y in range(3)
e por fim, print(lista)

"""
