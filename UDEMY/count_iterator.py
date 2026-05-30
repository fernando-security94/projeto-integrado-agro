from itertools import count

c1 = count(start=5, step=5)  # Contagem de 10 ao infinito ou até break. 
r1 = range(10, 101)  # Contagem de 10 à 100


print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

for i in c1:
    if i > 100:
        break
    print(i)

print()

for j in r1:
    print(j)    