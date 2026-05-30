'''
Introdução à funções (def) em Python.
Funções são trechos de códigos usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos), 
e retornar um valor específico.
Por padrão, funções em Python retornam None (não-valor)

'''

# def Print(a, b, c, ):
#     print(a, b, c,)

# Print(1, 2, 3)
# Print(4, 5, 6)
# Print(7, 8, 9,)

def saudacao(nome):
    print(f'Olá {nome}!')


saudacao('Fernando')
saudacao('Poliane')
saudacao('Marlos')
saudacao('Arthur')
saudacao()

'''
Nesse caso de função def(), a função saudacao recebeu um parâmetro nome, para que toda vez que executada
exiba a mensagem "Olá {nome}! A função def permite que a mesma seja executada diversas vezes com valores diferentes
como vemos a cima. Existe também, a possíbilidade de atribuir um argumento padrão ao parâmetro nome, que será exibido
quando a função for chamada sem nenhum valor. Caso nenhum argumento padrão seja atribuido, e a função seja chamada e
e não receber nenhum argumento, um erro 'TypeError: missing required argument' será levantado, o que singifica que o parâmetro
precisa receber 1 argumento. 


'''