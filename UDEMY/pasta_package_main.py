# from sys import path

# import pasta_package.modulo
# from pasta_package import modulo
# from pasta_package.modulo import *
# # from pasta_package.modulo import soma_modulo

# print(soma_modulo(1, 2))
# print(pasta_package.modulo.soma_modulo(10, 20))
# print(modulo.soma_modulo(100, 200))
# print(variavel, soma_modulo(300, 400), sep=', ')
# print()

# print(*path, sep='\n')

"""
Quando houver a necessidade de dividir o programa
em pastas, para que os módulos que estão protegidos
por essas pastas sejam importados para o __main__ 
podemos fazer das seguintes formas, sendo a última, uma
má pratica de programação.

Uma pasta pasta_package foi criada e nela contem um 
módulo.py, que nada mais é do que um arquivo python, 
e nesse módulo, temos uma função def soma_modulo(x, y).
Fora dessa pasta, na raiz, foi criado o pasta_package_main,
que na ordem de execução é o main file.

Dentro de pasta_package_main.py podemos fazer:
from pasta_package.modulo import soma_modulo, para executar:
print(soma_modulo(1, 2))

from pasta_package import modulo:
print(modulo.soma_modulo(10, 20))

import pasta_package.modulo
print(modulo.soma_modulo(100, 200))

Má pratica:
from pasta_package.modulo import *
Nesse caso, tudo o que houver no módulo, será importado
e para que seja feito da melhor forma, utilizamos 
__all__ = tudo o que quer importar em formato de lista
e alocado em uma variável.

"""

from pasta_package import fala_oi, soma_modulo

print(soma_modulo(10, 10))
fala_oi()