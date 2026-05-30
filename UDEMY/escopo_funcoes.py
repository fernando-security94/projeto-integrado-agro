"""
Escopo de funções em Python
Escopo significa o local onde determinado código pode atingir
Existe escopo local e global
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas os nomes do mesmo local 
podem ser alcançados

"""

x = 1

def escopo():
    x = 10
    y = 20
    def outra_funcao():
        x = 20
        y = 2
        print(x, y)
    
    outra_funcao() # Essa função só pode ser executada se for chamada dentro de seu escopo local.
    print(x, y)

# print(x)
escopo()
print(x)  # Variavel do lado de fora do escopo da def escopo()


'''
Sobre os escopos dessas funções, podemos dissertar:
A variável x que está do lado de fora do escopo será imutável, mesmo após ter outras variáveis com o mesmo nome
porém, dentro dos escopos das funções seguintes. Ou seja, as variáveis dos escopos, são protegidas e imutáveis, exceto
quando forem declaradas como "global", dentro do escopo:
x = 1
def escopo():
    global x = 10
Nesse caso, a variável x dentro de escopo() terá um novo valor. E a mesma pode ser mudada novamente em outro escopo interno
desde que declarad global:
x = 1
def escopo():
    global x = 10
    def outro_escopo():
        global x = 20 
    outro_escopo()
    print(x)
escopo()

A variável x era 1, passou a ser 10 dentro de escopo() e passou a ser 20 dentro de outro_escopo(). Se não fosse "global"
cada x teria um valor diferente, protegido pela sua própria função. O mesmo vale para a variável y.
Variáveis não globais, são protegidas por seus escopos. Se uma função dentro de outra função não tiver nenhuma variável 
declarada, é possível acessar a variável de um escopo externo, mas não funciona ao contrário.      


As funções que forem executadas, serão exibidas em ordem reversa, ou seja, de escopos internos para escopos externos.
Nesse caso a função outro_escopo() será executada e exibida primeiro, seguida de escopo().

Esse fenômento é chamado de Call Stack, que significa criação de novos lugares na memória para que as funções sejam "empilhadas"
em sequência para serem executadas, as primeiras funções criadas serão as primeiras a entrarem no Call Stack,
porém, serão as últimas a serem exibidas. Usando as funções acima, podemos dizer que, quando o programa é executado
ao chegar em escopo() e sua variável for definida, o interpretador vai criar um call stack para pausar a função escopo(),
pois existe uma outra função dentro dela, que é outro_escopo, que será "empilhada", e executada na ordem. 

'''