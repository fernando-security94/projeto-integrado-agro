from itertools import count

c1 = count(start=5, step=5)  # Contagem de 5 em 5 ao infinito ou até break. 
r1 = range(10, 101)  # Contagem de 10 à 100


print('c1', hasattr(c1, '__iter__'))  # checando se count é iterável - true
print('c1', hasattr(c1, '__next__'))  # checando se count é iterator - true
print('r1', hasattr(r1, '__iter__'))  # checando se range é iterável - true
print('r1', hasattr(r1, '__next__'))  # checando se range é iterator - false

for i in c1:
    if i > 100:
        break
    print(i)

print()

for j in r1:
    print(j)    


"""
Aqui veremos a diferença entre o módulo count e a função range.
Ambos podem gerar contadores, porém, count, por natureza,
sempre gera um contador infinito, até que através de uma 
iteração, seja interrompido.
Ja a função range, deve ter seu início e fim declarados, podendo 
também, ter intervalos, sucessivamente.

Em count, usa-se argumentos nomeados como start= e step=, 
que pode marcar o ínicio e os intervalos do contador.
O fim do contador em count deve ser declarado no laço for,
como no exemplo acima. Count não recebe end= como keyword argument.

O módulo count é tanto um iteravel quanto um iterator.
A função range é iterável, mas não é iterator.


"""