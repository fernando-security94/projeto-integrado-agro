# Escopo da classe e de metodos da classe


class Animal:

    def __init__(self, nome):
        self.nome = nome
        
    
    def comendo(self, alimento='carne'):  # parâmetro com valor padrão
        return f'O {self.nome} esta comendo {alimento}'
    
leao = Animal('leão')
print(leao.nome)
print(leao.comendo())  # Recerá o valor padrão
print(leao.comendo('frango'))  # argumento posicional
# ou
print(leao.comendo(alimento='peixe'))  # argumento nomeado


'''
As classes, assim como laços for, condicionais if e funções def 
possuem seu escopo próprio. 

Nesse caso, dentro da class Animal, temos duas instâncias, 
sendo a segunda instância, uma função def que executa uma ação.

Normalmente, a def comendo() não teria acesso ao escopo de 
def __init__(), porém, ao utilizar self como primeiro parâmetro,
essa def passa a ter acesso a instância self.nome, para que possa
return uma mensagem após a def comendo() ser executada.

Ao executar a def comendo(), por ter acesso ao escopo com self, 
toda a classe será executada.

É importante dizer que a def comendo() recebeu um parâmetro com valor padrão
ou seja, quando for executada com print(leao.comendo()), por não
ter sido passado nenhum argumento, o valor padrão exibido será 
'carne', evitando assim, futuros erros. É permitido também, na hora 
da execução, passar argumento posicional como leao.comendo('frango') ou nomeado
leao.comendo(alimento= 'peixe')


'''