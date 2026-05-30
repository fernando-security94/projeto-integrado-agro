'''
Introdução ao empacotamento, desempacotamento de listas 

'''

lista = ['Fernando', 'Poliane', 'Arthur']
nome1, *resto = lista
print(nome1, resto)

# ou

nome, *resto2 = ['Fernando', 'Poliane', 'Arthur']
print(nome, resto2)

# ou qualquer uma das duas formas, mas ao invés de utilizar *variável, por convenção pode-se usar *_ 
# sinalizando que a variável não será utilizada. O _ pode ser colocado em qualquer posição,
# de acordo a necessidade do Dev.


lista2 = ['Fernando', 'Poliane', 'Arthur']
nome2, *_ = lista2
print(nome2)

# Usando _ nos dois primeiros valores de forma individual, ou podendo agrupar através de *, para desempacotar o terceiro valor.
lista3 = ['Fernando', 'Poliane', 'Arthur']
_, _, nome3 = lista3
print(nome3)

'''
Duas formas de desempacotar apenas um valor da lista, e empacotar o restante em uma única 
variável, utilizando *variável. Podendo criar uma lista e depois atribuir às variáveis de desempacota/empacotamento,
ou, diretamente atribuindo os valores da listas à essas variáveis.
Se eu atribuir menos valores do que a quantidade de variáveis, o erro "Not enough values to unpack" será exibido, 
e se eu atribuir mais valores do que a quantidade de vairáveis, o erro "Too many values to unpack", será exibido.
'''