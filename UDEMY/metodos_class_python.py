'''
Métodos em instâncias de classes Python

Hard Coded - Algo que foi escrito diretamente, como por exemplo:
self.nome = 'Fusca'

- Uma classe pode gerar varias instancias
- Na classe, o self é a própria instância, sendo obrigatório iniciar com self.

'''

class Carro:
    def __init__(self, nome_carro= 'Sem modelo'):  # método __init__ sempre retorna None
        self.nome = nome_carro
        # self.nome2 =  alguma_coisa

    def acelerar(self):
        print(f'{self.nome} está acelerando...')
    
fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
# print(fusca.acelerar())  # Dessa forma irá retornar um None após executar a função acelerar()
Carro.acelerar(fusca)  # Mudando o self dentro da classe, mas obtendo o mesmo resultado

print()

celta = Carro(nome_carro='Celta')
print(celta.nome)
celta.acelerar()


'''
Nesse exemplo, estamos vendo diferentes métodos dentro das classes.
Métodos em classes, são na verdade, funções que executam alguma ação.

A class Carro foi criada, e automaticamente recebe self. Recebeu, também,
um parâmetro com valor padrão, para em caso de nao receber nenhum argumento,
seja posicional ou nomeado, receberá esse valor pré-definido.

A instância self.nome foi criada e recebe o argumento nome_carro.

Dentro dessa classe, foi criada função acelerar() que também deve receber
self como primeiro parâmetro, para poder ter acesso a class.
E exibirá uma mensagem de que self.nome está executando uma ação.

Vamos atribuir a class Carro a uma variável, e nesse caso, a class
receberá um argumento posicional 'Fusca' e será exibido através
de print(fusca.nome) - instância criada na class. Para executar a 
ação de acelerar(), será através de fusca.acelerar(), nesse caso,
não foi necessário chamar print() porque será executada dentro da
função acelerar()

Depois, a mesma class Carro foi atribuída a uma outra variável,
e a class também pode receber argumento nomeado, como 
nome_carro= 'Celta', e será exibido com print(celta.nome)
E a função acelerar também será executada.

Resultado:
Fusca
Fusca está acelerando...

Celta
Celta está acelerando...



'''


