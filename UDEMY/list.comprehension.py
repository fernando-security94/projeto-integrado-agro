"""
List comprehension in Python
List comprehension é uma forma rápida e resumida de criar listas
a partir de iteráveis.

"""
# Gerando uma lista sem list comprehension

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

# Com list comprehension

lista = [numero  for numero in range(10)]  # laço for junto com variável (à esquerda do for) e iterável, no caso range(10)

lista2 = [numero * 3 for numero in range(11)]  # Cada número do laço in range(11) será multiplicado por 3

print(lista)
print(lista2)
