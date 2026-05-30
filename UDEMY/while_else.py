""" While/Else """

string = 'Valor qualquer'

i = 0  # i é normalmente utilizado para index na programação. 
while i < len(string):
    letra = string[i]

    print(letra)

    i += 1
else:  # Caso tenha um break no bloco while, o else não será executado
    print('O else foi executado')