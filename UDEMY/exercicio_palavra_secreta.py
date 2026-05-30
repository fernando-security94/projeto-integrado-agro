"""
Faça um jogo para o usuário adivinhar qual a palavra secreta 
- Proponha a palavra secreta e dê a oportunidade ao usuário digitar apenas uma letra.
- Ao usuário digitar a letra, o programa deve conferir se a letra está na palavra secreta
- Se a letra estiver na palavra secreta, exiba a letra, se não estiver, exiba 
"Essa letra não existe" e conte a quantidade tentativas do usuário
"""
# Módulo que vai limpar o terminal após todos os códigos serem
# executados#

import os


palavra_secreta = 'Jesus'
letras_acertadas = ''
tentativas = 0

while True:
    
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra por vez!')
        continue
    
    if letra_digitada in palavra_secreta:
         letras_acertadas += letra_digitada
         
    palavra_formada = ''   
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabens! Você descobriu a palavra secreta!')    
        print(f'A palavra era {palavra_secreta}')
        print(f'O número de tentativas foi de {tentativas} tentativas!')
        letras_acertadas = ''
        palavra_formada  = ''
        tentativas = 0
        

"""
Dissertando o exercício:
Antes mesmo de criar as variávei, é preciso criar um laço while True,
para que a aplicação continue rodando, mesmo depois de todas as condições match.
Feito isso, foram criadas 3 variáveis de antemão, a palavra_secreta que, de fato
é a palavra a ser adivinhada, a letra_acertada que receberá uma string vazia e 
tentativas que será igual a 0, pois adicionará 1 a cada tentativa do usuário.
Dentro do laço while, uma nova variável letra_digitada terá um input, que futuramente será 
adicionada e salva a cada laço em letra_acertada, caso seja correte. 
A cada input digitado, tentativa += 1.
Se o usuário digitar mais de uma letra por vez, uma mensagem de erro será exibida,
e com continue, voltará ao inpuut, já tendo adicionado uma tentativa. 
Na condição if se a letra_digitada estiver in palavra_secreta, a letras_acertadas terá
letra_digitada adicionada a cada tentativa. 
Nova variável palavra_formada receberá uma string vazia, pois receberá todas as letras acertadas.
No laço for, iteração em palavra_secreta, se letra_secreta estiver in letras_acertadas
a palavra_formada receberá a letra_secreta a cada tentativa. Caso naõ esteja, será
adicionado um * dentro de palavra_formada. A palavra_formada será exibida a cada laço.
Condição if, já pra exibir se o usuário ganhou o jogo, se palavra_formada for igual a palavra_secreta:
Será exibida uma mensagem de vitória, qual era a palavra_secreta e o número de tentativas.
Para que o jogo seja recomeçado, as variáveis letras_acertadas, palavra_formada e tentativas
serão chamadas novamente, porem zeradas com strings varias e 0 (tentativas). 
Foi importado o módulo os, para limpar o terminal se a o usuário acertar todas as letras
deixando mais clean para que as mensagens seguintes sejam exibidsas.








"""

        








