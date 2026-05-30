'''
UML - Unified Modeling Language - Linguagem para fazer diagramas
e montagem de software.
- Relação entre classes: associação, agregação e composição
- Associação é um tipo de relação onde os objetos estão ligados 
dentro do sistema.
- Essa é a relação mais comum entre objetos e tem subconjuntos
como agregação e composição.
- Geralmente, temos uma associação quando um objeto tem um atributo
que referencia outro objeto.
- A associação não especifica como um objeto controla o
ciclo da vida de outro objeto.

'''
# Associação

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None  # protected

    @property
    def ferramenta(self):
         return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
         self._ferramenta = ferramenta


class FerramentaDeEscrever():
        def __init__(self, nome):
             self.nome = nome


        def escrever(self):
            return f'{self.nome} está escrevendo'
        
escritor = Escritor('Fernando')
escritor2 = FerramentaDeEscrever('Fernando')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_escrever  # associação de escritor com a property ferramenta que é get o valor de maquina_escrever
# escritor.ferramenta = caneta


print(escritor.nome)
print(caneta.nome)
print(maquina_escrever.nome)
print()
print(caneta.escrever())
print(escritor2.escrever())
print(caneta.escrever())
print(maquina_escrever.escrever())
print(caneta.escrever())        


'''
Entrando no assunto de relação entre classes, neste código,
teremos exemplos de associação. Ou seja, as classes irão relacionar-se
entre si.

Como será feito?

Criaremos duas classes. A primeira class Escritor receberá a 
instância __init__(self, nome), depois de atribuir self.nome = nome
vamos atribuir self._ferramenta = None, pois terá seu valor atribuído
através de uma @property.

Criaremos uma @property def ferramenta(self) que irá return um método protected
self._ferramenta (será usado em __init__). A property se comporta como um getter, ou seja,
pega um valor para o atributo

Na sequência, criaremos um setter @ferramenta.setter def ferramenta(self, ferramenta) e vamos 
atribuir o método protected self._ferramenta = ferramenta


Agora, vamos criar a segunda classe, que será class FerramentaDeEscrever,
com instância __init__(self, nome), self.nome = nome, que será
de fato, o nome de qual ferramenta de escrever será usada.

Essa class, receberá um método que executa a ação de escrever,
def escrever(self) e return fstring com uma mensagem: return f'{self.nome} mensagem.'

Feito isso, agora vamos, de fato, associar uma class com a outra.

Primeiro, vamos atribuir a class Escritor a uma variável e definir seu valor, no caso,
'Fernando'

Segundo, vamos atribuir a class FerramentaDeEscrever a uma variável, e também, definir seu valor,
que será 'Caneta Bic'

Terceiro, vamos atribuir class Ferramenta a uma variável, também, e criar seu valor,
que será 'Máquina'

Agora, nessa parte ocorre a associação entre Escritor e FerramentaDeEscrever, através de 
escritor.ferramenta(que é a property ou getter) = maquina_escrever(que é atribuída à class)

Vamos exibir essas três variáveis através de print('variável'.nome)

Por fim, vamos executar as variáveis com os atributos das classes: print('variavel'.nome)

E também, executar a ação de def escrever(): print('variavel'.escrever())


'''