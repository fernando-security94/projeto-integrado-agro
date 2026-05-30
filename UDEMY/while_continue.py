"""
Bloco de repetição while/continue
Contínue - Forma de pular um determinado valor dentro do laço while e continuar sua execução
"""

contador = 0

while contador <= 100:
    contador += 1
    

    if contador == 6:
        print('Não vou mostrar o', contador)
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue
    
    print(contador)

    if contador == 70:
        break
