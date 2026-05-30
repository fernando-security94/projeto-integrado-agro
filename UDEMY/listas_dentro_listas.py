lista = [
    # Indice da lista
    #Indice da lista dentro da lista
    #   0       1
    ['Maria', 'João'], # 0
    #   0       1
    ['Edna', 'Mingau'], # 1
    #   0           1           2
    ['Fernando', 'Poliane', 'Marlos', 'Iraci', 'Ruidemberg'], # 2
]

print(lista)

print(lista[1][0])  # Vai acessar o índice 1 da lista e exibir o valor do índice 0 dessa lista interna. 
print(lista[2][0])
print(lista[2][1])
print(lista[2][3])

print()


for sala in lista:
    print(f'A sala é {sala}')
    for nome in sala:
        print(nome)