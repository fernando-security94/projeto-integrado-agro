'''
Retorno de valores das funções (return)

Retornar o valor de uma função permite que você utilize esse valor em variáveis ou até mesmo
em operações aritiméticas. Caso não retorne nada, o valor da função sempre será None por natureza.
Ao usar a função return, o programa irá priorizar sempre o retorno dos valores escolhidos.

É permitido apenas 1 return por função:
Exemplo:

def soma(x, y):
    if x > 10:
        return 10
    return x + y

Nesse caso, se a condição if for verdadeira, o primeiro return será executado, a função será
dada por completa e será encerrada, não executando o segundo return de x + y.
'''

def soma(x, y):
    return x + y

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma1 + soma2)
