"""
Generator expressions , iterables and iterators
Diferença entre iterável e iterador
"""

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()  # tem __iter__ e __next__

print(next(iterator))
print(next(iterator))
print(next(iterator))

"""
Iterável = Item no qual é possível acessá-lo sequecialmente
Iterador = É o responsável por entregar o proximo valor sequencial. 
Essa é a sua única e exclusiva função. 
O iterador não sabe os valores passados e nem futuros, apenas utilizando a sua
função next, que é possível acessar e entregar esses valores sequencialmente.
Não é possível acessar o índice do iterator, tal como len.  

Quando não houver mais nada a ser iterado, o erro StopIteration será levantado.
"""
