'''
Enumerate - Enumera iteráveis (índices)

'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Felipe')
lista.append('Fábio')
lista.append(True)

# Se eu atribuir o iterator (enumerate) a uma variável, uma vez que os dados forem consumidos, 
# não será mais possível fazer iteração com laço for sobre a lista.

#lista_enumerada = enumerate(lista)

# Se eu exibir a lista interada com o enumerate, o programa exibirá o iterador e seu local na memória, e não os valores
#print(lista_enumerada)

# Caso não queira utilizar o laço for, é possível fazer type conversion ao atribuir a uma variável.
#lista_enumerada = list(enumerate(lista))




# Então, eu posso iterar com o for diretamente com enumerate(lista), assim, é possível iterar quantas vezes quiser
for item in enumerate(lista):
#    print(item)
    # desempacotamento com indice e valor
    indice, nome = item
    print(indice, nome)

# É possível desempacotar diretamente na primeira linha do laço for.
#for indice, nome in enumerate(lista):
#    print(indice, nome)

'''
Forma de desempacotar utilizando for dentro de outro for

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla: ')
    for valor in tupla_enumerada:
        print(f'\t{valor})




'''