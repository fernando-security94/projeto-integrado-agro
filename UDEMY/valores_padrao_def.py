"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
Uma vez que um parâmetro receber um valor padrão, todos os outros também devem receber valores padrão.
"""

def soma(x, y, z=None):  # Valor padrão com None não vai gerar bug no código, caso seja necessário mudar o código sem receber argumento.
    if z is not None:
        print(f'{x=} {y=} {z=}', '----', 'x + y + z = ', x + y + z)
    else:
        print(f'{x=} { y=}', '-----', 'x + y = ', x + y)

soma(2, 1)
soma(300, 500)
soma(100, 900, 0)
soma(900, y = 700)
soma(z=50, x=10, y=20)  # Quando usar argumentos nomeados, os parâmetros podem ser posicionados fora de ordem.


