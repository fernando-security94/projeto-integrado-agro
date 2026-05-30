"""
https://brasilescola.uol.com.br/matematica/conjunto.htm

- Sets- Conjuntos em Python (tipo set)
- Representados graficamente pelo Diagrama de Venn 
- Sets em Python são mutáveis, porém aceitam apenas tipos 
imutáveis como valor interno. 
"""

# Criando um set:
# set(iterável) ou {1, 2, 3}

# s1 = set('Fernando')  # Dessa forma, aparentemente só aceita 1 argumento. Quando usado dessa forma, geralmente
# # será um set vazio.
# print(s1, type(s1))

# ou

# s2 = {'Fernando', 123, 'Poliane'}  # Set com dados, utilizando chaves. 
# print(s2, type(s2))

# # Se eu colocar um tipo mutável dentro do set, causará o erro TypeError: Unhashable type 'list
# # set_lista = {[1, 2, 4, 4, 5, 10, 10, 10]}

# # Seus valores serão sempre únicos, ou seja, não haverá valor repetido, a função set faz a limpeza de forma automática.
# set_1 = {1, 2, 4, 4, 4, 4, 5, 6, 7, 7, 8, 'Fernando', 'Fernando', 9, 10}
# print(set_1)

# # É possível utilizar type cast com set para eliminar valores duplicados:
# lista = [1, 1, 2, 3, 4, 4, 5]
# print(set(lista))


"""
Sets são eficientes para remover valores duplicados de iteráveis.
- eles não tem índices;
- eles não garantem ordem (aleatórios);
- eles são iteráveis (for in, not in)

Métodos úteis:
add, update, clear, discard 
"""
# Método add() - adiciona valores ao set
s1 = set()
s1.add('Fernando')
s1.add(100)
s1.add('Poliane')
s1.add(True)
print(s1)

s1.update(('Arthur',))  # Adiciona o valor de forma iterada a não ser que seja tupla ou list, podendo não seguir a ordem correta.
print(s1)

s1.discard(('Arthur')) # Descarta um valor de forma selecionada! É preciso colocar o argumento a ser descartado
s1.discard('Poliane')
print(s1)


s1.clear() # Limpa o set por completo. Não recebe nenhum argumento.
print(s1)

"""
Operadores úteis
- união | união (union) - Une
- intersecção & (intersection) - Itens presentes em ambos
- .difference() - diferença - Itens presentes apenas no set da esquerda
- .symetric_difference()- diferença simétrica ^ - Itens que não estão em ambos

"""

set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
set_3 = set_1.union(set_2)  # Ou podemos usar | ao inves de .union
set_4 = set_1.intersection(set_2)  # ou & 
set_5 = set_1.difference(set_2)  # ou - sinal de menos
set_6 = set_1.symmetric_difference(set_2)  # ou ^  


print(set_3, set_4, set_5, set_6, sep=', ')
