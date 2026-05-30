# Cria opçao para o usuário sair
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-*/): ')

    numeros_validos = None

    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos')
        continue

    operadores_permitidos = '+-*/'


    if operador not in operadores_permitidos:
        print('Operador inválido!') 


    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue
    
    print('Confira o resultado da sua operação: ')
    if operador == '+':
        print(f'{numero_1} + {numero_2} =' , numero_1 + numero_2)
    elif operador == '-':
        print(f'{numero_1} - {numero_2} =' , numero_1 - numero_2)
    elif operador == '*':
        print(f'{numero_1} * {numero_2} =' , numero_1 * numero_2)
    else:
        print(f'{numero_1} / {numero_2} =' , numero_1 / numero_2)


    sair = input('Deseja sair [s]im: ').lower().startswith('s')
    
    if sair is True:
        print('Você saiu!')
        break
    else:
        continue


'''
Calculadora usando while
Dentro do laço while, para haver repetições e dar opção para o usuário sair, haverão 3 inputs. 
numero_1, numero_2 e o operador aritimético. Uma variável numeros_validos foi atribuída o valor None.

Dentro de um bloco try, o programa tentará converter o input de numero_1 e numero_2 para bool, se isso for possível, numeros_validos
será True, pois permitirá de fato que as operações sejam realizadas, se nao forem float, numeros_validos continuarão None, ou seja,
um não-valor. Dentro de um bloco if, se numeros_validos for None, exiba uma mensagem de erro. 

Atribua os operadores permitidos a uma variável, no caso, operadores_permitidos.
Criar uma condição if que se o operador digitado não estiver em operadores_permitidos, exiba uma mensagem de erro. 
Dentro de outra condição if, se o usuário digitar mais de um operador, através de len(), exiba uma mensagem de erro, seguido
de continue, para voltar ao início do laço e tentar novamente. 

Uma mensagem será exibida para checar o resultado das operações.
Uma série de condições serão criadas para identificar o tipo de operação com laço if, elif, else.

Ao final do resultado da operação, a variável sair receberá um input, sendo que se o usuário digitar com letra maiúscula ou minúscula,
será transformada em minúscula com a função .lower() e qualquer resposta com 's' com a função startswith('s'), será definida como True.
Dentro de um laço if, se sair for True, exiba mensagem e break, caso contrário, volte para o início do calculo. 





'''