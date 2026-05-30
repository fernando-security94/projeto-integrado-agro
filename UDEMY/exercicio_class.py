'''
Crie uma class Carro (nome)
Crie uma class Motor (nome)
Crie uma class Fabricante (Nome)

Faça uma ligação entre Carro e Motor 
OBS:
Um motor pode ser de vários carros
- Faça uma ligação entre Carro e Fabricante
Exiba o nome do carro, motor e fabricante

'''


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome


carro = Carro('Camaro')
fabricante = Fabricante('Chevrolet')
carro.fabricante = fabricante
print()
motor = Motor('v8')
carro.motor = motor
print(carro.nome, carro.fabricante.nome, carro.motor.nome)



print(f'Nome do carro: {carro.nome}')
print(f'Motor: {motor.nome}')
print(f'Fabricante: {fabricante.nome}')
print()

print(carro.nome)
print(carro.motor.nome)
print(carro.fabricante.nome)

print()

carro2 = Carro('Chronos')
fabricante2 =Fabricante('Fiat')
carro2.fabricante = fabricante2
motor2 = Motor('1.4')
carro2.motor = motor2
print(carro2.nome, carro2.fabricante.nome, carro2.motor.nome)

print()

print(f'Carro: {carro2.nome}')
print(f'Fabricante: {fabricante2.nome}')
print(f'Motor: {motor2.nome}')


'''
Nesse exercício tivemos que criar algumas classes e fazer com
que elas se relacionem entre si.

Primeiro, vamos criar cada classe.
A class Carro será a que irá possuir maior número de atributos, por
ser a base de todo o código, que vai servir de molde para as outras classes.

Class carro será inicializada com def __init__(self, nome), e após
atribuir self.nome = nome, vamos criar duas instâncias protected, sendo
self._motor = None e self._fabricante = None, pois serão atribuídas
depois que suas respectivas classes forem criadas. 

Class Motor foi criada e tbm será inicializada com def __init(self, nome), alias,
as três classes serão desse formato.
Atribuir instância self.nome = nome

Class Fabricante criada , inicializada com def __init__(self, nome),
e instância self.nome = nome atribuída.

Agora, dentro da class Carro, vamos fazer a ligação com as outras classes.

Vamos criar uma @property def motor(self) que irá return
self._motor(préviamente criada como instância na def __init__)
e um setter @fabricante.setter def motor(self, valor) que irá atribuir
self._motor = valor

Vamos aplicar a mesma coisa para o fabricante.
Então, @property def fabricante(self), irá return self._fabricante(préviamente
criada na instância def __init__), e na sequência, criar um setter fabricante.setter
def fabricante(self, valor) e será atribuido self._fabricante = valor


Agora, vamos executar os atributos, relacionar as classes entre si e exibir os v
valores

- Atribuir class Carro a uma variável e passar seu valor.
- Atribuir class Fabricante a uma variável e passar seu valor.
- Relacionar variável carro com a instância fabrincante e atribuir a variável
fabricante - caro.fabricante = fabricante, dessa forma vamos conseguir exibir
o nome do fabricante quando carro for chamado.
- Atribuir class Motor a uma variável
- Relacionar variável carro com instância motor e atribuir
a variável motor - carro.motor = motor
- Exibir o nome do carro com carro.nome, o fabricante com carro.fabricante.nome, e o motor
com carro.motor.nome

- Depois executamos novamente com fstr, mas sem a relação da class Carro, apenas para
exibir de forma mais organizada, dessa forma, foram chamadas como carro.nome, fabricante.nome
e motor.nome

- Criamos um novo carro, um novo fabricante e um novo motor, atribuindo novamente 
as respectivas classes à novas variáveis, porem, ao relacionarem entre si, mantivemos
os mesmos atributos - carro2.fabricante = fabricante2, carro2.motor = motor2




'''