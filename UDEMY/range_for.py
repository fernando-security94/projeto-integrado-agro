"""
Range + for para usar intervalos de números
"""

'''
Nesse caso, para que eu consiga de fato exibir os números em um range (alcance) de 0 a 100
eu preciso iterar sobre cada número utilizando o laço for. Se eu chamar a função print direto
Também consigo através da função range, definir o número de casas a serem puladas.
Sendo a ordem: início / fim / de quanto em quanto. IMPORTANTE: O ÚLTIMO NÚMERO
NUNCA SERÁ EXIBIDO
'''

numeros = range(0, 100)
print(numeros)

numeros = range(0,101, 5)

# Variável número irá receber o valor de cada iteração.
for numero in numeros:
    print(numero)