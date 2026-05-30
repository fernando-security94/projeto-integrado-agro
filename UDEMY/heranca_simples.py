'''
# Herança simples - Relações entre classes
# Associação - objeto usa outro objeto
# Agregação - objeto tem outro objeto
# Composição - É dono de outros objetos
# Herança - Objeto é o objeto e também outro tipo de objeto

# Herança ou Composição

# Classe principal (Pessoa)
# super class, base class, parent class
# Class filhas (Cliente)
# Sub class, child class, derived class


'''

# Herança Simples - Relações entre classes

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_class(self):
        print('Buscando na classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_class(self):
        print('Buscando na classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)
    


class Aluno(Pessoa):
    cpf = 'cpf aluno'
    


p1 = Pessoa('Felipe', 'Ribeiro')
p1.falar_nome_class()
print(p1.nome, p1.sobrenome)
print()

c1 = Cliente('Fernando', 'Ribeiro')
c1.falar_nome_class()
print(c1.nome, c1.sobrenome)
print()


a1 = Aluno('Edna', 'Giovanini')
a1.falar_nome_class()
print(a1.nome, a1.sobrenome)
print(a1.cpf)

# help(Cliente)


# tudo o que estiver buscando em um objeto, seguirá a ordem de method resolution order

'''
Neste código, vamos exibir exemplos de herança simples, que é, na verdade,
relação entre classes, onde, basicamente, uma classe recebe a outra como "parâmetro".

- Criar class Pessoa, essa class terá uma variável cpf = '1234', 
sómente para ilustrar que se tiverem duas variáveis (teremos 
uma variável 'cpf' na class Aluno) com o mesmo nome,
o último valor será salvo

Vamos inicializar a class Pessoa com def __init__(self, nome, sobrenome),
e atribuir as instâncias self.nome = nome, self.sobrenome = sobrenome

Vamos criar um método que executa uma ação, def falar_nome_class(self),
que exibirá uma mensagem 'Buscando na classe Pessoa', por de fato, estar dentro do
molde da class Pessoa. Vamos chamar uma função que exibe o nome da class 
em que está sendo executada. Então, será:
print(self.nome, self.sobrenome, self.__class__.__name__)

Agora, vamos criar a class Cliente, que RECEBE a class Pessoa, ou seja, tudo o que
estiver na class Pessoa, será herdado pela class Cliente, da seguinte forma:
class Cliente(Pessoa):
E receberá o mesmo método def falar_nome_class(self), exibirá uma mensagem parecida com
a anterior de 'Buscando na class Cliente', e chamará a função self.__class__.__name__

Agora, criar class Aluno(Pessoa) que receberá como "parâmetro", a class Pessoa, 
da mesma forma com a class Cliente, que herdará tudo o que tem na super class. 
Em class Aluno vamos apenas atribuir a variável cpf um novo valor. Apesar de 
estar em outra class, por terem o mesmo nome, o último valor será salvo.

Vamos às execuções:
- Atribuir class Pessoa a uma variável e criar seus valores.
- Executar o método que exibe o nome da class com p1.falar_nome_class()
- Exibir p1.nome, p1.sobrenome

- Atribuir class Cliente a uma variável e criar seus valores.
- Executar c1.falar_nome_class()
- Exibir c1.nome, c1.sobrenome

- Atribuir a class Aluno a uma variável e criar seus valores
- Executar o método c1.falar_nome_class()
- Exibir a1.nome, a1.sobrenome
- Exibir a1.cpf (último valor agregado será exibido)



'''