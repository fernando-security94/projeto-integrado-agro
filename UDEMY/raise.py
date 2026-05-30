"""
raise - lançando exceções (erros)


"""

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Voce tentou dividir por zero')
    return True

def deve_int_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'{n} deve ser int ou float. '
            f'{tipo_n} enviado!'
        )
    return True
    

def divide(n, d):
    deve_int_float(n)
    deve_int_float(d)
    nao_aceito_zero(d)

    return n/ d

print(divide('8', 0))

"""
A função raise é utilizada para levantar erros nos quais,
em determinadas situações, não tem o que fazer ou como 
controle do que possa estar errado no código de forma legível
e organizada.

Nesse caso, temos uma função que faz divisões matemáticas.
def divide recebe dois argumentos, numero(n) e divisor(d).

Nós queremos garantir que essa função nao aceite divisões
por zero e que receba apenas int ou float. 

Então uma função def para isso foi criada: def deve_int_float(n)
e receberá apenas um argumento, e futuramente será chamada duas vezes.

Nessa função, vamos checar a instância de n e d através de uma
condicional if not isinstance(n,(float, int)) e se for verdadeira
raise TypeError será chamada. Esse raise pode ter fstrings
exibindo uma mensagem de acordo a necessidade.

Para que a def deve_int_float funcione, ela precisa ser executada
dentro da def divide(), uma vez para n e uma vez para d:
deve_int_float(n)
deve_int_float(d)

Para que divisões por zero nao sejam aceitas, a função 
def nao_aceito_zero receberá um argumento que
será divisor(d), foi a mais simples de ser criada.
def nao_aceito_zero terá uma condicional if d == 0
raise ZeroDvisionError será ativada e uma mensagem será exibida.

Tanto def deve_int_float() quanto def nao_aceito_zero() 
return True no final, pois ou a função retorna true no final, 
ou retorna um erro.





"""