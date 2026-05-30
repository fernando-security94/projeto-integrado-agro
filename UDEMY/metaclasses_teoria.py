# Metaclasses são os tipos das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer

# class Foo:
#     ...


# Foo = type('Foo', (object,),{})
# f = Foo()  # class tipo type. Type é quem gera a class. Type é uma metaclass
# # print(isinstance(f, Foo))
# print(type(f))
# print(type(Foo))



from typing import Any


def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'

class Meta(type):
    falar = 123
    def __new__(msc, name, bases, dct):  # cria e retorna a class Pessoa
        print('NEW FROM META')
        cls = super().__new__(msc, name, bases, dct)
        cls.attr = 1234  # tudo o que criar aqui, estará disponível para as outras classes
        cls.__repr__ = meu_repr

        print(cls.__dict__)

        if 'falar' not in cls.__dict__ or \
            not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente método falar')
        
        return cls
    
    def __call__(self, *args, **kwargs):  # cria e retorna a instância
        instancia = super().__call__(*args, **kwargs)

        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie attr nome')
        return instancia
    

# __new__ de uma metaclass cria e retorna a class em si

class Pessoa(metaclass=Meta):  # Instancia de MCOeta
    def __new__(cls, *args, **kwargs):
        print('NEW FROM CLASS')
        instancia = super().__new__(cls)        
        return instancia


    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome

    def falar(self):
        return f'{self.nome} está falando...'
        

p1 = Pessoa('Fernando')
print(p1.nome)
print()
print(p1.__dict__)
print(p1.falar())
print(p1.attr)


'''
Nesse código vamos explicar como funciona a hierarquia com
metaclasses, que podem parecer com heranças, mas na verdade, não
são. 

- Criamos uma class Pessoa(metaclass = Meta) que recebe uma 
metaclass Meta que ainda não foi criada. Nesse caso, é 
necessário explicitar a origem da metaclass.

- Vamos criar o método new da class, que irá criar o init.

- def __new__(cls, *args, **kwargs)
- Vamos exibir uma mensagem para localizar o __new__ da class
- Vamos atribuir super().__new__(cls) a uma variável e return,
que é a criação da instancia da classe.

- Vamos inicializar a class com def __init__(self, nome)
- Vamos exbir uma mensagem para localizar o __init__
- Instanciar o argumento de __init__ self.nome = nome

- Vamos criar uma def falar() que executa uma ação
- return fstring dizendo que self.nome está falando.

- Agora precisamos criar a metaclass

- Criar class Meta(type), que por hierarquia, recebe type, que é o 
que cria a  e retorna a class.

- Criar o new da metaclass com def __new__(msc, name, bases, dict)
- Vamos exibir uma mensagem par localizar o new da metaclass.
- Vamos passar o __new__ para super() e atribuir a uma variável.
- cls = super().__new__(msc, name, base, dict)
- Vamos criar um novo atributo em cls, que estará disponível para as
outras classes.
- cls.attr = 1234
- Fora da classe, vamos criar uma função que será futuramente um 
__repr__

- Criar def meu_repr(self):
- Vai return f'{type(self).__name__}({self.__dict__})'
- Dentro da class, vamos atribuir cls__repr__ = meu_repr
- Vamos exibir cls.__dict__ 

- Criar uma condicional se o método falar nao for implementado,
ou nao for callable, levantar uma execeção 
NotImplementedError('Implemente o método falar')
- return a class cls

- Chamar o método def __call__(self, *args,**kwargs), que cria e retorna a instância.
Vamos passar os argumentos de __call_ para super() e atribuir a uma variável.
- instancia = super().__call(*args, **kwargs)

- Criar uma condicional se 'nome' não estiver na variável instancia.__dict__, levantar
a exceção NotImplementedError('Crie attr nome')
- return a variável instancia

- Vamos as execuções:
- Atribuir class Pessoa e seu valor a uma variável.
- Exibir p1.nome
- Exibir p1.__dict__ da metaclass
- Executar def falar()
- Exibir o atributo p1.attr




'''