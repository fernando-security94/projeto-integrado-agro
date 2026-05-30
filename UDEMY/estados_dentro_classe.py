'''
Mantendo estados dentro da classe
'''

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando')
            return

        print(f'{self.nome} está filmando')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando')
            return
        
        print(f'{self.nome} está parando de filmar')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return
        
        print(f'{self.nome} está fotografando')






        



c1 = Camera('Canon')
c2 = Camera('Sony')


print(f'Modelo: {c1.nome}')
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()


print()

print(f'Modelo: {c2.nome}')
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()
c2.parar_filmar()


'''
Nesse código, temos diferentes estados dentro de uma única classe.
Esses estados, na verdade, são funções(novas instâncias) que 
executam certas ações.

Em primeiro lugar, definimos a class Camera. 
Por padrão de classe, recebera def __init__(self, nome, filmando=False)
Então temos dois parâmetros, sendo o segundo declarado como False por padrão,
pois de fato, ainda não esta filmando.
As instâncias self.nome e self.filmando foram criadas e será
através delas, que os próximos estados dentro do escopo da classe
terão acesso.

Agora, os estados(ações) serão criados.

O primeiro, serã a ação de filmar
Então a def filmar(self) foi criada, e a unica instância será self,
ela mesma.

Ao ser executada, o código print(self.nome), exibirá uma mensagem de que
está filmando. Detalhe que, só foi possível acessar o parâmetro nome
utilizando self. 

Caso fimar() seja executada novamente, a mensagem 'ja esta filmando' será exibida, 
pois criamos a condicional if self.filmando, ou seja, se self.filmando for True,
a mensagem será exibida, mais uma vez, com print(self.nome).

A seguir, precisamos fazer a camera parar de filmar.
Então def parar_filmar(self) foi criada. 

Quando executada, exibirá a mensagem dizendo que 'self.nome está
parando de filmar'

Seguindo o mesmo raciocínio de filmar, caso parar_filmar() for 
executada novamente, a mensagem 'self.nome não está filmando' será exibida
através de uma condicional if negativa, ou seja, if not self.filmando for True,
exiba a mensagem.

Por fim, criamos a ação de fotografar, com def fotografar(self)
Ao ser executada, a mensagem 'self.nome está fotografando', mas,
a camera não pode fotografar enquanto filma, então, criamos
a condicional if self.filmando() for True, e quando executada,
vai exibir a mensagem 'self.nome não pode fotografar filmando.'


Antes de executar todos estados, precisamos atribuir a classe 
à uma variável, então criamos c1 e c2, que recebe a
class Camera('Canon') e Camera('Sony') que são argumentos do
parâmetro nome.






'''
