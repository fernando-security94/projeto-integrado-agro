frase = 'O Python é uma linguagem de programação '\
    'multiparadigma.'\
    'Python foi criado por Guido Van Rossum.'

i = 0
qtde_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtde_apareceu_mais_vezes < qtd_atual:
        qtde_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual
    

    i += 1

print('A letra que apareceu mais vezes foi '
f'"{letra_apareceu_mais_vezes}" que apareceu '
f'{qtde_apareceu_mais_vezes}x')

'''
Debuger por escrito:

Iteração de styrings com bloco while, que foi utilizado para criar um contador
de letras, e também para exibir a letra que mais se repetiu.
Descrição do código:
Temos uma variável "frase" que recebe um pequeno texto.
Foi criado uma variável "i" que por convenção é usada para index.
Foi criado um bloco while, que fará uma iteração em cada caractere do texto
, enquanto "i" for menor que o tamanho da frase "len(frase),
 uma nova variável" letra_atual" receberá uma letra a cada iteração.
Uma variável qtde_letras_atual irá receber a contagem da frase
iterada com "letra_atual
Se a "letra_atual for um espaço, não será contabilizado, e a iteração continuará
até a proxima letra.
Uma variável qtde_apareceu_mais_vezes foi criada para encontrar qual letra
mais apareceu. No bloco if:  se qtde_apareceu_mais_vezes for menor que
qtde_letras_apareceu_atual, a mesma receberá o valor da qtde_atual 
e letra_apareceu_mais_vezes receberá o valor de letra_atual.
Lembrando que i += 1 foi para o final, sendo relacionado ao while, no topo.
Por fim, vamos exibir atra vez de string e fstrings a letra_apareceu_mais_vezes 
e "qtde_vezes_letra_apareceu. Caso duas letras empatem o número de vezes que apareceram,
apenas a letra que foi repetida primeiro, será exibida. 

'''