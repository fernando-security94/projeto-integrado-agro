# Funções decoradoras e decoradores com classes

def add_repr(cls):
    def meu_repr(self):
        clas_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{clas_name}({class_dict})'
        return class_repr
    
    cls.__repr__ = meu_repr
    return cls


@add_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome




brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)


'''
Utilizamos funções decoradoras em classes 
para padronizar uma determinada ação e para deixar
o código mais limpo, com menos limpa e menos repetições.

Antes de criarmos a função decoradora, vamos às classes.

- Criar a classe Time e inicializar com def __init__(self, nome)
- Receberá o parâmetro nome e vamos instanciá-lo com self.nome = nome

- Criar a classe Planet, e também será inicializada da mesma
forma que Time, def __init__(self, nome)

- Vamos atribuir a class Time e seu valor a duas variáveis diferentes.

- Faremos o mesmo com a class Planeta

- Vamos exibir todas as variáveis atribuídas. O que será
exibido, são os endereços dos objetos em questão, na memória
do computador, que é o que acontece com uma class sem __repr__
Para "corrigir" esse comportamento e exibir
de fato os valores, vamos criar uma função decoradora.

- Fora do molde das classes, vamos criar def add_repr(cls). 
Nessa def, vamos implementar o modo __repr__ que retornará uma str,
mas, como se tratam de dois valores, que podem ser exibidos em dict,
vamos fazer dessa forma.

- A class def add_repr(cls) recebe a própria class. 

- Essa def será o decorator.

- Dentro de def add_repr(cls), vamos criar mais uma def meu__repr(self)

- A def meu_repr(self) não precisaria estar dentro def add_repr(cls), necessariamente.

- Poderia ser da seguinte forma, até visualmente mais limpo:

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})
    return class_repr

def add_repr(cls):
    cls__repr__ = meu_repr
    return cls
    

- A função def meu_repr() está recebendo self porque é como se estivesse 
dentro da class.

- Nessa def, vamos atribuir métodos que vão exibir o nome da class
na qual o objeto está sendo executado, vamos passar de str para dict e 
organizar em uma terceira variável, chamada de class_repr, que será
retornada

- Vamos chamar a classe e o método __repr__ e atribuir a 
def meu_repr da seguinte forma:
cls.__repr__ = meu_repr
return cls

- Então, o método __repr__ foi adicionado à class add_repr(cls).

- Agora, para se comportar como decorator, precisamos decorar as classes.

- Acima de cada class, vamos adicionar @add_repr

- Dessa forma, quando as variáveis atribuídas às classes
vão exibir seus valores reais em forma de dicionário
e em qual class eles estão.





'''