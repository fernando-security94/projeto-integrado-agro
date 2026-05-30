# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe callable

from typing import Any


class Callme:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwargs):  # faz a instancia da classe ser executável
        print(*args, 'está chamando...', self.phone)  
        return

call1 = Callme('123456789')
call1('Fernando Ribeiro')

'''
Nesse caso, call1 não é um objeto callable, ou seja, executável, porque é uma
instância da class CallMe relacionada a self.phone, não é um método ou uma função.

O método __call__ transforma essa instância em executável(callable).
Pode-se dizer que é um tipo de typecasting

Na criação do método __call__ foram adicionados *args e **kwargs,
permitindo mais de um argumento para a mesma instância, como vemos na execução:

- Atribuir a class Callme e seu valor a uma variável.
- Vamos atribuir mais um valor em call, que não irá substituir, no metodo __call_
a execução está como print(*args, 'está chamando'..., self.phone), ou seja, o que está sendo adicionado
se encaixa em *args ou **kwargs, porque self.phone ja está posicionado no final.



'''
