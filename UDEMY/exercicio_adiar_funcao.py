# Exercício adiamento de execução de funções

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna



soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))


"""
O adiamento de função se deu de forma simples, apesar de ser
um assunto complexo.
A função def criar_funcao recebe dois argumentos, um deles
é x.
Dentro de def criar_funcao uma def interna é criada, e recebe
apenas y, pois a função externa ja possui o x.
A def interna irá retornar os argumentos de criar_funcao e seu proprio.
E vamos return interna sem executar ao fim do código, adiando
a execução antecipada de soma e multiplica.

ficando: 
def interna(y):
    return funcao(x, y)
return interna


PS: Forma de adiar a execução da função. Também é possível adiar a execução dos parâmetros, mudando para a função interna
"""