"""
Crie funções que duplicam, triplicam e quadriplicam
o número recebido como parâmetro

"""

# Minha resolução

def duplica(numero):
    return numero * 2

def triplica(numero):
    return numero * 3

def quadriplica(numero):
    return numero * 4

print(duplica(10))
print(triplica(20))
print(quadriplica(30))

print()

# Resolução professor:

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(40))
print(triplicar(50))
print(quadruplicar(60))

'''
Dissertando resolução do professor:

Uma função para o multiplicador foi criada e recebeu um parâmetro multiplicador. Dentro dessa função, foi criada
uma outra função para multiplicar, que receberá um parâmetro número, e retornará numero * multiplicador.
A função do multiplicador retornará a função multiplicar sem executar.

A função do multiplicador será atribuida a uma variável duplicar, recebendo o valor 2, 
a variável triplicar, recebendo o valor 3 e a variável quadruplicar, recebendo valor 4.

Por fim, vamor exibir as três variáveis(numero a ser multiplicado) com closure, para finalizar a função multiplicar.


'''