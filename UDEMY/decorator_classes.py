# Classes decoradoras (Decorator classes)

from typing import Any


class Multiplicar:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 10


    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        print(args, kwargs)
        return resultado * self._multiplicador



  # decorator da classe decoradora
def soma(x, y):
    return x + y


@Multiplicar
def multiplicacao(x, y):
    return x + y


dez_mais_dez = soma(10, 10)
dez_vezes_dez = multiplicacao(10, 10)
print(dez_mais_dez)
print(f'Resultado da soma é {dez_mais_dez}  e resultado do multiplicador é {dez_vezes_dez}')


'''
Da mesma forma que criamos funções decoradoras, também é 
possível criar classes decoradoras, que nesse caso, 
a def soma está sendo decorada pela class Multiplicar, que,
além de retornar a soma de x + y, e com isso, também retornará 
o return da class Multiplicar

- Criar class Multiplicar e inicializar com self e um argumento.
- Instanciar self.func = func

- Criar uma instancia protegia que será o multiplicador, que vai
ser atribuído no método call, por que quando tentarmos executar
a instancia da class, não será callable, portanto, self._multiplicador = 10

- Vamos criar o método __call__ para tornar a instancia da class
executável e para criar o método de multiplicação. O método
receberá self, *args, **kwargs

- Vamos sobrescrever o método e atribuir a uma variável, adicionando
a instancia self.func que está em __init__
- resultado = self.func(self, *args, **kwargs)
- Vamos exibir os args e kwargs
- return resultado * self._multiplicador
- Para que o multiplicador funcione, é necessário decorar a função soma
- @Multiplicar
def soma(x, y):
    return x + y

- Não existe diferença na forma de decorar com funções ou classes,
mas é importante lembrar que o decorator de classes, a primeira letra 
é maiúscula, literalmente o nome da class.

Vamos executar:
- Nesse caso não foi necessário atribuir a classe a uma variável, pq 
a class virou um decorator.
- Vamos atribuir a def soma e seus dois argumentos que serão somados, e depois
multiplicados a uma variável dez_mais_dez = soma(10, 10)
- print(dez_mais_10)

Resultado = (10, 10){}
200


'''