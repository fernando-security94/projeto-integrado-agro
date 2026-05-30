# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes 
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstrctmethod são métodos que não tem corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instanciadas
# diretamente.
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethod).
# Uma subclasse abstrata em Python tem sua metaclasse
# sendo ABCmeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.


from abc import ABC, ABCMeta, abstractmethod


# class Log(metaclass=ABCMeta):
    # ...

# ou


class Log(ABC):  # é o mesmo que class Log(metaclass=ABCmeta)
    @abstractmethod  # classe abstrata não deve ser instanciada
    def _log(self, msg):... # Método abstrato não tem corpo
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    

class LogPrintMixin(Log):
    def _log(self, msg):  # é obrigatório implementar o método abstrato log para utilizar a classe abstrata
        print(f'{msg}, from class: ({self.__class__.__name__})')

class LogFileMixin(Log):
    def _log(self, msg):
        print(f'{msg}, from class:({__class__.__name__})')



# Para usar uma classe abstrada deve ser através de herança, ja que não pode ser instanciada:
l = LogPrintMixin()
l2 = LogFileMixin()
l.log_success('You are logged in') 
l2.log_error('You are logged out')

