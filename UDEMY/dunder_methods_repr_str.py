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


from typing import Any


class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):  # mais simples para apenas exibir str
        return f'{self.x}, {self.y}'

    def __repr__(self):  # mais usado para desenvolvedores
        class_name = self.__class__.__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'  # garantindo a representação
    # correta com !r, pois no caso de z, que é uma str, sem o !r o resultado seria sem aspas.
        

p1 = Ponto(1, 2)  
p2 = Ponto(354, 400)

print(p1)  # exibe o __str__
print(repr(p1))  # exibe o __repr__
print()
print(p2)  # exibe __str__
print(f'{p2!r}')  # outra forma de exibir __repr__ (!r) ou !s para str