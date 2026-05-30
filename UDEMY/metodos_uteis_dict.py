"""
Métodos úteis dos dicionários em Python

len- quantas chaves
keys - iterável com as chaves
values - iterável com valores
items - iterável com chaves e valores 
setdefault - adiciona valor se a chave não existe
copy - retorna cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último ítem selecionado
update - atualiza um dicionário com outro

"""

dicionario = {
    'nome': 'Fernando', 
    'sobrenome': 'Ribeiro',
}

# Usando setdefault em caso de acessar uma chave inexistente ou definir por padrão.
dicionario.setdefault('idade', 29)



print(len(dicionario))
print(tuple(dicionario.keys()))
print((dicionario.items()))
print(list(dicionario.values()))




# exibe somente as chaves
for chave in dicionario.keys():
    print(chave)

# exibe somente os valores
for valor in dicionario.values():
    print(valor)

# Exibe chaves e valores
for chaves, valores in dicionario.items():
    print(chaves, valores, sep=': ')
print()


# Utilizando get()
p1 = {
    'nome': 'Poliane',
    'sobrenome': 'Novaes',
}

print(p1.get('nome', 'Não existe'))  # Valor padrão caso a chave seja inexistente

# Utilizando pop()
# chave_apagada = p1.pop('sobrenome')

# print(chave_apagada)
# print(p1)

# # Utilizando popitem() - elimina o última chave adicionado

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# Utilizando update() O dicionário original será atualizando, mas através de outro dicionário. 
# E ao criar novas chaves, essas serão adicionadas ao dicionário original.

p1.update({
    'nome': 'novo valor',
    'idade': 29

})
print(p1)

# É possivel update() com argumentos nomeados:

p1.update(nome='Atualizei de novo', idade=700)
print(p1)

# Update() utilizando tuplas:

tupla = (('nome', 'Mudei de novo'), ('idade', 800))
p1.update(tupla)
print(p1)

# Update utilizando listas:
lista = [['nome', 'Função update é demais'], ['idade', 900]]
p1.update(lista)
print(p1)



# Na função update, é possível receber iteráveis que irão se comportar como dicionário. No caso vimos tupla e lista
# Nao funciona com string