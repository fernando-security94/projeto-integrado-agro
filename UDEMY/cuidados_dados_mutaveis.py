'''
Cuidados com dados mutáveis
=  -> copiado o valor (imutáveis)
=  -> aponta para o mesmo valor na memória (mutável)

'''
lista_a = ['Fernando', 'Poliane']
lista_b = lista_a

lista_a[0] = 'Jesus'
print(lista_b, lista_a)

'''
Quando ocorre uma situação na qual eu atribuo uma variável e seu valor à uma nova variável,
o que acontece é que eu acabo fazendo com o que as duas variáveis apontem para o mesmo valor, e não
criando uma cópia ou uma única nova variável. Se eu fizer uma alteração na lista_a, como no exemplo,
como ela foi atribuida a lista_b, ao exibir, ambas terão seus valores alterados. PS: Somente no caso de valores mutáveis,
como no caso, listas. Se fosse uma string, que é imutável, seria uma cópia. 

É possível criar uma cópia utilizando a função copy() e nesse caso, se eu alterar a variável original, a cópia não sofre alterações.
'''
lista1 = ['Fernando', 'Poliane']
lista2 = lista1.copy()

lista1[0] = 'Jesus'
print(lista1, lista2)

# For in em listas, iterando sobre cada valor da lista.
for letra in lista2:
    print(letra)

print()

for indice in lista_a:
    print(indice)