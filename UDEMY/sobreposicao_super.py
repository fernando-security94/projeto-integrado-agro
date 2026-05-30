'''
- super() é a super classe na sub classe
- Classe principal (Pessoa)
---> super class, base class, parent class
Classes filhas(Cliente)
----> sub class, child class, derived class

'''
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()  # retorna a super class temporariamente, quando sobreposta
#         print('DEPOIS DO UPPER')
#         return retorno


# string = MinhaString('Nando')
# print(string.upper())


class A:
    atributo_a = 'valor_a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        # print('A class A não exibe a sobreposição, porque é um object\n')
        
        print('Exibindo valor da class A: ')
        print('A')
        return

class B(A):
    atributo_b = 'valor_b'

    # sobrepondo o __init__ na class B
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('Sobreposição da class B: ')
        super().metodo()  # exibe 'tudo o que estiver na class A'
        
        print('Exibindo valor da class B: ')
        print('B')
        return


class C(B):
    atributo_c = 'valor_c'


    def __init__(self, *args, **kwargs):        # super().__init__(*args, **kwargs)
        print('EI, burlei o sistema')
        super().__init__(*args, **kwargs)

    def metodo(self):
        print('Sobreposição da class C: ')
        super().metodo()
        super(B, self).metodo()
        A.metodo(self)  # é a mesma coisa que super(A, self).metodo()

        print('Exibindo valor da class C: ')
        print('C')
        # super(A, self).metodo() - AttributeError - super object has no attribute
        return
        
        


c = C('Atributo do C', 'Segundo atributo do C')
a = A('Atributo do A')
b = B('Atributo do B', 'Segundo atributo do B')
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
print()
print(a.atributo)
print(b.atributo)
print(c.atributo)
print()
a.metodo()
print()
b.metodo()
print()
c.metodo()

print(C.__mro__)
# print(C.mro())
# print(B.mro())
# print(A.mro())
print()
print(b.outra_coisa)
print(c.outra_coisa)

'''
Neste código, vamos dissertar sobre a sobreposição simples, que é um tipo de herança, porém,
ao fazer a sobreposição, vamos exibir o valor da class que está como instância self.

- Criar uma class A. Atribuir 'valor_a' a uma variável.
- Inicializar com def __init__(self, atributo) e instanciar
com self.atributo = atributo. Método __init__ será sobreposto depois.
- Criar uma def metodo(self) que exibe 'A' e será sobreposto também.

- Criar uma class B(A) que recebe de herança a class A. Atribuir 'valor_b'
a uma variável.
- Agora, ocorre uma sobreposição do __init__(self, atributo) da class A, 
na class B com mais um atributo, da seguinte forma:
def __init__(self, atributo, outra_coisa)
self.outra_coisa = outra_coisa.
- Utilizar a função super() para devolver a função do __init__ através de
super().__init(self, atributo) 
- Instanciar self.outra_coisa = outra_coisa
- Criar a mesma def_metodo(self) que exibe 'B', chamar a função super() e será sobreposta pelo valor de A

- Criar a class C(B) que recebe de herança a class B. Atribuir 'valor_c'
a uma variável.
- Fazer novamente a sobreposição do __init__, só que dessa vez, vamos
passar *args e **kwargs através de,
def __init(self, *args, **kwargs)
- Criar def metodo(self), chamar função super() para C e para B(), assim, 
os valores sobrepostos em C e B serão exibidos, ou seja, 'B' e 'A'
- Exibir 'C' referente a propria class.
- Return para encerrar

- Vamos atribuir as três classes em variáveis e passar seus valores
- Na class A, temos apenas um atributo, ou seja, aceitará apenas
um argumento.
- Ja na class B, quando feita a sobreposição do __init__, foi passado mais um atributo (qualquer_coisa),
permitindo assim, mais um argumento posicional.
- O mesmo ocorre na class C.

- Exibir as variáveis atributo_a, atributo_b e atributo_c
- Exibir a instância atributo através de variavel.atributo
- Exibir a def método através de c.metodo() que vai retornar os valores
sobrepostos das classes herdadas. Na class C, por exemplo, fizemos super().metodo() e 
super(B, self).metodo().
- Quando não passamos nenhum parâmetro na função super, fica implicito que nos 
referimos à própria class em questão, entao nesse caso, seria o mesmo que:
super(C, self).metodo()
super(B, self).metodo() - explicito que estamos buscando na class B, mesmo sendo chamada na class C

- É possível exibir a ordem de resolução dos métodos com a função
mro(method resolution order):
print(A.mro())
print(B.mro())
print(C.mro())

- Por fim, exibimos o segundo atributo 'outra_coisa com:
print(b.outra_coisa) e 
printo(c.outra_coisa)




'''