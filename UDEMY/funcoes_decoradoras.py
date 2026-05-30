'''
Funções decoradoras e decoradores
Decorar = Adicionar, remover, restringit, alterear
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python usar as funções 
decoradoras em outras funções.
Decoradores são "Syntax Sugar"

'''
def create_function(func):
    def internal(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print(f'O seu resultado é {result}')
        print('Ok, você foi decorada')
        return result
    return internal
     

@create_function  # Utilizado como decorador de função. Syntatic sugar
def reverse_string(string):
    print(f'A real função é def {reverse_string.__name__}()')  # Exibe nome da real função por trás de tudo
    return string[::-1]



def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parameter must be a string')
    
inverted = reverse_string('123')
print(inverted)
print()
hello_world = reverse_string('Hello World!')
print(hello_world)
print()
reverse_name = reverse_string('Fernando')
print(reverse_name)


# revert_string_checking_parameter = create_function(reverse_string)
# inverted = revert_string_checking_parameter('123')
# print(inverted)


"""
A ordem cronológica desse código começa em def reverse_string(string)
que é uma função que retorna os valores invertidos
de uma string.

Depois foi criada uma def is_string(param) que checa
se a instância do valor é uma str. Receberá um parâmetro.
Se a instância não for de str, raise TypeError irá ocorrer.


Depois, foi criada uma função decoradora chamada
def create_function, que tem a função de executar outras funções.
Essa função recebe uma def internal(*args, **kwargs) com
dois argumentos. Dentro dessa função, foi feito uma
iteração nos args, chamando a def is_string() recebendo
o iterador: 
for arg in args:
    is_string(arg)

O parâmetro func da def create_function() receberá 
*args, **kwargs e serão atribuídos a uma variável.
Essa variável result será retornada na def internal, e a 
return internal será para create_function.

Por fim, def create_function que executará rever_string será
atribuída a uma variável revert_string_checking_parameter,
e essa variável será atribuída à uma outra variável, chamada
inverted e então com valores adicionados e pronta
para ser exibida. 





"""