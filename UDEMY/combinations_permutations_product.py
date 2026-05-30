'''
Combinations, Permutations, Product - itertools
Combinations -  Ordem não importa - iterável + tamanho do grupo
Permutations - Ordem importa
Product - Ordem importa e repete valores únicos
'''
from itertools import combinations, permutations, product
import pprint

# Exemplo de combination

def print_iter(iterator):
    print(*list(iterator), sep='\n')

people = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

shirts = [
    ['tank top', 'V neck'],
    ['black', 'white', 'red'],
    ['S', 'M', 'L'],
    ['men', 'women'],
    
]

print_iter(combinations(people, 2))
print()
print_iter(permutations(people, 2))  # Faz todas as combinações possíveis
print()
print_iter(product(*shirts))  # gera um aumento exponencial, na medida que aumenta os valores
print()

"""
Nessa seção, foi possível utilizar a mesma função para
os três diferentes tipos de módulos. Combinations, permutations and product.

Primeiro, from itertools import combinations, permutations, product.
Após as listas people and shirts terem sido definidas, foi necessário criar uma 
função iteradora que execute os três módulos.

Então, def print_iter recebe um iterator, e esse iterator
será convertido em lista, para ser exibido quando a função for 
executada.

Primeira execução foi com combinations entre os nomes da lista people, de dois em dois (não houve repetição) 
Segunda execução  foi com permutations entre os nomes da lista people, onde há repetição e mantém a ordem.
Terceira execução foi uma relação com products entre os valores da lista shirts, 
de forma que os tipos de camiseta, cores, tamanhos e para qual público foram iterados
em sua totalidade. 


"""