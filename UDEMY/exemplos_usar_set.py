"""
Exemplos de uso dos set()

"""

letras = set()

while True:
    letra = input('Digite uma letra: ')
    letras.add(letra)

    if 'l' in letras:
        print('Parabéns, você digitou a letra secreta')
        break
    
    print(letras)
