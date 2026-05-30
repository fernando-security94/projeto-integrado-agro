'''
- Herança Múltipla - Python orientado a objetos
- Quer dizer que no Python, uma classe pode estender
várias outras classes.
- Animal -> Mamifero -> Humano -> Pessoa -> Cliente
- Herança múltipla e mixins
- Log ->FileLog
- Animal -> Mamifero -> Humano -> Pessoa -> Cliente
- Clientw(Pessoa, FileLog)

- A, B, C , D
D(B, C) - C(A) - B(A) - A

-       A
#     /   \
     B     C
      \   /
        D

        
- Python 3 usa C3 superclass linearization para
gerar method resolution order (mro)
- https://en.wikipedia.org/wiki/C3_linearization

- Para saber a ordem de chamada dos métodos:
- Use o método de classe Class.mro()
- Ou o atributo __mro__ através de Class.__mro__


        
'''

class A:
    ...

    def quem_sou(self):
        print('A')

    
class B(A):
    ...

    def quem_sou(self):
        print('B')

class C(A):
    ...

    def quem_sou(self):
        print('C')

class D(B, C):
    ...

    def quem_sou(self):
        print('D')


d = D()
c = C()
b = B()
a = A()

d.quem_sou()
c.quem_sou()
b.quem_sou()
a.quem_sou() 

print(D.mro())
print(C.mro())
print(B.mro())
print(A.mro())




'''
Aqui vemos um exemplo básico e objetivo de herança múltipla
Nesse caso, temos quatro classes, sendo:
- Class A
- Class B(A) - Recebe class A de herança
- Class C (A) - Recebe class A de herança
- Class D (B, C) - Recebe class B e class C de herança


Percebe-se que as class B, C e D recebem outras classes de herança.
Aqui temos o efeito diamante(desenhado anteriormente). Se a herança múltipla da Class D
fosse o contrário, o mro (method resolution order) seria diferente.

Em relação a herança múltipla:
- Tudo o que estiver presente em class A, estará presente em class B e class C.
- Tudo o que estiver presente em class B e class C, estará presente em class D.
- A class D irá possuir tudo o que estiver  não somente na class B, class C, mas 
também, na class A, pois será passada de herança durante o efeito diamante.

Criamos uma def quem_sou(self) em cada class, e exibirá um valor correspondente à sua class.

- Vamos atribuir a class D() a uma variável, sem passar nenhum valor.
- Vamos atribuir a class B() a uma variável, sem passar nenhum valor.
- Vamos atribuir a class C() a uma variável, sem passar nenhum valor.
- Vamos atribuir a class A() a uma variável, sem passar nenhum valor.

'''