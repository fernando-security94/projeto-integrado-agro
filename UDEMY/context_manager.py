# Context Manager com classes
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o Python vai usar.
# Isso é chamado de Duck typing. Um conceito relacionado
# com tipagem dinâmica onde o Python não está interessado no
# tipo, mas se alguns métodos existem no seu objeto para que
# ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como 
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção
# e o traceback. Se ele retornar True, a exceção no with será
# suprimida.

# ex:
# with open('context_manager.txt', 'w') as file:
#     ...
    
# Implementar o open:

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
        print('INIT')

    def __enter__(self):
        print('Opening file')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('Closing file')
        self._arquivo.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)

        # print(class_excepetion)
        # print(exception_)
        # print(traceback_)

        # exception_.add_note('Minha nota')


        # return True   # Trata a exceção permitindo executar o programa com erro
        



with MyOpen('context_manager.txt', 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')
    file.write('Line 4\n')
    print('With', file)


"""
O context manager é utilizado para criar seus próprios
protocolos, sendo uma classe que possui métodos,
que dentre eles, abrir e fechar arquivos.

- Criar a class MyOpen

- Inicializar a class com __init__(self, caminho_arquivo, modo) e receberá dois 
parâmetros que serão utilizados para abrir o arquivo. 

- Instanciar self.caminho_arquivo  = caminho_arquivo e self.modo = modo

- Instanciar self._arquivo = None, que será o arquivo de fato a ser aberto.

- Exibir mensagem dizendo que está no INIT

- Criar o método de abertura def __enter__(self)

- Abrir o arquivo com self._arquivo utilizando o métoodo open,
e receberá as instâncias self.caminho_arquivo, self.modo, e 
enconding='utf8'

- Em context manager, é necessario open() e close um arquivo.

- Vamos criar o método def __exit__(self, class_exception, exception_, traceback_)

- Obrigatóriamente, o método exit deve receber a exceção da classe,
a exceção em si e o traceback.

- Quando existir a possibilidade de uma palavra ser utilizada
pela linguagem, adicionamos _ no final, como por exemplo,
exception_ e traceback_

- Vamos exibir uma mensagem de fechamento

- E fechar o arquivo com self._arquivo.close()

- Vamos adicionar uma nota, caso uma exceção seja levantada, através de
exception_add_note('Minha nota)

- Porém, se o ____exit__ retornar True, todos os erros serão suprimidos,
e o programa vai continuar rodando, mesmo contendo exceções.

- Feita toda a lógica para a abertura do arquivo, vamos
executar utilizando o with MyOpen, que é uma classe que
abre e fecha um arquivo.

- with Myopen('context_manager.txt', 'w') as file:- os argumentos posicionais
são referentes a caminho_arquivo, que é literalmente o endereço
onde o arquivo se encontra e 'modo', que no caso, será modo escrita 'w'.

- Vamos adicionar linhas com o método write():

- file.write('texto com quebra de linha')

- É recomendado testar o context manager ao levantar uma exceção. Então, podemos
adicionar um argumento a mais em qualquer uma das execuções, ja que apenas
1 argumento posicional foi pedido.

- Vale dizer, que com esse módulo, só é permitido utilizar iteráveis,
como str.

- Vamos exibir as características do file, dentro do método with,
que retornará os valores de 'caminho_arquivo', 'modo' e enconding='utf8'





"""

