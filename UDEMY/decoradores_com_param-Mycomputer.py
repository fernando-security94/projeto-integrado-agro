def function_factory(func):
    print('Decorator 1')

    def nested(*args, **kwargs):  # Nested ou inner functions são funções internas. 
        print('Inner function')
        result = func(*args, *kwargs)
        return result
    return nested

@function_factory
def sum(x, y):
    return x + y

multiply = function_factory(lambda x,y: x * y) # Forma de utilizar a fábrica de funções com lambda
minus = function_factory(lambda x,y: x - y)
divided = function_factory(lambda x, y : x / y)

ten_plus_five = sum(10,5)
ten_times_five = multiply(10, 5)
ten_minus_five = minus(10,5)
ten_divided_five = divided(10, 5)

print(ten_plus_five)
print(ten_times_five)
print(ten_minus_five)
print(ten_divided_five)
print(sum.__name__)
print(multiply.__name__)
print(minus.__name__)
print(divided.__name__)



"""
Seguindo a linha de raciocínio do código anterior,
como temos uma função decoradora que recebe
outra função que  executa outras funções.
Uma vez que executarmos as funções de sum(), minus() e 
multiply(), na verdade, estamos executando a função nested(), 
pois tudo o que estiver conectado com function_factory(), será 
executado por nested(), portanto, para provar isso, ao executar
as funções de aritmética mas sem exibir, uma mensagem "Decorator 1"
e "Inner function" serão exibidas. 



"""

#shift + alt + f para formatar