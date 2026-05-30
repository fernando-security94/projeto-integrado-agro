"""
Empacotamento e desempacotamento de dicionários

"""
a, b = 1, 2
a, b = b, a
print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()  #empacotamento interno
# print(a1, a2, sep=': ')
# print(b1, b2, sep=': ')

# for chave, valor in pessoa.items():
#     print(chave, valor, sep=': ')

pessoa = {
    'nome': 'Poliane',
    'sobrenome': 'Novaes',

}

dados_pessoa = {
    'idade': 16,
    'altura': 1.60,
}

pessoa_completa = {**pessoa, **dados_pessoa}  # ** Serve para extração de todo o conteúdo dos dicionários

print(pessoa_completa)

for chave, valor in pessoa_completa.items():  # Iterando sobre os dicionários desempacotados
    print(chave, valor, sep=': ')

print()


# args e kwargs (keyword arguments / argumentos nomeados)
def argumentos_nomeados(*args, **kwargs):
    print('ARGUMENTO NÃO NOMEADO:', args)  # Argumentos não nomeados são enviados separadamente em args

    for chave1, valor1 in kwargs.items():
             
        print(chave1, valor1, sep=': ')

                    # args
argumentos_nomeados(1, 2, nome='Joana', qualquer=123)

print()

# desempacotar kwargs
argumentos_nomeados(**pessoa_completa)  # Passada de função em caso de ter muitos argumentos

print()

configuracoes = {
    'arg1': 'valor1',
    'arg2': 'valor2',
    'arg3': 'valor3',
    'arg4': 'valor4',
}

argumentos_nomeados(**configuracoes)