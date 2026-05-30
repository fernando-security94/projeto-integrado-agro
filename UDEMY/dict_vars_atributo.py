# __dict__ e vars para atributo de instancias

class Pessoas:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoas.ano_atual - self.idade
    
p1 = Pessoas('Edna Cristina', 58)
p2 = Pessoas('Fábio Augusto', 32)

p1.__dict__['outra'] = 'coisa' # A exibição através de dict permite que os atributos sejam editáveis.
# p2.__dict__['nome'] = 'EITA'

print(p1.__dict__)  # Exibindo através de __dict__
print(vars(p1))     # Exibindo através de vars()

print(p2.__dict__)  # Ambos retornam dicionários
print(vars(p2))     # mas apenas __dict__ é editável

"""
A função de __dict__ e vars em classes, é basicamente poder exibir
todos os valores de uma só vez, sem a necessidade de executar a classe
até consumir todos os atributos. 

Tanto __dict__ quanto vars, retornam um dicionário, pois as classes, possuem 
o que seria equivalente a chave e valor, em dicionários.

Porém, a função __dict__ permite a edição das chaves e valores, e também,
é possível adicionar sem a necessidade de criar uma nova variável para a classe.



"""