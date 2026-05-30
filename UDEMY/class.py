'''
Class - Classes são moldes para criar novos objetos

- As classes podem gerar novos objetos (instancias) que 
podem ter seus próprios atributos e métodos. 

Os objetos gerados pela classe podem usar seus dados internos
para realizar várias ações. 

Por convenção, usamos PascalCase para nomes de classes. Primeira letra sempre maiúscula - Tipo  ClassObject

'''

# Criando uma classe

# class Pessoa:
#     def __init__(self, nome, sobrenome):
#         ...



# p1 = Pessoa()  # gera uma nova instancia da classe Pessoa
# p1.nome = 'Fernando'  # atribuito de p1 = Pessoa()
# p1.sobrenome = 'Ribeiro'

# p2 = Pessoa()  # atributo de p2 = Pessoa()
# p2.nome = 'Poliane'
# p2.sobrenome = 'Novaes'

# print(p1.nome)
# print(p1.sobrenome)
# print()
# print(p2.nome)
# print(p2.sobrenome)


'''
Sempre que eu atribuir uma Classe() a uma variável, estou criando uma nova instância
e essa instância receberá atributos diferentes.

Como em class Pessoa() que foi atribuída a p1 e p2.
Ambos p1 e p2 recebem dois atributos com valores diferentes.


'''

# Introdução ao método __init__ - Inicializador de atributos

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Fernando', 'Ribeiro')
p2 = Pessoa('Poliane', 'Novaes')

print(p1.nome)
print(p1.sobrenome)

print()

print(p2.nome)
print(p2.sobrenome)


'''
Aqui vemos duas formas de criar classes em Python.
A primeira forma sem o método __init__(self) e a segunda com.

Ao criar uma classe, é importante manter sempre a primeira letra
maiúscula. Então nesse caso, foi criado class Pessoa, e depois
um place holder, ja que nao usaremos __init__

Para gerar uma nova instância da class Pessoa, é necessário
que seja atribuída a uma variável. Após gerar a instância,
é necessário criar os atributos, que são como argumentos em funções.

Nesse formato, foi criado com p1.nome= atributo 1 e 
p1.sobrenome= atributo 2, sendo p1 a variável na qual a class Pessoa
foi atribuída, já nome e sobrenome, são os novos atributos da classe.

O mesmo processo para a variável p2.

Ambas foram exibidas.

A segunda forma, utilizando __init__(self) é mais automatizada
por utilizar funções já determinadas pelo Python.

Ao criar a class Pessoa, é necessário criar uma função def 
que vai receber o método __init(self, atributos). Ou seja,
o método __init__ vai inicializar a função e receber seus atributos
de forma automática.

Porém, o primeiro "argumento" a ser passado, SEMPRE vai ser self, ou seja, 
é reservado para a própria classe, em questão, que no caso é Pessoa.

Então, para que os atributos que serão agregados a variáveis futuramente
recebam os respectivos valores, vamos usar self.atributo1 = atributo1
e self.atributo2 = atributo2  

Com isso, não há a necessidade de primeiro atribuir a classe Pessoa
a uma variável e depois criar seus atributos.
Isso ja foi feito com __init__ e depois self.

As variáveis irão receber a classe Pessoa, com seus atributos
já passados. 

p1 = Pessoa('Fernando', 'Ribeiro)
p2 = Pessoa('Poliane', 'Novaes)

Então aqui temos a class Pessoa e seus atributos p1 e p2,
recebendo nome e sobrenome com argumentos posicionais, respectivamente, como foi declarado
na def __init__



'''