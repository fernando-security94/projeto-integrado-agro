# dir, hasattr, getattr

string = 'Fernando'
metodo = 'append'

if hasattr(string, 'append'):
    print('Existe upper')
    print(getattr(string, metodo)())
    
else:
    print('Não existe o método', metodo)


"""
dir é uma função utilizada dentro do debugger que irá retornar
todos os atributos que estão definidos dentro do seu objeto,
no caso, a string.

No caso de hasattr, é uma checagem se determinado objeto possui
ou não um atributo/ método. Para essa checagem, 
independente do objeto ou método, é necessário sempre utilizar
strings.

Se o método a ser checado estiver em uma variável, é possível
checar dinamicamente atraves de getattr, alocando
ambas as variáveis em uma tupla e executando com parênteses.


"""