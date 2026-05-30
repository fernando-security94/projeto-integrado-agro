"""
Exercícios com funções
- Crie uma função que multiplique todos os argumentos não nomeados recebidos.
- Retorne o valor total para uma variável e mostre o valor da variável.

- Crie uma função que fala se o número é par ou impar.
- Retorne se o número é par ou impar. 


"""

def multiplica(*args):
    total = 1
    for numero in args:
        print('Multiplicação', total, '*', numero)
        total *= numero
    print('Total = ', total)
    return total

numeros_multiplicadores = (1, 2, 3, 4, 5, 6, 7)
resultado_total = multiplica(*numeros_multiplicadores)

print(f'O resultado total é {resultado_total}')

def par_impar(x):
    if x % 2 == 0:
        return f'O número {x} é par'
    return f'O número {x} é impar'

print(par_impar(13))
print(par_impar(2))
print(par_impar(29))
print(par_impar(38))
print(par_impar(700))
print(par_impar(7))


'''
Somente a forma de exibir o segundo exercício que eu 
precisei mudar para igual a do professor.

Dissertando os exercícios

Primeiro exerício: Defini uma função que recebe *args argumentos
não nomeados, o que me possibilita trabalhar com múltiplos valores.
Dentro dessa função, defini uma variável total que será 1, para
evitar que todos os números múltiplicados sejam igual 0.

Dentro de um laço for, iterei sobre os *args, para que o total possa
multiplicar cada numero enviado e ser agregado a cada laço.

Dentro de uma variável, atribui uma tupla com os números a serem multiplicados.
Em outra variável, atribuí os numeros a serem multiplicados à função,
e os desempacotei (distribuí pela variável) usando *numeros_multiplicadores

Por último, exibi o resultado total com fstrings.


Segundo exercício:
Defini uma uma função par_impar que recebe apenas um parâmetro, para checar
se o mesmo é impar ou par. O parâmetro pode ser qualquer nome, mas por convenção
utilizei "x".
Dentro da função, utilizei uma condição if, onde se o valor restante de 
uma divisão de x por 2 for igual a 0, significa que x é par,
portanto irá RETORNAR uma fstring com o argumento x em chaves dizendo
que é par. Caso essa condição não seja atingida, x será par.
Não houve a necessidade de utilizar o else, seria redundante. 

E por último, exibi e executei a função par_impar diversas vezes,
com diversos argumentos para testar o funcionamento do código,
e aparentemente, não apresentou nenhum bug. 





'''