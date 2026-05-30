numero = int(input("Digite um numero: "))

def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é impar')
    return numero

resultado = par_ou_impar(numero)

