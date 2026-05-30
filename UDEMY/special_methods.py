# Python Special Methods, Magic Methods or Dunder Methods
# Dunder - double underscore = __dunder__
# Antigo e útil - https://rszalski.github.io/magicmethods
# https://docs.python.org/3/reference/datamodel/html#specialnames
# __lt__(self, other) - self < other
# __le__(self, other) - self <= other
# __gt__(self, other) - self > other
# __ge__(self, other) - self >= other
# __eq__(self, other) - self == other
# __ne__(self, other) - self != other
# __add__(self, other) - self + other
# __sub__(self, other) - self - other
# __mul__(self, other) - self * other
# __truediv__(self, other) - self / other
# __neg__(self) - - self
# __str__(self, other) - str
# __repr__(self) -str


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x= {self.x!r}, y= {self.y!r})'
    
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Point(novo_x, novo_y)
    
    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other



if __name__ == '__main__':
    p1 = Point(4,2)
    p2 = Point(6,4)
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que P2', p1 > p2)
    print('P2 é maior que P1', p2 > p1)


'''
Aqui veremos um exemplo sobre como usar special methods,
e suas assinaturas.

- Criar uma class Point

- Vamos iniciar a class com def __init__(self, x, y) e receberá
dois parâmetros.

- Instanciar os parâmetros x e y com self.x e self.y

- Criar um special methodo para exibir certos dados em 
uma string

- Esse special methodo será def __repr__(self) que recebe 
a própria class

- Vamos criar uma variável para atribuir type(self).__name__ , que
quando chamado, será o próprio nome da class Point.

- Vamos return uma fstring e será exibido a variável
class_name, e os valores de x e y que serão calculados no próximo
special method, com x = self.x e y = self.y

- Criar o método def __add__(self, other) que receberá dois parâmetros, que serão
atribuídos a x e y. Esse método realiza a soma entre dois objetos.

- Atribuir self.x + other.x em uma variável novo_x, e 
self.y + other.y à novo_y.

- return a class Point(variáveis criadas.)

- Vamos criar um método que checa se um valor é maior do que o
outro (greater than) e receberá dois parâmetros, self e other.

- Então o método def __gt__(self, other)

- Vamos atribuir o valor total da soma entre self.x e self.y à
variável resultado_self

- Vamos atribuir o valor total da soma entre other.x + other.y à
variável resultado.other

- Como estamos checando uma condição que deve retornar bool, 
return resultado_self > resultado_other

- Criar uma condicional if para em caso de o __name__ do arquivo
for main, executar as seguintes tarefas:

- Atribuir a class Point com seus dois parâmetros e uma variável.
Esses valores serão somados em def __add__ e checados em def __gt__

- Atribuir class Point e seus dois parâmetros em uma outra variável.
Esses valores serão somados em def __ad__ e checados em def __get__

- Criar uma terceira variável e atribuir a soma de p1 e p2, que serão
exibidos através do método __repr__

- Para exibir os valores da soma de p1 + p2, preciso print(p3)

- Para executar o método def __gt__, vamos print uma mensagem, p1 > p2

- Para executar o método def __gt__, vamos print uma mensagem, p1 < p2

- Ambas retornarão bool, sendo a primeira False, 
pois a soma de self.x + self.y = 6, e a segunda será True,
pois a soma de other.x + other.y = 10.







'''