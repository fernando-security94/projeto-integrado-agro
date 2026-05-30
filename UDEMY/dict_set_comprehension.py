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