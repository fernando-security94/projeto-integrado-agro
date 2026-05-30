"""
Reduce - Faz a redução de um iterável em um valor
"""

from functools import reduce


products = [
    {'name': 'Product 5', 'price' : 10.00},
    {'name': 'Product 1', 'price' : 22.32},
    {'name': 'Product 3', 'price' : 10.11},
    {'name': 'Product 2', 'price' : 105.87},
    {'name': 'Product 4', 'price' : 69.90},
]

# Função reduce functools

def reduce_function(increase, product):
    print('Increase', increase)
    print('Product', product)
    print()
    return increase + product['price']

total = reduce(
    reduce_function,
    products,
    0
)

print(f'Your total is: {total:.2f}' )
print()


# Using sum()
sum_total = sum(p['price'] for p in products)
print(f'Your total is: {sum_total:.2f}')

# total = 0  # função reduce de forma universal sem functools
# for p in products:
#     total+= p['price']

# print(round(total))


"""
A função reduce, como o próprio nome ja indica,
consegue reduzir todos os valores a um só, podendo fazer 
operações aritméticas em cada passagem, ou apenas
substituindo e salvando o próximo valor.

Temos uma lista que recebe inúmeros dicionários e suas chaves.
Criamos uma def reduce_function que receberá dois argumentos.
Um increase e product.
Vamos exibir 'Increase' e seu argumento, 'Product' e seu 
argumento, pular uma linha, e
return increase + product['price] que é a chave
que queremos reduzir.

Em uma nova variável, vamos chamar a função reduce, o primeiro 
argumento será a def reduce_function, o segundo argumento, a lista
de products, e por fim, o número 0, que por
convenção é usado para que não levante exceções, começando
igualmente do zero em ambos os argumentos.

Por fim, vamos exibir em fstrings para que seja possível
utilizar :.2f para 2 casas decimais.

Também é possível fazer exatamente a mesma coisa com a função
sum(), sendo necessário um map antes do laço for, para 
mapear a chave 'price':

sum_total = p['price] for p in products)

Por fim, exibir sum_total com fstrings e :.2f para 2 casas
decimais.




"""