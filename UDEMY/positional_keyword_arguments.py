'''
Controlando a quantidade de argumentos posicionais e nomeados em funções
*ags (ilimitado de argumentos posicionais)
**kwargs (ilimitado de argumentos nomeados)
- Positional-Only Parameters (\) - Tudo antes da barra deve
ser APENAS argumento posicional.
- PEP 570 - Python Positional-Only Parameters
- https://peps.python.org/pep/0570/
- Keyword-Only Arguments (*) - * sozinho NÃO SUGA VALORES.
- PEP 3102 - Keyword only arguments
- https//peps.python.org/pep-3102/
'''


# Função com argumentos posicionais ilimitados:

def soma(*args):
    print(sum(args))
soma(10, 20, 30)


# Função com argumentos posicionais limitados pela \ 

def soma_2(a, b, /, x, y):  # apesar que também é permitido posicional após a barra, porém nao é permitido nomeado antes da barra
    print( a + b + x + y)
soma_2(40, 50, x=60, y=70)

# Função com argumentos nomeados obrigatórios após *

def soma_3(a, b, *kawrgs, x, y):  # São permitidos argumentos nomeados antes do *
    print(a + b + x + y)
soma_3(a=80, b=90, x=100, y=110)

def soma_4(a, b, /, c, d):  # Exemplo de erro de argumentos nomeados antes da barra
    print(a + b + c + d)
soma_4(a=3, b=4, c=5, d=6 ) # positional_only arguments passed as keyword arguments 'a, b'