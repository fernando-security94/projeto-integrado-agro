"""
Variáveis livres  + nonlocal
"""

def fora(x):
    a = x  # Variável livre por não estar no escopo da função dentro()

    def dentro():
        return a  # A função interna só pode ler a free var
    return dentro

dentro1 = fora(10) 
dentro2 = fora(20)
dentro3 = fora(30)
print(dentro1())
print(dentro2())
print(dentro3())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))  
print(c('c'))
print(c('d'))
print(c('e'))

final = c()
print(final)

'''
Variáveis livres são variáveis que não estão no escopo de funções
internas, porém, essas funções internas podem ler as variáveis
livres. Para que uma função interna tenha acesso a variável livre
usa-se a função 'nonlocal *nome variável' 

Nesse código, temos a função def fora(x) que recebe um argumento.
Esse argumento foi atribuído à uma variável livre.
Dentro de def fora(x) foi criada a função def dentro() que 
retorna a variável livre, lembrando que a função dentro() só pode
ler a free var.
Foram atribuídos diferentes valores de def fora() para variáveis,
e na sequência foram exibidas.

Uma função para concatenar strings foi criada, def concatenar(argumento)
e receberá um argumento, que foi atribuído a uma variável.

Dentro de def concatenar, foi criado def interna, que também recebe 
um argumento com valor padrão definido.
Def interna(valor_a_concatenar='') irá retornar a variável da def concatenar(), mas para que isso
não gere um erro, é necessário converter a free var in nonlocal, então,
em def interna(), será feito 'nonlocal valor_final'. 
A cada execução, valor_final += valor_a_concatenar, ou seja, a cada execução
de concatenar(), os valores str adicionados, serão concatenados e exibidos 
na função. 

Então atribuímos a função à uma variável e fizemos diversas 
execuções com valores diferentes, e por fim, atribuímos a função executada
à uma variável final para exibir todos os valores concatenados. 

'''

