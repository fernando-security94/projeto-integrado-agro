"""
Exemplos mais complexos de função lambda sendo 
executadas através de outras funções.

"""

def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

 # sem lambda
duplica = cria_multiplicador(2) 

# com lambda
duplica = executa(
    lambda m: lambda n: n * m,
    2  # Duplicador
)
print(duplica(10))  # Número a ser multiplicado


print(
    executa(
        lambda x, y: x + y,  # Função lambda não utilizam return, para retornar, é só escrever na mesma linha,
        10, 5  # e depois passar os valores.

    ),
    executa(soma, 10, 5),
    soma(10, 5), sep='| '
)


print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    )

)