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