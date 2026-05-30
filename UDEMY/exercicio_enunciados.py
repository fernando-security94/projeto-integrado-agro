'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se esse número
é par ou impar. Caso o usuário não digite um número inteiro, informe
que o número não é inteiro
'''

numero = input('Digite um número inteiro: ')

# Resolução professor usando try / except:
try:
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'
    
    print(f'O número {numero_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro!')


# Minha resolução

# if numero.isdigit():
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print(f'O número {numero_int} que o usuário digitou é par!')
#     elif numero_int % 3 == 0:
#         print(f'O número {numero_int} que o usuário digitou é impar!')
# else:
#     print('O número precisa ser inteiro!')

print()


'''
Faça um programa que pergunte a hora ao usuário, e baseando-se no horário descrito,
exiba a saudação adequada!
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.
'''

# Minha resolução
horario = input('Que horas são: ')

if horario >= '0:00' and horario <= '11:59':
    print('Bom dia!')
elif horario >= '12:00' and horario <= '17:59':
    print('Boa tarde!')
elif horario >= '18' and horario <= '23:59':
    print('Boa noite!')
elif horario >= '24':
    print('Esse horário não existe!')

print()

# Resolução professor
entrada = input('Digite a hora em números inteiros:? ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Esse horário não existe!')
except:
    print('Digite apenas números inteiros!')

''''
Faça um programa que pergunte o nome do usuário, se o nome tiver 4 letras ou menos, escreva:
Seu nome é muito curto; se tiver entre 5 e 6 letras escreva: 
Seu nome é normal; Maior que 6 letrar: seu nome é muito grande:
'''

# Minha resolução
# nome = input('Qual é o seu nome: ')
# nome_len = len(nome)


# if nome_len <= 4:
#     print('Seu nome é muito curto')
# elif nome_len >= 5 and nome_len <= 6:
#     print('Seu nome é normal!')
# else:
#     print('Seu nome é muito grande!')
    

# Resolução professor

nome =  input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto!')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é grande!')
else:
    print('Digite mais de uma letra!')

