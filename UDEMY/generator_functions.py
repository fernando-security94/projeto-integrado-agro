"""
Introdução à Generator functions em Python
generator = (n for n in range(1000000))

"""

def generator(n=0):
    yield 1  # Pausa a função 
    print('Continuando a iteração...')
    yield 2  # A cada iteração, a função volta pro yield, a não ser que acabe
    print('Mais uma iteração...')
    yield 3
    print('Vai acabar...')
    return 'ACABOU' # Encerra a função


gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Fazendo a exibição acima dinamicamente com laço for

for n in gen:
    print(n)


print()

# Gerando contador range com generator functions

def gerador(n=0, maximum=10):
    while True:
        yield n  # Pausa e impede que o loop infinito do while fique rodando
        n += 1

        if n > maximum:
            return 'Chegou ao fim'
       
 
for i in gerador(n=10, maximum=100):
    print(i)

"""
Seguindo o racioncinio de generator expressions, essa idéia será aplicada
em funções com ou sem argumentos nomeados.
A função yield tem como objetivo pausar a function até que seja chamada 
novamente com next, ou iterada de forma dinâmica com laço for.

Aqui temos uma def generator que recebe argumento nomeado n = 0.
Yield 1 será a primeira pausa da função quando executada, exibirá
o número do yield em si. Após utilizar print(next), os objetos
seguites serão exibidos, tal como o número do próximo yield, que também
pode ser uma str. Para finalizar uma generator function utiliza-se
return e uma str, por exemplo: return 'Acabou'

Para iterar de forma dinâmica, alocaremos a def generator() na variável
gen, e por fim, chama-la dentro do laço for.

Gerando contador com generator functions
Função def gerador() com dois argumentos nomeados criada, n=0 e maxium=10.
Poderia ser apenas um argumento maximum=qualquer numero, que automaticamente
ja seria iniciada a partir de zero.
Criar um loop infinito de while true, porém com yield n, pausando a função.
E na sequência, para que a cada chamada de função, um numero seja adicionado,
n += 1

Condição if n > maximum, return 'Chegou ao fim', ou seja, assim que o
argumento n for maior que o argumento maximum ja definido, a função será
encerrada. 

E para iterar de forma dinâmica com laço for, é mais simples ainda.
Nesse caso, para não partir de zero, o argumento n foi nomeado com 10,
até o maximum=100.c

"""