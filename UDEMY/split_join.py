'''
split e join com list e str
split - divide uma str
join - unde uma str
strip - corta os espaços do começo e do fim
rstrip - corta os espaços da direita
lstrip - corta os espaços da esquerda

'''

string = ('         Olá, tudo bem?          ')

string_crua = string.split(',')  # O argumento dentro da função split é exatamente onde o usuário quer dividir. 

lista_frases = []  # forma de alterar uma lista sem mexer na lista original

for i, frase in enumerate(string_crua):
    lista_frases.append(string_crua[i].strip())
    

for j, frase_2 in enumerate(lista_frases):
    print(lista_frases[j].strip())



# print(string)
# print(string_crua)  # Apesar de ser inicialmente uma string, ao usar split, a função retornará uma lista uma lista.
# print(string_fixed)

string_unida = ', '.join(lista_frases)
print(string_unida)

'''
A função join() deve ser atribuída a uma nova variável que receberá a junção, o primeiro argumento deve ser o valor
separador, através de uma string vazia, um '-' ou até mesmo uma outra variável como:
string_unida = string.join(lista_frases), mas isso pode retornar um valor estranho e sem sentido

'''

nomes = 'Fernando', 'Poliane', 'Marlos'
nomes_unidos = []

for k, nome in enumerate(nomes):
    nomes_unidos.append(nomes[k])
nomes_unidos = '*'.join(nomes)
print(nomes_unidos)


