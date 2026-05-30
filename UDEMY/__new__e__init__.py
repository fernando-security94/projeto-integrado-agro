# __new__ e __init__  em classes em Python
# __new__ é o método responsavel por criar e
# retornar o novo objeto. Por isso, __new__ recebe cls;
# __new__ DEVE retornar o novo objeto
# __init__ é o responsável por inicializar
# a instância. Por isso __init__ recebe self.
# __init NÃO DEVE retornar nada (None)
# object é a super classe de uma classe - 

class A(object):  # Toda superclasse herda automaticamente de object
    def __new__(cls, *args, **kwargs):  # Não recebe self, pq é o new que criará o self
        print('Antes de criar a instância')
        instancia = super().__new__(cls)
        print('Depois de criar a instância')
        instancia.x = 123
        return instancia # forma correta de criar a instância da class   

#        return object.__new__(A)


    def __init__(self, x):
        self.x = x
        print('Sou o __init__')

    def __repr__(self):
        return 'Class A()'
    



a = A(4598)
 # ou
# a = object.__new__(A)  # Primeiro método chamado antes do __init__
# a.__init__()
print(a)
print(a.x)


"""
Dentro do assunto de special methods, um dos métodos
menos utilizados é o __new__, que é responsável por criar
e retornar o novo objeto. Ou seja, antes de inicializar uma class
com __init__, o __new__ é criado, e como o self só é criado depois de 
inicializar a class, __new__ recebe cls, ou seja, a própria class.

- Toda superclass herda automaticamente object, que está um patamar
mais alto dentre as classes. Portanto, object é a superclasse
de uma classe.

- Somente um código extremamente avançado e peculiar usaria __new__

- 99.99% dos casos usa-se exclusivamente __init_

Dissertando o código:

- Criar class A()- Não há a necessidade de explicitar a herança de 
object. 

- Criar o método new com def __new__(cls, *args, **kwargs). O método
recebeu dois parâmetros sendo args e kwargs para que ao inicializar a class,
não haver a preocupação de match o número de parâmetros da superclass.

- Vamos exibir uma mensagem para exibir antes de criar a instância.

- Vamos sobrescrever o método new com super().__new__(cls) atribuíndo
a uma variável.

- Exibir mensagem após a criação da instância.

- Qualquer objeto que seja adicionado em __new__, poderá ser acessado
em __init__, como no caso de instancia.x = 123

- Criar o método def __init(self, x) receberá self e o parâmetro 
adicionado após a criação da instância em def __new__

- Instanciar self.x = x (retornará 123)

- Vamos criar o método def __repr__(self) que retornará o nome
da class - 'class A'

- É importante ressaltar que esses métodos DEVEM estar no esboço
da superclass.

- Atribuir a class com seu argumento posicional a uma variável.

- Se o valor for diferente do que foi previamente escolhido, 
o último será salvo, quando o parâmetro x for chamado.

- Exibir variável a, que retornará o valor de def __repr__ = 'Class A()'

- Exibir variável a.x, que será o valor atribuído no momento da 
execução da class A('valor)




"""
