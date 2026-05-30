'''
Exiba os índices da lista

'''

# Minha resolução

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Felipe')
lista.append('Fábio')
lista.append(True)

for letra in range(len(lista)):
    print(letra, lista[letra], type(lista[letra]))

'''
Para exibir os índices primeiro, eu utilizei o laço for juntamente com range do tamanho da lista,
com isso, na medida que a lista for alterada para mais ou para menos, os índices também vão mudar. 
E, para exibir indice e valor paralelamente, exibi o iterador letra e a lista[letra] iterada. 

'''
print()
# Resolução professor:

lista1 = ['Fernando', 'Poliane', 'Marlos']
lista1.append('Tamires')
lista1.append('Edna')

indice = range(len(lista1))

for indice in indice:
    print(indice, lista1[indice], type(lista1[indice]))