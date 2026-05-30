"""
Manipulando chaves e valores em dicionários.

"""
pessoa = {}
pessoa2 = {}

##
##

# É possível criar chaves e valores com sinal de atribuição, depois de criar o dicionário vazio.

chave = 'Nome completo'  # Criando chaves de forma dinâmica, se caso mudar o valor, não vai gerar nenhum erro
                         # por estar atribuída a uma variável.

pessoa[chave] = 'Fernando Ribeiro'
print(pessoa[chave])   
print(pessoa)

print()

pessoa2[chave] = 'Poliane Novaes'
print(pessoa2[chave])
print(pessoa2)

print()

# Checagem de índice inexistente em dicionários pode ser feita através de get() ou condição if + get.
# Por natureza, a função get() sempre retornará None, mas é possível atribuir uma mensagem após
# o índice que deseja acessar.
print(pessoa.get('sobrenome'))

print()

# Usando if

if pessoa.get('sobrenome') is None:  # Também pode ser if pessoa.get('sobrenome') is not none:
    print('Esse índice não existe')
else:
    print('Esse índice existe.')