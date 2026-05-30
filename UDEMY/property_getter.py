'''
- @property - um getter no modo Pytonico
- um método para obter um atributo

- @property é uma propriedade do objeto, sendo um método
que se comporta como um atributo =O

- Geralmente é usada nas seguintes situações:
- como getter
- para evitar quebra do código cliente
- Código cliente é o código que usa o seu código
- para habilitar setter
- para executar ações ao obter o atributo

'''
# @property - Método que se comporta como atributo

class Caneta:
    def __init__(self, cor_tinta):
        self.cor_tinta = cor_tinta

    @property  # Também está servindo como getter Pythonico
    def cor(self):
        print('A cor da caneta é: ')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return f'A cor da tampa é {self.cor_tinta}'
    
caneta = Caneta('Azul')
caneta2 = Caneta('Verde')
print(caneta.cor)
print(caneta.cor_tampa)
print()
print(caneta2.cor)
print(caneta2.cor_tampa)















############################################
# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor  

#     def get_cor(self):
#         print('GET COR:')  
#         return self.cor


# ####################################
        
# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())

'''
O @property é um método que se comporta como um atributo. Ou seja
é uma def decorada que pode executar uma ação, sem quebrar o código 
que está protegido, então, caso haja alguma alteração no código, para que 
nao haja a necessidade de alterar em todas as linhas em questão (que podem ser milhões),
é só alterar na def decorada por @property, que se comporta como
um getter.

Aqui temos uma class Caneta que recebe self, cor
Criamos, inicialmente, self.cor = cor e atribuimos a cor, com
a class Caneta executada: caneta = Caneta('Azul'), e exibimos
através de print(caneta.cor), resultado = Azul.

Depois, por alguma razão, o nome de self.cor foi alterado para self.cor_tinta.
E agora?
Para que não quebre o código ou perca tempo alterando todas as 
linhas necessárias, uma @property foi criada para proteger a instância, e 
se comportar como getter. 

Dessa forma, criamos:
@property
def cor(self):  @propety tem acesso ao self
return self.cor_tinta(nome alterado)

Dessa forma, esse getter pythonico vai fazer com que o código volte a funcionar.
Por que?
@property recebe def cor(self), certo? Só que, return self.cor_tinta, 
e como 'Azul' foi o valor atribuído a classe Caneta na primeira variável,
seria a mesma coisa que executar a instância, se não houvesse
alteração.

E por fim foi criada mais uma property para definir a cor da tampa da caneta, que
geralmente, será a mesma cor da tinta da caneta. 
Então, criamos:
@property
def cor_tampa(self)
    return f' A cor da tampa é {self.cor_tinta}


'''