'''
Gerador de CPF

'''
import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contador_digito_1 = 10


resultado_digito_1 = 0
for digito_1 in nove_digitos:
    #print(digito_1, contador_digito_1)
    
    #print(int(digito_1) * contador_digito_1)
    resultado_digito_1 += int(digito_1) * contador_digito_1
    contador_digito_1 -= 1

    resultado_mulitplicado_1 = resultado_digito_1 * 10 % 11
    primeiro_digito = resultado_mulitplicado_1 % 11

    if primeiro_digito > 9:
        primeiro_digito = 0
    else:
        primeiro_digito = primeiro_digito

print()
# cpf_incompleto = f'{nove_digitos}{primeiro_digito}'
# print()
# print(primeiro_digito)
# print(f'O primeiro dígito do CPF é {primeiro_digito}.')
# print(cpf_incompleto)
# print()

# SEGUNDO DÍGITO

dez_digitos = nove_digitos + str(primeiro_digito)
contador_digito_2 = 11
resultado_digito_2 = 0

for digito_2 in dez_digitos:
    #print(digito_2, contador_digito_2)
    #print(int(digito_2) * contador_digito_2)
    resultado_digito_2 += int(digito_2) * contador_digito_1
    contador_digito_2 -= 1
    resultado_mulitplicado_2 = resultado_digito_2 * 10 % 11
    segundo_digito = resultado_mulitplicado_2 % 11

    if segundo_digito > 9:
        segundo_digito = 0
    else:
        segundo_digito = segundo_digito


# resultado_multiplicado_2 = resultado_digito_2 * 10
# segundo_digito = resultado_digito_2 % 11

# segundo_digito = segundo_digito if segundo_digito > 9 else 0  # Condição if de uma linha

cpf_gerado_pelo_calculo= f'{nove_digitos}{primeiro_digito}{segundo_digito}'

print(f'O CPF completo é {cpf_gerado_pelo_calculo}')



# print()
# print(segundo_digito)
# print(f'O segundo dígito do CPF é {segundo_digito}')




'''
Usando o mesmo código para encontrar os dígitos do CPF,
nesse caso, vamos cria um gerador aleatório de CPF
matemáticamente validos.
Vamos importar o módulo random, e utilizaremos a função randint,
para gerar números inteiros aleatóriamente.

A variável nove dígitos receberá uma string vazia, e 
dentro e um laço for in range(9) referente aos 9 dígitos
a cada laço do range, nove_dígitos terá um numero de 0 a 9 adicionado atraves de
nove_digitos += str(random.randint(0,9))

Depois, é só seguir a partir do contador_digito_1

'''