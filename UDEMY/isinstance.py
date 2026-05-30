"""
isinstance() -  para saber se o objeto é de determinado tipo.
"""

lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, 
         {'nome': 'Fernando'}]


# Iterando sobre cada item, para saber qual isistance de set
# quando encontrar um set, irá add 5.

for item in lista:
    if isinstance(item, set):
        print('SET:')
        item.add(5)
        print(item, isinstance(item, set))  
        print()

    elif isinstance(item, str):
        print('STR:')
        print(item.upper(), isinstance(item, set))
        print()

    elif isinstance(item, (int, float)):
        print('NUM:')
        print(item * 10), isinstance(item, set)
        print()
    
    else:
        print('OTHER')
        print(item)


"""
isistance() é uma função em Python que checa qual tipo de dado
está presente em determinado local, seja uma lista, tupla, dicionário, etc.
É possível trabalhar com isinstance() para fazer condições, que se 
verdadeiras, tomem determinadas ações.

Aqui temos uma lista mista com diversos objetos de diferentes tipos.
Dentro de um laço for para iterar em cada item dessa lista, teremos diversas
condicionais if para checar o tipo de dado.

No primeiro if, estamos checando if isinstance de set dentro da lista.
Ao chamar a função, é preciso passar dois argumentos, o iterador (item)
e o tipo de dado que quer checar:
if isinstance(item, set)

No caso do set, ao ser uma condição verdadeira, vamos add(5) ao set.

A segunda condicional (elif) é para STR, caso verdadeira, vamos 
tornar upper()

A terceira condicional (elif) checa se tem int ou float, que podemos chamar de 
NUM, ou seja, números. Se for verdadeira, cada valor encontrado
será multiplicado por 10. Sempre que for passar mais de um tipo, deve ser em tupla.

Por fim (else), os dados restantes serão apenas exibidos, que nesse caso
será um dicionário, com sua respectiva chave e valor. 

Todas as condicionais estão dentro do laço for.

OBS: De forma inteligente, o VScode, consegue prever quais funções
podemos utilizar após determinar o tipo de dado a ser checado, de forma
específica para cada tipo de dado. Por isso a importância de todos
os if, para não gerar erros inexperados no código.



"""