"""
Generator expressions

"""
import sys  # função getsizeof

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()  # tem __iter__ e __next__

# Generator expression são funções que sabem pausar em determinada ocasião
# Todo generator é um iterator, mas iterator não é generator.
lista = [n for n in range(10000)]  
generator = (n for n in range(10000))  # Generator utiliza-se parênteses 

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))


"""
Nesse caso, tanto lista quanto generator vão ter valores iterados em um range de 10000. Porém, a lista será
salva inteira na memória, consumindo mais espaço, e quando executada, todos os valores serão exibidos,
exceto seja executada com índices específicos.
Ja o generator, não salva tudo de uma vez, e fica pausado esperando entregar o próximo valor
somente a cada nova chamada, consumindo menos memória.
 
O ponto positivo de iterar com grandes valores utilizando listas, é que é possível acessar seus índices,
chamar função len(), podendo achar valores específicos, sem perder tempo e recursos.

Porém, se a lista for alterada com mais valores, os mesmos serão agregados de uma só vez na memória, 
aumentando seu consumo, com generator não, pois, é uma função que fica pausada por natureza e não sabe
quantos ou qual o próximo valor a ser entregue, até ser executada.


"""