"""
Argumentos nomeados e não nomeados em Python
Argumento nomeado tem nome e com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor) ou argumento posicional


"""

def soma(x, y):
    print(f'{x=} {y=}', '|', 'x + y = ', x + y)

soma(1, 2)  # Exemplo de argumento não nomeado. Apenas o valor direto, na mesma ordem dos parâmetros (variável entre parenteses da função).
soma(2, 1)
soma(3, 4)
soma(4, 3)
soma(5, 6)
soma(x = 6, y = 5)  # Exemplo de argumento nomeado. Apos um argumento nomeado, todos os outros precisam ser nomeados tambem
soma(7, 8)
soma(8, 7)

print(soma)
print(type(soma))