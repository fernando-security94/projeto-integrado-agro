'''
Composição é uma especialização da agregação.
Mas nela, quando todo objeto "pai" for apagado, todas
as referencias dos objetos filhos também serão apagadas.

'''

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    
    def __del__(self):
        print('APAGANDO', self.nome)

 

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

       # garbage collector - finalizador
    
    def __del__(self):
        print('APAGANDO', self.rua, self.numero)

cliente1 = Cliente('Maria')
print(cliente1.nome)
cliente1.inserir_endereco('Av Brasil', 53452)
cliente1.inserir_endereco('Rua B', 34)
endereco_externo = Endereco('Av Saudade', 314131)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()
print()


del cliente1  # As partes dependentes de cliente (rua e numero) também serão apagadas.

print(endereco_externo.rua, endereco_externo.numero)


print('#### AQUI TERMINA MEU CÓDIGO ####')
print()

'''
Nesse código, vamos exemplificar a composição, que é definida quando os 
objetos são interdependentes, e quando o objeto primário for alterado ou apagado,
os demais também serão apagados.

Aqui temos duas classes.

A primeira class Cliente será inicializada com self, nome. Depois
de atribuir self.nome = nome, vamos atribuir uma lista vazia, onde os clientes e endereços serão adicionados,
com self.enderecos = []

Vamos criar o método def inserir_endereços(self, rua, numero), vamos atribuir a class Endereco que 
ainda não foi criada, com rua e numero através de
self.enderecos.append(Endereco(rua, numero)) - Isso é composição, pois estamos
tornando a class Endereco dependente da Class Cliente.

Vamos criar o método def listar_enderecos(self) através de um laço for
sendo for endereco in self.enderecos - serão adicionados de 
forma iterada a lista vazia previamente criada.

Agora, vamos criar a class Endereco(self, rua, numero), que ja foi previamente adicionada em composição 
na class Cliente. Após atribuir as instancias self.rua = rua e 
self.numero = numero

Vamos atribuir a Class Cliente a uma variável e passar seu valor,
cliente1 = Cliente('Maria')

Agora, com essa mesma variável, vamos executar o método def inserir_endereço, com
cliente1.inserir_endereco(valor), e vamos adicionar mais de um
endereço para o mesmo cliente.

Por fim, vamos listar os endereços através de cliente.listar_enderecos()

E ao término de todas as execuções, exibir uma mensagem de finalização

Agora, como adicionais, fizemos alguns testes com o garbage collector, que
nada mais é do que a função del, que literalmente, recolhe objeto por
objeto ao término das execuções.

Criamos def __del__(self), exibindo uma mensagem e, quando na 
class Cliente, vai apagar self.nome, e, quando na 
class Endereco, vai apagar self.rua, self.numero.

Caso a função del seja chamada antes do término, fora das classes, ainda teríamos
espaço e tempo de exibir um endereço externo, que foi criado em class Cliente
através de def inserir_endereco_externo(self, endereco) com a 
função append, self.enderecos.append(endereco)

Executamos esse método atribuindo a class Endereco a uma nova variável, passando seu valor,
e depois, associando-a com a variável cliente 1 e 
executando o metodo def inserir_endereco_externo, passando 
endereco_externo em sua execução:

endereco_externo = Endereco(nome da rua, numero)
cliente1.inserir_endereco_externo(endereco_externo)




'''