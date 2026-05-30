"""
Iterável ->  str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador

"""

# for letra in texto: Desmembrando laço for

texto = 'Fernando'  # iterável
iterador = iter(texto)  # Iterador através da função iter

while True:
    try:
        letra = next(iterador)  # entrega o próximo valor do iterável
        print(letra)
    except StopIteration:
        break


"""
Enquanto houver condições verdadeiras, ou seja, valores a serem
iterados, a função next que está no iterador entregará o proximo valor
à variável letra, que por sua vez será exibida a cada laço.  
Quando não houverem mais valores a serem iterados, o erro StopIteration
será levantado, quebrando o programa, mas, como estão dentro do bloco
try/except, esse erro será tratado como uma exceção, e assim que surgir
a função break sairá do laço. 

"""
print()


# O que foi feito com while, pode também ser feito com for
# Para cada coluna i, vai ter uma coluna j com range(1, 3), ou seja, 1 e 2. 0 pra 1, 0 pra 2
# 1 pra 1, 1 pra 2, e assim sucessivamente

for i in range(10):
    if i == 2:
        print('i é 2, pulando..')
        continue

    if i == 8:
        print('Seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
    
else:
    print('Laço for completo com sucesso')  # Não será completo por conta do break