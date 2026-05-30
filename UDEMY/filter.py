"""
Filter é um filtro funcional

"""

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

def price_order(product):  # Função que acessa chave 'price'  
    return product['price']

products = [
    {'name': 'Product 5', 'price' : 10.00},
    {'name': 'Product 1', 'price' : 22.32},
    {'name': 'Product 3', 'price' : 10.11},
    {'name': 'Product 2', 'price' : 105.87},
    {'name': 'Product 4', 'price' : 69.90},
]

new_products = [
    p for p in products
    if p['price'] > 10  # Map à esquerda do laço for, filtragem fica à direita do laço for 

]


'''
Usando a função filter: 

products_filter = filter(
    lambda p: p['price'] > 10,
    products
)
print()
print_iter(list(products_filter))
'''

new_order_products = sorted(products, key=price_order)  # Função que ordena preços em ordem crescente
products_above_ten_order = sorted(new_products, key=price_order)  # Produtos maiores que dez em ordem crescente

print()
print_iter(products)
print()
print_iter(new_products)
print()
print_iter(new_order_products)
print_iter(products_above_ten_order)


"""
A função filter tem como objetivo filtrar dados de acordo
com as condições que queremos exibir. Sendo que, a função map,
apesar de mapear os dados, também pode retornar tais valores.

Seguimos utilizando a def print_iter(iterator) de aulas anteriores,
para que quando executado, o código não retorne filter object, e sim,
os valores, de fato.

Definimos uma def price_order(product) que permite o acesso a chave
'price'.

Temos uma lista com dicionários e seus respectivos valores, nos quais
vamos filtrar e exibir apenas produtos acima de 10.00

Em uma nova variável, vamos fazer um list comprehension na lista
de products, se a chave 'price' for > 10. Veja que, a condição
de ser > 10 foi colocada após o laço for, ou seja, se caracteriza
filter, mas de uma forma que pode ser usada em outras linguagens,
sem recuros do Python.

Ao usar o recurso do Python, é necessário from functools import
reduce.

Ao atribuir uma nova variável, chamamos a função filter(função
lambda para acessar a chave 'price', products), e para exibir
utilizamos a def print_iter() e cast para list.

Chamamos novamente a função def print_iter para exibir os novos 
valores maiores que 10 (sem recurso python).



"""