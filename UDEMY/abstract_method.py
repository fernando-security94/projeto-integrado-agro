# abstract method para qualquer método já decorado
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação


from abc import ABC, ABCMeta, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

   
    @property
#    @abstractmethod
    def name(self):  # irá retornar None por não ter nada no getter
        return self._name
  
    @name.setter
    @abstractmethod
    def name(self, name):...
        
        
class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
    
    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name

foo = Foo('Bar')
print(foo.name)



