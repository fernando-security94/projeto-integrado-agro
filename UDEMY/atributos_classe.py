# Atributos de classe


class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
#        self.ano_atual = 100
        return 
        

    def get_ano_nascimento(self):
#        return self.ano_atual - self.idade  # Usar self pode causar um problema, por ter um atributo com mesmo nome. 
        return Pessoa.ano_atual - self.idade  # Portanto, pode-se usar o nome da class ao invés de self.
    
p1 = Pessoa('Fernando', 30)
p2 = Pessoa('Poliane', 42)


print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print(p1.__dict__)  # Exibe todos os atributos da instância em dict

"""
Nesse breve código foi mostrado como um simples atributo com 
o mesmo nome de uma variável ou constante, pode mudar o andamento
do código.

A class Pessoa foi criada e recebe self, nome, idade.
Uma variável ano_atual foi colocada dentro da classe. Poderia
ser uma constante fora da classe, também.

Uma def get_ano_nascimento foi criada para encontrar o ano
de nascimento do atributo nome, baseado no atributo idade e 
na variável ano_atual.

Agora, um outro atributo também com nome ano_atual(self.ano_atual) com valor x,
foi criado propositalmente para causar essa divergencia.

O erro seria causado na def get_ano_nascimento quando 
return self.ano_atual - self.idade, porque o valor foi aleatório,
e mesmo se fosse algo proximo de ano_atual, ainda assim, o resultado
seria incorreto.

Portanto, nesse caso, para que a VARIÁVEL seja usada e não o
ATRIBUTO, será com return Pessoa.ano_atual - self.idade

Então, dessa forma estamos garantindo que a variável da classe
está sendo utilizada, e não self.ano_atual

Ao fim, criamos duas variáveis que recebem nome e idade, respectivamente.

Depois, exibimos Pessoa.ano_atual, as variáveis p1 e p2 executando
def get_ano_nascimento()






"""