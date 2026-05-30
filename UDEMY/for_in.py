"""
O laço for é uma forma de iteração, da mesma forma que usamos 
o while, porém, muito mais simples e resumido
"""

# Exemplo de iteração usando while

nome = 'Fernando'
indice = 0
tamanho_nome = len(nome)

while indice < tamanho_nome:
    print(nome[indice])

    indice += 1

print()

# Exemplo de iteração usando for in

nome1 = 'Fernando'
novo_nome1 = ''

# A variável letra foi criada dentro do laço for para receber os valores de cada iteração
for letra in nome:
    novo_nome1 += f'*{letra}'

    print(letra)
print(novo_nome1)
