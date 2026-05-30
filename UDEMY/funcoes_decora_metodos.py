# Funções decoradoras e decoradores com métodos


def add_repr(cls):
    def meu_repr(self):
        clas_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{clas_name}({class_dict})'
        return class_repr
    
    cls.__repr__ = meu_repr
    return cls

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return f'{resultado}. Você está em casa'
        return resultado
    return interno


@add_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

    def falar_nome(self):
         return f'O nome do time é {self.nome}'


@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O nome do planeta é {self.nome}'

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)
print()
print(brasil.falar_nome())
print(portugal.falar_nome())
print()
print(terra)
print(marte)
print()
print(terra.falar_nome())
print(marte.falar_nome())


'''
Nesse codigo, vamos ver um exemplo de decoração de métodos.
Por exemplo, vamos decorar o método def falar_nome com 
a função decoradora def meu_planeta, que ao executar falar_nome(), por 
estar decorada, irá exibir o que estiver no decorator.

- Vamos criar a def meu_planeta(metodo) que recebe um argumento.
- Dentro dessa função, criaremos uma função interna def interno(self, *args, *kwarg)
- Na def interno() é onde o a def decoradora será desenvolvida.
- Precisamos de alguma forma utilzar o argumento de meu_planeta, então,
vamos substituir o método inteiro e atribui-lo a uma variável 'resultado':
- resultado = metodo(self, *args, **kwargs)
- Vamos criar uma condicional if, sendo se houver 'Terra' em resultado,
return uma fstring, se nao, não é necessário usar else, apenas 
return resultado, e para fechar o ciclo da def, é necessário retornar a def interno().
- Agora, para decorar o método falar_nome é a parte mais fácil.
- @meu_planeta
  def falar_nome(self)

- Por ter sido decorada, a def falar_nome vai retornar o que está
sendo retornado em def meu_planeta, que é o que o 'resultado' em def interno(),
sendo um tipo de closure.

- Ao print(terra.falar_nome) a fstring f'{resultado}. Você está em casa'.
o resultado será:
'O nome do planeta é Terra. Você está em casa'







'''