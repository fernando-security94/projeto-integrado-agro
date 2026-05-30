"""
Dictionary comprehension e Set comprehension
"""

produto = {
    'nome': 'Caneta azul',
    'preço': 2.5,
    'categoria': 'Escritório'
}

dc = {
    chave: valor.upper()
    # isinstance checa o tipo de objeto, no caso, se valor for str, função upper será executada
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()
    
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),

]
# dc = {
#     chave: valor
#     for chave, valor in lista
# }

print(dc)
print(dict(lista))

# Set comprehension
s1 = {i for i in range(10)}
print(s1)


'''
Compreensão de dicionários é uma forma de iterar sobre
todos os valores utilizando o menor número de linhas possível

Nesse código, temos um dicionário que recebe uma chave
e um valor.upper() que só será executado se a condição
if isinstance for verdadeira, pois irá checar o tipo
de dado que a chave receberá. Caso seja false, else o mesmo
valor, sem ativar a função .upper()

Na sequência vejo o dict comprehension com laço for
sendo chave, valor in produto.items()

Na segunda parte, temos uma lista que recebe uma tupla, 
que foi organizada de forma parecida a um dicionário, 
contendo "chave" e "valor", só que em formato de str, 
separados por vírgula e não por dois pontos, como em dict.

Foram exibidos o dc verdadeiro, e através de type casting
a lista que recebe a tupla foi convertida em dicionário,
com dict(lista)

E por fim, um exemplo simples de set comprehension.
Sets também são colocados em chaves, porém, sem dois pontos.
Foi gerado um laço for para um range de 10. Então, 
irá retornar um set de 0 a 9.

'''