"""
https://docs.python.org/pt-br/3/library/stdtypes.html

Imutáveis ja vistos: str, int, float, bool
"""
string = 'fernando'

# Substitui o caractere do índice 2 por ABC, mas é possível fazer a mesma coisa com
# a função replace

outra_string = f'{string[2]}ABC{string[4:]}'

# A função zfill() Adiciona uma quantidade de zeros de acordo com o que o dev digitar
# Nesse caso:  complete com zeros até chegar em 80 caracteres,
# incluindo o valor da variável
print(string.zfill(80))

print(outra_string)


# Função capitalize transforma a primeira letra em maiúscula
print(string.capitalize())



# string = 'Fernando'

# print(string.replace('a', '@') and string.replace('o', '0'))
# print(string.replace('F', '7'))
