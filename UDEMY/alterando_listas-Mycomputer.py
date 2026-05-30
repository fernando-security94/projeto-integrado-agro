"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis, índices e fatiamento
Métodos úteis:
- append -> Adiciona item ao final da lista
- insert -> Adiciona um item no local (índice) escolhido
- pop -> Remove último item da lista ou índice escolhido
- del -> Apaga um índice 
- remove -> Remove um VALOR específico da lista. Não é possivel acessar pelo índice
- clear -> Limpa a lista
- extend -> Estende a lista
-  + -  -> Concatena listas 
Create, Read, Update, Delete - CRUD


"""
lista = [10, 20, 30, 40]
lista.append(50)
lista.append(60)
lista.pop()
lista.append(70)
lista.append(80)

valor_removido = lista.pop()

print(lista, 'Valor removido:', valor_removido)

lista2 = [123, 'Abba', 'YHWH', True]

lista2.extend('Fer')  # Extende a lista com valores iterados (separados)

lista2.insert(8, 'Jesus')  # Em insert, primeiro argumento é o índice a ser inserido, depois o valor
del(lista2[1])
#del lista2[-1]  Tambem funciona sem parenteses, apenas com espaço

# lista2.clear()
# print(f'A lista foi limpa : {lista2}')

# del(lista2[1])  # Somente a função del vem antes da variável e não usa ponto, apenas parenteses.


print(len(lista2))
print(lista2)

'''
Listas são consideradas um dos tipos de objetos mais maleáveis de 
se trabalhar, pois podem receber qualquer tipo de dados, e por se
tratar de um tipo mutável, existem diversas formas de ser manipulada.

Nesse caso temos uma lista que recebe alguns valores. Na sequência, com a função
.append(adiciona valores no fim da lista) dois valores foram
adicionados. Depois, com a função .pop(remove o último valor e nao usa índice), o último valor
foi removido. E depois, novamente, mais dois valores foram adicionados com .append()
O último valor removido foi atribuído a uma variável através de 
variável = lista.pop()

Uma segunda lista foi criada com diversos tipos de valores.
Ao usar a função .extend(), só recebe valores iteráveis, ou seja,
serão adicionados automaticamente iterados, no caso de uma str,
os valores serão separados por unidade, então 'Fer', será exibido
'F', 'e', 'r'.

A função .insert() precisa de dois argumentos para funcionar. O primeiro
é o índice onde o valor será inserido, e o segundo é o valor, de fato.

A função del é executada também atraves do índice, mas em colchetes,
podendo ser com ou sem parenteses.
del(lista[1]) ou del lista[1]

Por fim, o tamanho da lista2 foi exibido através de len(), e 
a lista2 também foi exibida


'''