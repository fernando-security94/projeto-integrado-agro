# @property + @setter - getter e setter em Python
# - como getter
# - evita quebrar código cliente
# - para habilitar setter
# - para executar ações ao obter um atributo

class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None
    
    @property
    def cor(self):
        # print('ESTOU NO GETTER:')
        return self._cor
    
    @cor.setter 
    def cor(self, valor):
        # print('ESTOU NO SETTER:')
        if valor == 'Rosa':
            raise ValueError('Cor não permitida')
        self._cor = valor

    @property
    def cor_tampa(self):
        # print('A cor da tampa é: ')
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
# caneta.cor = 'Rosa'  Uma vez que o erro é levantado, ó código quebra
caneta.cor = 'Vermelho'
print(caneta.cor)
print()

# Scaneta.cor = 'Azul'
print()
print(f'A cor final da caneta é {caneta.cor}.')

print()

caneta.cor_tampa = 'PRETA'
print(caneta.cor_tampa)
print()
print(f'A cor da caneta é {caneta.cor} e a tampa é {caneta.cor_tampa}.')
















'''
class Caneta:
    def __init__(self, cor):
        # private protected
        self._cor = cor  # atributo com under ou dunderline não deve ser usados fora da classe
    
    @property
    def cor(self):
        print('PROPERTY:')
        return self._cor  # isso será exibido ao executar o código
    
    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        print('ESTOU NO SETTER:', valor)
        self._cor = valor

    
caneta = Caneta('Verde')
caneta2 = Caneta('Vermelho')

caneta.cor = 'Rosa'
caneta2.cor = 'Amarelo'
print(caneta.cor)
print(caneta2.cor)
print()


caneta.cor = 'PRETO'
caneta2.cor = 'BRANCO'

# getter -> obter valor
print(caneta.cor)
print(caneta2.cor)

'''



'''
Aqui vemos a utilização de @property e @setter, no caso de Python,
o @property é um getter. 

Ambos são métodos que se comportam como instâncias com o objetivo
de executar determinadas ações. O @property busca o valor,
ja é o @setter, o define, e também, pode criar limitações e 
condicionais, como veremos nesse código.

Quando um desenvolvedor definir um atributo com under ou dunderline,
signfica que esse atributo NÃO DEVE ser usado FORA da classe, 
somente nas instâncias ou no molde.

A class Caneta foi criada, recebendo self, cor
O atributo self._cor = cor significa que é private protected,
ou seja, não pode ser usado fora da classe.

Depois, criamos uma @property def cor(self), que exibirá uma 
mensagem somente para se localizar durante a execução. E, irá
retornar self._cor, o mesmo atributo de __init__, pois é o que 
será exibido.

Depois, criamos @cor.setter, para um setter ser criado, é necessário
nomeá-lo antes. Dentro de @cor.setter, a def cor recebe self, valor.
Não há problema em repetir o nome das funções, desde que estejam
decoradas e protegidas por @property ou @setter.

Como o setter permite criar condições ou restringir certos valores,
uma condicional if foi criada para que if valor (que será a cor da caneta) == 'Rosa',
raise ValueError, ou seja, um erro de valor será levantado e quebrará o código.

Se tudo for de acordo as restrições de @cor.setter, uma mensagem será
exibida, da mesma forma em @property, somente para localização, e por fim,
vamos atribuir o valor a self._cor (mesmo atributo de __init__), então,
podemos entender que esses métodos serão executados em cascata, sendo,
a última chamada, o valor a ser exibido.

Como no código, chamamos a class Caneta e atribuímos a cor 'Azul', que será executado
pela @property.

Depois, atribuímos o valor 'Verde' diretamente a caneta.cor, que será
executada pelo setter, com as restrições, a cor da caneta, passa
a ser verde.

Criamos, também uma @property def cor_tampa(self), que irá get a cor da tampa da caneta,
para isso, return self._cor_tampa


E, por obrigação, @cor_tampa.setter, foi criada 
para definir a cor com def cor_tampa(self, valor).
A instância foi parecida com __init__, 
sendo self._cor_tampa = valor

Atribuímos a cor 'PRETA' através de caneta.cor_tampa = 'PRETA'

E, para praticar, exibimos a cor final da caneta e da tampa,
com fstrings:
print(f'A cor final da caneta é {caneta.cor} e a tampa é {caneta.cor_tampa})

'''