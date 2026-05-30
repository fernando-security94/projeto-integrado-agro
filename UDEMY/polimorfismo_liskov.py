# Polimorfismo em Python Orientado a objetos
# Polimorfismo é o princípio que permite que
# classes derivadas de uma mesma superclasse
# tenham métodos iguais (com a mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método: Mesmo nome e quatidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload) Python não suporta
# Sobreposição de métodos (override) Python suporta



from abc import ABC, abstractmethod
 
class Notificacao(ABC):
    def __init__(self, mensagem) -> None:  # None por padrão
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool:...  # -> significa um aviso que precisa retornar bool



class NotificacaoEmail(Notificacao):

    def enviar(self) -> bool:
        print('Enviando notificação por e-mail: ',"\n", self.mensagem)
        return True  # caso contrário, irá contra Liskov Substitution Principle
                     # pois a assinatura do método foi feita para retorno bool



class NotificacaoSMS(Notificacao):
    
    def enviar(self) -> bool:
        print('Enviando notificação por SMS:', "\n", self.mensagem)
        return  # Irá retornar false pois por natureza, uma def sempre return None
                # portanto, irá quebrar o Liskov Substitution Principle, pois a assinatura
                # do método foi feita para retorno bool, e, uma vez assinado, deve-se seguir 
                # o mesmo padrão.
                



def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação não enviada')


    






n = NotificacaoEmail('Você tem 10 e-mails não lidos')
n.enviar()
print()
n = NotificacaoSMS('Você tem 10 mensagens não lidas')
n.enviar()
print()

notificacao_email = NotificacaoEmail('Testando e-mail')
notificar(notificacao_email)

print()

notificacao_sms = NotificacaoSMS('Testando SMS')
notificar(notificacao_sms)



'''
Polimorfismo utilizando Liskov Substitution Principle

Nessa primeira aula de polimorfismo, teremos duas classes, 
sendo a primeira, uma superclasse e a segunda, sua subclasse.

Antes de tudo, precisamos importar o método abstrato:
from abc import ABC, abstractmethod

- Criar a classe Notificação(ABC) que receberá o metodo ABC como herança.
Essa notificação, será especificada em algum tipo de notificação(por email e sms) futuramente.

- Inicializar a superclasse com def __init__(self, mensagem) e instanciar seu atributo:
self.mensagem = mensagem

- Criar um método abstrato def enviar que terá como assinatura um retorno bool.
Por ser abstrato, esse método não terá corpo e será sobrescrito na subclasse


- Criar uma class NotificacaoEmail(Notificacao) que receberá
a class Notificacao como herança. Então, tudo o que tiver na 
superclass, estará presente na subclass.

- Chamar a def enviar(self), mantendo sua assinatura de bool, só deixou de 
ser abstrata, porque agora, de fato, terá corpo e executará uma ação.

- Exibir mensagem de envio de notificação por email e return True, precisa 
ser explicito, pois def retorna None por padrão. Dessa forma,
o Liskov Substitution Principle será mantido.

- Criar class NotificacaoSMS(Notificacao) que também herdará 
a superclass Notificacao.

- Utilizar a mesma def enviar que foi chamada na subclass NotificacaoEmail
- Exibir a mesma mensagem de envio de notificação, voltada para sms.
Vale ressaltar, que ao executar print('Enviando notificacao por...') depois da quebra
de linha, é chamado self.mensagem, que é o parâmetro a ser passado 
no momento da atribuição e execução da class em uma variável.
- No return, não colocamos nada, sendo assim, a def retornará
None por padrão, indo contra a assinatura do método, causando uma quebra no programa 
quando a condicional if for criada para checar se a notificação
foi enviada.


- Aqui ocorre o polimorfismo, pois uma mesma notificação, se comporta
de duas formas diferentes, seja para email e/ou sms.

- Ao criar a def notificar(notificacao: Notificacao) o 
parametro notificacao recebe a class Notificacao como assinatura. Ou seja,
essa def precisa se comportar como uma Notificação, só que sem 
a necessidade de ter sido especificada, e no momento das atribuições,
independentemente de qual class for atribuída, def notificar(notificacao: Notificacao) irá
funcionar normalmente

- Vamos executar a def enviar() no parâmetro notificacao : notificacao.enviar()
e atribuí-lo a uma variável notificacao_enviada.

- Condicional if criada para checar se notificacao_enviada for True, e exibir mensagem.

- Agora vamos começar as execuções

- Atribuir a class NotificacaoEmail(mensagem) a uma variável.
- Executar a def enviar()

- Atribuir a class NotificacaoSMS(mensagem) a uma variável.

- Vamos testar a def notificar() que checa se a notificação foi enviada

- Atribuir NotificacaoEmail(mensagem) a uma variável.

- Chamar e executar a def notificar(notificacao_email). Receberá a variável
na qual a class foi atribuída.

- Fazer o mesmo com a class NotificacaoSMS():
Nesse caso, irá retornar como notificação não enviada, pois na assinatura do método, 
por ter sido bool, não foi explícito o return True ou False, portanto, 
por uma def retornar None por natureza, o else na condicional if (False)
será executado.
















'''