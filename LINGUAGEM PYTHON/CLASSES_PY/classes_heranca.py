# Criação de classes e atributos

class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def saudacao(self):
        return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos'
    
    def aniversario(self):
        self.idade += 1

pessoa1 = Pessoa("João", 30, "Masculino")
print(f'Nome: {pessoa1.nome}.\nIdade: {pessoa1.idade}.\nGênero: {pessoa1.genero}\n')

# executa saudação
print(pessoa1.saudacao())

# executa aniversario
pessoa1.aniversario()
print(pessoa1.saudacao())

pessoa1.aniversario()
print(pessoa1.saudacao())


# heranças
class Animal:
    def __init__(self, nome):
        self.nome = nome
    def faz_barulho():
        pass

class Cachorro(Animal):
    def faz_barulho(self):
        return "está latindo."


class Gato(Animal):
    def faz_barulho(self):
        return "está miando."

toddy = Cachorro("Toddy")
mingau= Gato("Mingau")

print(f'Nome: {toddy.nome}.\nAção: {toddy.faz_barulho()}\n')
print(f'Nome: {mingau.nome}.\nAção: {mingau.faz_barulho()}\n')
print()

# exercicio de class Veiculo
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    # ação de acelerar
    def acelerar(self, incremento):
        self.velocidade += incremento
    
    # status do veiculo
    def status(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nVelocidade: {self.velocidade}'
    

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia
    
    def acelerar(self, incremento):
        self.velocidade += incremento + self.potencia

class Bike(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def status_bike(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nTipo: {self.tipo}\nVelocidade: {self.velocidade} km/h'

# criando objetos
carro1 = Carro("Toyota", "Corolla", 2022, 150)
bike1 = Bike("Trek", "Mountain Bike", 2021, "MTB")

# Acelerando e executando status
carro1.acelerar(100)
bike1.acelerar(20)

print(f'Status do carro:\n{carro1.status()}')
print(f'Status da bike:\n{bike1.status_bike()}')
