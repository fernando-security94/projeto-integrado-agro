'''
Funções recursivas e recursividade
- Funções que podem se chamar de volta
- São úteis para dividir problemas grandes em partes menores

Toda função recursiva deve ter:
- Um problema que possa ser dividido em partes menores
- Um caso recursivo que resolve o pequeno problema
- Um caso base para que a recursão 
- fatorial - n! = 5 * 4 * 3 * *2 *1 = 120
- Fatorial em matemática é a multiplicação de um número representado por n! por seus 
- antecessores maiores ou iguais a 1.

- https://brasilescola.uol.com.br/matematica/fatorial.htm

'''

def recursive(start=0, end=10):
    
    print(f' Recursão {start}, final {end}') # Ao colocar no final, irá return end antes de exibir start=4 end=4

    # Caso base para encerrar o looping e evitar stack overflow

    if start >= end:
        return end
    
    
    # Caso recursivo que vai 
    # contar até o final
    
    start += 1
    return recursive(start, end)

print(recursive())

'''
Limite de recursão que por convenção do Python é de mil recursões,
pode ser aumentado (apesar de não recomendado)
através de import sys 
sys.setrecursionlimit(1004) - no caso de haver 1000 recursões para 1000 contadores.

Funções recursivas têm a mesma função que loops para iteração, então
é recomendado a preferência dos loops, pois 
em funções recursivas, todo o escopo da função é salvo na call stack, ou seja,
é possível causar stack overflow antes mesmo de executar a função por completo, levando
a quebra do programa. 
'''
print()

# Aplicando fatorial em Python:

def factorial(numero):
    # caso base para evitar zero e números negativos
    if numero <= 1:
        return 1
    
    # recursão fatorial

    return numero * factorial(numero -1 )

print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(9))
print(factorial(10))

"""
A recursão acima tem objetivo de mostrar a fatorial de diversos números, lembrando que o Python tem um 
limite de recursões para não comprometer o call stack.

Foi criada uma def factorial que recebe um argumento.
Se esse argumento for menor ou igual a 1, return o proprio 
argumento, com isso, não serão levados em
consideração números negativos ou zero.

Depois, mais um return do argumento * a def factorial(argumento - 1)
Ou seja, quando a função for executada, 
o argumento será um número inteiro, portanto, será 
o número * a função (numero - 1), se o número for 5,
por exemplo, será 5 * factorial(5 - 1).
Isso é uma recursão. Serão feitas recursões até o argumento,
ou seja, o número for menor ou igual a 1, e o valor de 
cada recursão será multiplicado pelo próximo argumento(número).


"""