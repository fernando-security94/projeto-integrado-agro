'''
- Encapsulamento - Modificadores de acesso (public, protected, private)
- Python NÃO tem modificadores de acesso
- Python possuim convenções do que deve ou não ser feito
Exemplos:
- Sem underline - public, pode ser usado em qualquer lugar
- Com 1 underline _ - protected - NÃO deve ser usado FORA da classe ou
de suas subclasses.
- Com 2 underline __ - private - "name mangling" (desconfiguração de nomes) em Python
- Só deve ser usado na classe que foi declarado.

- 4 pilares da Programação Orientada a Objeto:
- Abstração, Herança, Encapsulamento, Polimorfismo

'''
# Encapsulamento

from functools import partial

class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'

    def metodo_publico(self):
        self._metodo_protected()
        print(self._protected)
        print(self.__private)
        return 'método_publico'

    def _metodo_protected(self):  # criado para uso interno da classe
        return '_método_protected'    
    
    def __metodo_private(self):
        return 'Isso é private'
    


f = Foo()
#print(f.public)
print(f.metodo_publico())
print()

print(f._metodo_protected())  # Isso não deve ser feito por convenção

# print(f.__metodo_private())   # Levantará AttributeError
# print(f._Foo__metodo_private())  # name mangling para que possa ser acessado


'''
Nesse código, vamos mostrar o encapsulamento, que é um dos pilares
da programação orientada a objeto, e também, exemplos de método público,
protected e private.

Primeiro, criamos a class Foo e a instância __init(self)

Dentro do escopo da class, vamos criar um método por vez e encapsular na Class Foo
Então, criamos def metodo_publico(self) e irá retornar 'método publico'

Dentro da instância __init__ vamos utilizar self.public = 'Isso é publico', quando
a class for atribuída a uma variável, e essa variável executar 
a def metodo_publico().

Agora, criamos def _metodo_protected(self), e só deve ser acessado dentro da classe e 
suas subclasses. Irá return '_metodo_protected', e vamos utiliza-lo 
na instância de classe self._protected = 'isso é protegido', e vamos colocá-lo
em def metodo_public como self._metodo_protected e print, apenas
para ser exibido quando o método publico for executado.

Lembrando, que quando um atributo está da seguinte forma, self._atributo,
signfica que não deve ser usado por convenção, uma vez que Python
não possui modificadores de acesso.

Por fim, criamos um def __metodo_private(self), que retorna 'isso é private'
Vamos atribui-lo na instância __init__ com self.__private = 'isso é privado'
e executar em def metodo_publico, apenas para fim de mostrar, que,
somente em caso de __metodo, o  Python levantará uma exceçao de 
AttributError.

Para que todos os metodos sejam exibidos, uma vez que estão encapsulados em metodo_publico,
vamos atribuir a class à uma variável f = Foo()
e exibir print(f.metodo_publico())







'''