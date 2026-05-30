'''
Tipo de dados tuples (tuplas) = lista imutável
Ou seja, não é possível alterar qualquer valor da tupla através do índice.
É possível desempacotar tuplas usando a mesma forma de listas.
Para criar tuplas, é simplesmente uma lista sem colchetes ou utilizar parenteses


'''

nomes = 'Fernando', 'Poliane', 'Arthur'
nome, *_ = nomes

print(nomes, nomes[1], nome, _, sep=', ')

print(type(nomes))