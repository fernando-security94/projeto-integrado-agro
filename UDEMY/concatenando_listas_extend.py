'''
Concatenando listas com + e extend
'''
lista_a = [1, 2, 3, 4, 5]
lista_b = [6, 7, 8, 9, 10]

lista_c = lista_a + lista_b  # concatenando com + através de polimorfismo.

# Se eu jogar a funcao extend em uma variavel, ira retornar None
# porque a ação extend, só trabalha de fato na lista a ser estendida
lista_d = lista_a.extend(lista_b)  

lista_a.extend(lista_b)  # Essa é a maneira correta de aplicar o extend em lista

print(lista_c) 
print(lista_a)
