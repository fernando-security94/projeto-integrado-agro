'''
Iterando string com while

'''

nome = 'Fernando Ribeiro'
nome2 = 'Poliane Novaes'
novo_nome = ''
novo_nome2 = ''

# Exercício guiado para colocar * entre cada letra do nome

print(nome)
print(len(nome))

indice = 0
indice2 = 0
while indice < len(nome) and indice < len(nome2):
    letra = nome[indice]
    letra2 = nome2[indice2]
    novo_nome += f'*{letra}'
    novo_nome2 += f'*{letra2}'

    indice2 += 1
    indice += 1

novo_nome2 += '*'
novo_nome += '*'

print(novo_nome)
print(novo_nome2)