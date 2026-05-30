"""
@staticmethods (métodos estáticos) são inúteis em Python

Métodos estáticos são métodos que estão dentro das classes, mas
não tem acesso nem ao self e nem ao cls.

Em resumo, são funções protegidas pelo molde da classe, portanto, para ser executada
é necessário chamar a class primeiro

"""

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)


c1 = Classe.funcao_que_esta_na_classe(1, 2, 3)
Classe.funcao_que_esta_na_classe(nomeado=1)

