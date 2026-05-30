'''
map - mapear dados

func tools - partial
'''

from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

products = [
    {'name': 'Product 5', 'price' : 10.00},
    {'name': 'Product 1', 'price' : 22.32},
    {'name': 'Product 3', 'price' : 10.11},
    {'name': 'Product 2', 'price' : 105.87},
    {'name': 'Product 4', 'price' : 69.90},
]

def increase_price(value, percentage):
    return round(value * percentage)

# Usando módulo partial de forma automática

increase_ten_percent = partial(
    increase_price,
    percentage=1.1
)

# # Usando partial de forma manual
'''new_products = [
    {**p, 
     'price': increase_ten_percent(p['price'])} 
    for p in products
]
'''

# using map

def change_price(product):
    return {
        **product,
        'price': increase_ten_percent(
        product['price']
        )
    }

new_products = map(
    change_price, 
    products
)


# Using a function 
# new_products = [
#     {**p, 
#      'price': increase_price(p['price'], 1.1)} 
#     for p in products
# ]




print_iter(products)
print_iter(new_products)
print(hasattr(new_products, '__iter__'))
print(hasattr(new_products, '__next__'))
print(new_products)
print(isinstance(new_products, GeneratorType))
print(list(new_products))  # Esgotamento do iterator, retornará uma lista vazia

# Triplicando valores em lista usando map

one_list = [1, 2, 3, 4, 5]

print(
    list(map(   # função no primeiro parâmetro, iterável no segundo parâmetro
        lambda x: x*3, 
        one_list)
        )
    )   

# Ou

print(
    list(map(
        lambda x: x* 3, 
        [1, 2, 3, 4, 5]
            )
        )
    )


"""
Partial- Função que retorna uma closure
map - Faz o mapeamento dos dados através de uma função.

Para utilizar partial é preciso from functools import partial

Utilizamos a mesma função da aula anterior para exibir
os valores da lista de forma iterada e com quebra de linha.

Temos uma lista com diversos dicionários com chaves 'name' e 'price'

Criamos uma função def increase_price e receberá dois argumentos.
Retornará os valores arredondados de value * percentage com a 
função round.

Vamos atribuir a def increase_price a uma variável e com a função
partial com dois argumentos, sendo o primeiro, a def e o segundo,
o segundo argumento dessa def ja nomeado, percentage=1.1, 
aumentar em 10%.

Para de fato conseguirmos mudar o preço, é necessário acessar a chave.
Portanto, um função def change_price com um argumento foi criada.
Essa def retornará o argumento expandido (**product), seguido da chave
a ser acessada e receberá a variável increase_ten_percent executada
com product['price']

Uma nova variável foi criada e receberá a função map, e receberá dois
argumentos, o primeiro será a def change_price, e o segundo,
a lista products.

O efeito cascata é feito quando map executa def change_price,
que executa increase_ten_percent, que recebe de fato a def
increase_price. Então temos uma função que mapeia todos os dados
executando uma função que executa outras funções.

Por fim, vamos exibir a new_products que é a lista de produtos
com valores aumentados em 10% através da def print_iter(),
que ja converte os objetos em list, pois se fosse feito
através de print convencional, o valor exibido seria
<map object at ........> que o local onde esse valor
está alocado na memória do computador.

Também foi feito o aumento em 3x dos valores de uma lista
usando map de duas formas.
A primeira foi definindo uma variável que recebe a lista com 
seus valores, e ao exibir, map vai executar uma função
lambda com x: x*3 como primeiro argumento, e a variável que
esta recebendo a lista como segundo argumento.

A segunda forma pode ser feita diretamente com print, e map
irá receber como primeiro argumento a mesma função lambda,
mas o segundo argumento será uma lista com os valores a 
serem triplicados.

O resultado será o mesmo.


PS: Todo GENERATOR é um iterator.
Nem todo ITERATOR é um generator.

"""