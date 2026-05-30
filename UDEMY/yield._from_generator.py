"""
Yiel from in generator functions
"""

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6

    
def gen3():
    yield from gen2()
    yield 30
    yield 40
    yield 50
    

gen = gen2()
gen_final = gen3()

# for numero in gen:
#     print(numero)

for numero in gen_final:
    print(numero)

"""
Dissertando yiel from
A funçao yield from é usada como continuação de yield
de funções anteriores, podendo facilitar na evolução do código.

Nesse caso, temos três funções, sendo gen1, gen2 e gen3.
Em cada uma delas temos 3 pausas yield, sendo que gen2
utiliza yield from da primeira função. Ou seja,
ao executar gen2, serão exibidos os valores de ambas
as funções.

Da mesma forma, gen3 possui um yield from gen2, e ao ser
executada, os valores das trÊs funções serão exibidas por estarem
ligadas por yield from gen1 e yield from gen2.

Para facilitar e iterar de forma dinâmica, sem a necessidade
de chamar a função next, as funções gen2 e gen3 foram
repassadas em variáveis gen e gen_final.

Porém, fiz a iteração com laço for apenas em gen_final,
pois tem ligação com gen2 e gen1, exibindo todos os valores
sem repetição.



"""