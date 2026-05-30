"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)

"""

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

'''
Essa função com argumentos x, y apresentará um erro pela quantidade de parâmetros ser insuficiente
para a quantidade de argumentos (valores) posicionais. 
def soma(x, y):
    return x + y

soma(1, 2, 3, 4 , 5)
'''
# Dessa forma, não há a necessidade de limitae os argumentos, pois os parâmetros estão empacotados e podem ser
# quantos forem necessários.

def soma(*args):
    total = 0
    for numero in args:  # soma de todos os números da função
        print('Soma', total, '+',  numero,)
        total += numero
        print('Total = ', total)    
    return total

numeros_unitarios = 1, 2, 3, 4, 5, 6, 7
soma_total = soma(*numeros_unitarios)  # Utilizando desempacotamento de funções através de uma variável
numeros_centenarios = 100, 200, 300, 400, 500
soma_centenas = soma(*numeros_centenarios)

print()
print(f'O total da soma é {soma_total}')
print(f'O total da soma de centenas é {soma_centenas}')

print()
"""
Também é possível fazer essa soma diretamente através de uma função sum(), porém, ela só
consegue receber 2 argumentos por vez. Para mais de 2 argumentos, é possível utilizar listas ou tuplas
"""
print(f'O total utilizando sum() é ', sum({soma_total}))  # Função sum feita com variáveis de valores desempacotados.
print(f'O total utilizando sum() é', sum({soma_centenas}))
