import random

import random

for _ in range(100):

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


'''
Usando o mesmo código do gerador de CPF, vamos indentar dentro de um laço for com uma variável _ 
que significa que não será usada ao longo do programa em um range de 100, dessa forma
o programa terá a capacidade de gerar 100 CPF's matemáticamente válidos a cada execução:

for _ in range(100):
    código do gerador indentado
'''