"""
Flag - Bandeira - Marca um local
None = Não valor
is e is not = é ou não é (tipo, valor identidade)
id = identidade de um elemento na memória

"""
# Função id
# v1 = 'a'
# v2 = 'a'
# print(id(v1))
# print(id(v2))

# Utilizei a função input com typecast para bool:
#condicao = bool(input('True or False: '))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo!')
else:
    passou_no_if = None
    print('Não faça nada!')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)


if passou_no_if is None:
    print('Não passou no if!')

if passou_no_if is not None:
    print('Passou no if!')  # Só vai passar no if se a condição for True