# Manipulação de string

texto = "Explorando a diversidade de linguagens de programação com Python"

print(f'\nTamanho do texto: {len(texto)}')
print(f'\npython in texto? {"python" in texto}')
print(f'\nQuantos "e" no texto? {texto.count("e")}')
print(f'\nAs 5 primeiras letras: {texto[:5]}')

print()
print()

# Manipulação de listas
cores = ['vermelho', 'azul', 'verde']

for cor in cores:
    print(f'Posição {cores.index(cor)}, cor: {cor}')

print()

# list comprehension
linguagens = ['Python', 'Java', 'JavaScript']
print(f'Antes de listcom: {linguagens}')

linguagens = [minusculo.lower() for minusculo in linguagens]
print(f'Depois de listcom lower: {linguagens}')

linguagens = [maiusculo.upper() for maiusculo in linguagens]
print(f'Depois de listcom upper: {linguagens}')

print()

# listcomp para converter valores com map e lambda
valor_dolares = [100, 150, 75, 50]
valor_cambio = 5.25
valor_reais = list(map(lambda x: x * valor_cambio, valor_dolares))
print(f'Valores em dolares: {valor_dolares}')
print(f'Valores em reais: {valor_reais}')

# list com filtrando valores com filter e lambda
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))

print(f'Numeros: {numeros}')
print(f'Numeros pares: {numeros_pares}')
print(f'Numeros impares: {numeros_impares}')

print()
# manipulação de tuplas
vogais = ("a", "e", "i", "o", "u")
tipo_vogais = type(vogais)
print(f'Tipo do objeto vogais: {tipo_vogais}')
for p, x in enumerate(vogais):
    print(f'Posição: {p}, vogal: {x}')
    