"""
Bloco de repetições
while(enquanto)- Executa uma ação enquanto uma condição for verdadeira
Loop infinito - Quando um código não tem fim, ou seja, sempre será verdadeiro e portanto
o laço while não vai parar de executar. 

"""

# condicao = True

# while condicao:
#     nome = input('Qual é o seu nome? ')
#     print(f'Seu nome é {nome}')
    
#     # Break vai interromper o laço while quando as condições forem executadas.
#     # E o break está ligado ao while mais próximo, valendo para o if, também. 
#     # É uma forma de impedir um loop infinito
#     break

contador = 0

# Gerei um contador automático, iniciando com valor zero
# e quando contador for igual a 10, break.

while contador < 10:
    
    # A cada volta, add 1 ao contador
    contador = contador + 1
#   contador += 1   Dessa forma, é o mesmo que o exemplo acima. 
    print(contador)

print('Acabou')