# dir, hasattr, getattr

string = 'Fernando'
metodo = 'append'

if hasattr(string, 'append'):
    print('Existe append')
    print(getattr(string, metodo)())
    
else:
    print('Não existe o método', metodo)


lista = ['Fernando']
metodo_2 = 'append'

if hasattr(lista, metodo_2):
    print('Existe append em listas')
    print(getattr(lista, metodo_2))
else:
    print('O método não existe em listas.', metodo_2)


dicionario = {
    'nome': 'Fernando'
}
metodo_3 = 'append'

if hasattr(dicionario, metodo_3):
    print('Existe append em dicionários')
    print(getattr(dicionario, metodo_3)())
else:
    print('Não existe append em dicionários')

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