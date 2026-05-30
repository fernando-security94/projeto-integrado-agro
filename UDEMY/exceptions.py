# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só precisa
# herdar de alguma exceção da linguagem.
# A recomendação da doc é de herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exeções (comum colocar Error no final)
# Levantando (raise) / lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)


class AnyError(Exception):  # Herdar de Exception para criar exceções
    ...


def try_error():
    exception_ = AnyError('This is my error', 'a', 'b', 'c')
    exception_.add_note('First note')
    exception_.add_note('Take a look at this error')
    raise exception_
    

class AnotherError(Exception):
    ...


try:
    try_error()
except (AnyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = AnotherError('Throwing error again')
    exception_.add_note('Second note')
    exception_.add_note('Take a look at this another error')
    exception_.__notes__ += error.__notes__.copy()  # copia as notas do error
    raise exception_ from error

'''
Criando exceções em Python
Nesse código vamos ver como levantar as próprias exceções, caso queira deixar avisado
que algum erro possa ocorrer quando algumas condições sejam verdadeiras.

Para criar qualquer exceção, em primeiro lugar, precisamos SEMPRE herdar de Exception. Sabendo disso, vamos ao 
passo a passo do código.

- Criar class AnyError(Exception) - A class deve sempre herdar de Exception
- Nessa class, como será apenas para levantar uma exceção, não terá
corpo, então podemos usar pass(...). As exceções será testadas
atravpes de def e try/except

- Criar def try_error()

- Atribuir class Anyerror a uma variável exception_.

- Podemos passar mais de uma informação dentro da exceção, 
como nesse caso, exception_ = AnyError('mais alguma informação')

- Usamos o _ no final da variável para não causar confusão se alguma
palavra estiver reservada para uso da linguagem.

- Raise a variável exception_

- Criar class AnotherError(Exception) e também pass...

- Dentro de um laço Try/except, vamos tratar e relançar as exceções:

- Try a def any_error()

- No except relançar as exeções AnyError e adicionar uma
exceção ja existente, ZeroDivisionError as error.

- Vamos exibir error.__class.__name__ para saber de qual
class vem o erro e qual o nome do erro.

- Exibir error.args- Quando se trata mais de uma exceção,
automaticamente as informações serão exibidas em args (tuple)

- Pular uma linha

- Atribuir a class AnotherError('mais informação')

- Vamos raise novamente a variável exception_ from error,
que era o erro anterior, mas que agora, está atribuída a class AnotherError.

Antes de passarmos para a parte de adicionar notas nas exceções,
é importante de dizer, que a primeira execeção, criada
em class Anyerror é a causa direta das exceções subsequentes, ou seje,
as exceções que foram criadas depois não aconteceriam sem a primeira.

- É possível adicionar notas nas exceçõe, que podem ser usadas
como para que outros desenvolvedores entendam onde está o erro 
e qual causa, etc.

- Selecionar o lugar onde quer adicionar a nota

- Na def try_error, logo após atribuir a class AnyError a uma variável
vamos escrever variável.add_note('escrever a nota')

- Então: exception_.add_note('First note')

- O mesmo serve para mais de uma nota, só adicionar na ordem 
desejada.

- Adicionar add_note depois de exception_ = AnotherError('mensagem')




'''