'''
Gerar dígitos de CPF com Python

CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7


'''
# PRIMEIRO DÍGITO

import re
import sys

#cpf_enviado_usuario = input('Digite seu cpf: ').replace('.', '').replace('-', '')  # Substituindo com função replace() de forma encadeada. 

# Com o modulo re (Regular expressions), é possível limpar o código e tirar tudo de uma vez, 
# sem a necessidade de encadear através do replace()
cpf_enviado_usuario= re.sub(r'[^0-9]', '', input('Digite seu cpf: '))

entrada_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)

if entrada_sequencial:
    print('Você digitou dados sequenciais')
    sys.exit()
 
nove_digitos = cpf_enviado_usuario[:-2]
contador_digito_1 = 10


resultado_digito_1 = 0
for digito_1 in nove_digitos:
    print(digito_1, contador_digito_1)
    
    print(int(digito_1) * contador_digito_1)
    resultado_digito_1 += int(digito_1) * contador_digito_1
    contador_digito_1 -= 1

    resultado_mulitplicado_1 = resultado_digito_1 * 10
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
    print(digito_2, contador_digito_2)
    print(int(digito_2) * contador_digito_2)
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


# print()
# print(segundo_digito)
# print(f'O segundo dígito do CPF é {segundo_digito}')

print(f'O CPF completo é {cpf_gerado_pelo_calculo}')

print()
# VALIDAÇÃO DE CPF

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print('O CPF digitado pelo usuário é valido!')
else:
    print('O CPF digitado pelo usuário é INVALIDO!')


'''
Dissertando exerício de achar dígitos CPF

Módulo re (replace) será importado para substituir pontos e traços.
Módulo sys será importado para encerrar o programa em caso de alguma condição incorreta
for ativada.
O usuário receberá um input para digitar seu CPF.
Logo depois, uma fórmula foi feita para evitar uma sequência, ex: 1111; Uma variável receberá essa fórmula
Se o input for sequência, uma mensagem será exibida e o programa será encerrado
através de sys.exit().

Uma variável receberá o valor que o usuário digitou no input menos os dois últimos dígitos
nove_digitos = cpf_enviado_usuario[:-2]
um contador, que será reverso, para achar o primeiro dígito foi criado com valor = 10
variável resultado_digito_1 = 0 foi criada para que o valor encontrado possa ser adicionado.

Dentro de um laço for, vamos iterar sobre nove_digitos e 
vamos multiplicar sobre cada valor do contador reverso e adicionar a
resultado_digito_1.

Após encontrar esse resultado, dentro da variáveç resultado_multiplicado
vamos fazer a multiplicação do resultado_digito_1 por 10 e
na variável primeiro_digito receberá o restante(módulo) do
resultador_multiplicado por 11.

Se primeiro_digito for maior que 9, primeiro_digito será igual a 0.
Caso contrário, terá seu valor próprio.

Para achar o segundo dígito, uma variável dez_digitos será criada
e receberá nove_digitos + str(primeiro_digito)
Um contador igual a 11 será criado e resultado_digito_2 também será igual a 0.

O restante do código será identico ao primeiro dígito.
Laço for, seguido de contador reverso, multiplicação do valor e restante da divisão por 11.

A variável cpf_gerado_pelo_calculo receberá a concatenação 
entre nove_digitos, primeiro_digito, segundo_digito em uma fstring.

Para finalizar, uma condição if foi criada para checar
se o cpf_enviado_usuário é == cpf_gerado_pelo_calculo
Se for verdadeira, uma mensagem de validação será exibida
Caso contrário, uma mensagem de invalidação será exibida.


'''