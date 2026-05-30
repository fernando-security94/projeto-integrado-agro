'''
Ordem dos decoradores:
São feitas de baixo para cima, ou seja, o mais próximo da função
será executado primeiro, e assim sucessivamente.

'''

def parameters_decorator(name):
    def decorator(func):
        print('Decorator:', name)

        def your_new_function(*args, **kwargs):
            result = func(*args, **kwargs)
            final = f'{result} {name}'
            return final
        return your_new_function
    return decorator



@parameters_decorator(name='Third') 
@parameters_decorator(name='Second')
@parameters_decorator(name='First')
def sum(x, y):
    return x + y

ten_plus_five = sum(10, 5)
print(ten_plus_five)


"""



"""