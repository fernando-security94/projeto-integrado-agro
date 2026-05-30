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
    print('ARGUMENTO NÃO NOMEADO:', args)  # Argumentos não nomeados são enviados separadamente em args, em ordem de execução

    for chave1, valor1 in kwargs.items():
             
        print(chave1, valor1, sep=': ')

                    # args
argumentos_nomeados(1, 2, 3, 4, nome='Joana', qualquer=123)  # argumento nao nomeado sera exibido em tupla

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

argumentos_nomeados(1, 2, 3, 4, 5, 6, **configuracoes)

# argumentos_nomeados(**configuracoes, 1, 2, 3) # SyntaxError - Positional argumen follows keyword argument unpacking

# argumentos_nomeados(nome2 = 'Jesus', 1, 2, 3, **configuracoes)  # SyntaxError - Positional argument follows keyword argument


'''
Em empacotamento e desempacotamento de dicionários, 
podemos fazer de forma simples, atribuindo a uma variável, como 
no código acima.

Temos dois dicionários com suas respectivas chaves e valores.

Para desempacotá-los de forma rapida e simples, vamos atribui-los
a variável pessoa_completa = {**pessoa, **dados pessoa}. Dessa forma
utilizando ** vamos desempacotar todos as chaves e valores em um 
único dicionário, ja atribuído a variável.

Usando um laço for, vamos iterar sobre a variável que recebeu os
dois dicionários desempacotados, através de
for chave, valor in pessoa_completa.items()

Empacotar e desempacotar args/kwargs:

Criamos uma função def argumentos_nomeados() que ja recebe
**args e **kwargs, ou seja, ja desempacotados e prontos para serem
atribuídos a algum lugar.

Uma mensagem será exibida para separar os argumentos posicionais
em uma tupla, e o que vier depois disso, serão argumentos nomeados.
Não é permitido argumentos poisionais depois de utilizar ao menos
um argumento noemado.

Dentro de um laço for, chave e valor in kwargs.items() para
que os argumentos nomeados sejam exibidos de forma iterada.

Ao chamar a função argumento_nomeados() uma série de argumentos
foram passados. Os argumentos 1, 2, 3, 4 são argumentos
posicionais, ja nome='Joana' marca o início 
de argumentos nomeados, e depois disso, todos os argumentos
devem ser nomeados, mas podem ser de qualquer tipo, str, int, float etc.

Com essa função pronta, podemos executá-la desempacotando **pessoa_completa,
que é o dicionário que recebeu dois dicionários desempacotados
no início do código. Nessa execução, novos argumentos podem ser
adicionados, desde que mantenham a ordem de sintaxe.

Um outro dicionário {configuracoes} foi criado, com chaves e valores.

A função argumentos_nomeados() foi executada novamente, e recebeu
argumento_nomeados(1, 2, 3, 4, 5, 6, **configuracoes), ou seja,
de 1 a 6, serão argumentos posicionais, e **configurações, será o
dicionário desempacotado, sendo considerado um argumento nomeado.




'''