'''
method vs @classmethod vs @staticmethod
method- self, método de instância
@classmethod - cls, método de classe
@staticmethod - método estático. Nem de instância e nem de classe


'''

class Connection:
    def __init__(self, host='localhost'):  # method
        self.host = host
        self.user = None
        self.password = None


    def set_user(self, user):  # setter
        self.user = user
        

    def set_password(self, password):
        self.password = password
        

    
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def connection_log(msg):
        print('LOG:', msg)
        return msg
    
print(Connection.connection_log('Essa é a mensagem de log.'))


c1 = Connection.create_with_auth('fernando', '1234')



# c1 = Connection()
# c1.set_user('fernando')
# c1.set_password('1234')

print(f'Usuário: {c1.user}')
print(f'Senha: {c1.password}')




# Sempre que necessário usar algo de SELF, esse é um método de instância (method)

'''
Nessa aula, veremos a diferença entre method, @classmethod e @staticmethod

Method sempre será relacionado ao self, ou seja, a instância da classe, e,
quando novas instâncias self forem criadas, elas terão acesso direto ao
__init__

@classmethod, como o próprio nome diz, está relacionado ao molde
da classe, e não usa-se self, mas, cls, que é a própria classe, como primeiro
parâmetro.

@staticmethod é literalmente estático. Não tem acesso ao self, nem ao cls.
Pode ser considerado como uma constânte, que contenha uma informação fixa,
como no exemplo do código, uma mensagem de log.

Em relaçao aos exemplos de código:
- Uma class connection foi criada, a def __init__ recebe self, host='localhost'
Então, atribuímos self.host = host, self.user e self.password
serão None, pois ainda não foram atribuídos.

Depois, uma instância def set_user foi criada, recebendo self, user, para de fato,
criar o usuário. O mesmo foi feito para def set_password

Não é errado criar essas instâncias de forma separada, mas, é 
possível uni-las em uma única instância, através de @classmethod,
que vai utilizar o molde da classe, mas com seus próprios parâmetros,
pois em @classmethod, não é possível acessar o self.

- @classmethod def_create_with_auth(cls, user, password)
foi criada. Após receber cls (a própria classe), receberá user
e password de uma vez.

A classe cls foi atribuída a uma variável para que possamos criar o 
usuário e senha através de connection.user = user e 
connection.password = password

E vamos return connection para que interromper a execução e 
não exiba None (pois toda def retorna None por natureza)

Um @staticmethod foi criado somente para exibir uma mensagem fixa de log
É importe reparar, que @staticmethod não recebe self, nem cls, somente o 
parâmetro, que no caso foi:
@staticmethod(msg)

E return msg para interromper a execução.


Para que possamos exibir user e password de forma individual,
primeiro atribuir a classe Connection a uma variável.
Depois, executar a c1.set_user('fernando') e c1.set_password('1234')

E também, é necessário print c1.user e c1.password para exibir.

Para fazer a mesma coisa, só que com user e password ao mesmo tempo,
Vamos atribuir a uma variável a class Connection com o @classmethod,
passando parâmetros posicionais, da 
seguinte forma:
c1 = Connection.create_with_auth('fernando', '1234')

Vamos exibir com fstrings por questão estética.


'''