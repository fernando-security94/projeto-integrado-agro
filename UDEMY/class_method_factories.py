# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja, 
# ao invés de receber a instância no primeiro parâmetro,
# receberemos a própria classe.

class Pessoa:
    ano = 2023  # atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod   # decorator que permite chamar a classe sem passar self
    def metodo_de_classe(cls):  # mas é obrigatório passar cls como parâmetro, ou seja, a própria classe.
        print('Hey')


    @classmethod
    def criar_com_50_anos(cls, nome):  # factory method - método que cria outro objeto
        return cls(nome,50)  # return cls é o mesmo que retornar a class Pessoa

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

p1 = Pessoa('Jõao', 34)
p1.metodo_de_classe()
print(p1.nome, p1.idade, sep=', ')
Pessoa.metodo_de_classe()

print()

p2 = Pessoa.criar_com_50_anos('Edna')
print(p2.nome, p2.idade, sep=', ')

p3 = Pessoa.criar_sem_nome(30)
print(p3.nome, p3.idade, sep=', ')


"""
Class method e factories são duas formas, dentro das classes, de chamar
a classe sem self e permite criar novos objetos na classe, 
respectivamente.

Criamos uma class Pessoa que recebe 2 instâncias, nome e idade. Possui, também, um
atributo ano = 2023, que poderia ser uma constante.

Após a obrigatoriedade de def __init(self), e atribuição das instâncias,
vamos criar uma def metodo_de_classe() que exibe uma mensagem.

Para isso, é necessário decorar essa def, antes. Então, através de
@classmethod, que é um decorator, a def, desde que dentro do escopo
de @classmethod, já está decorada, e pode ser executada através de 
Pessoa.metodo_de_classe(), ou seja, sem passar argumentos.
Mas, é obrigatório o uso de "cls" dentro da def, que é de fato,
a própria classe.

No proximo passo, vamos criar uma factory, que de fato é uma fábrica
de criar novos objetos serão chamados quando a classe for executada.

Parar criar uma factory, também usa-se o decorator @classmethod, 
porém, além de passar o cls, é necessário passar parâmetros e 
return cls com esses parâmetros, como feito em :
@classmethod
def criar_com_50_anos(cls, nome)
    return cls(nome, 50)

Esse objeto, cria pessoas com idade padrão de 50 anos, e o nome, será
passado como argumento posicional no momento em que for executada.

Mas, como a idade será atribuída, no momento de:
p2 = Pessoa.criar_com_50_anos('Edna)
print(p2.nome, p2.idade, sep=', ')

Ao return cls(nome, 50) o valor da idade foi atribuído como um
argumento posicional da classe, pois mesmo que esse objeto não tenha
acesso ao self, ele está dentro do molde da classe, então,
o Python entende, que o segundo parâmetro do objeto, seja o mesmo
que self.idade

Depois, parecido com a def de criar com 50 anos, criamos uma 
def criar_sem_nome(cls, idade)
e irá return cls('Anônima', idade), ou seja, o contrário da def
anterior, o primeiro parâmetro tem valor padrão de 'Anônima',
e o segundo será atribuído no momento da execução como argumento
posicional:

p3 = Pessoa.criar_sem_nome(30)






"""