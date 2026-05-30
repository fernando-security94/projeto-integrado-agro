# Context manager com função - Criando e usando gerenciadores de contexto

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    print('Abrindo o arquivo')
    try:
        file = open(caminho_arquivo, modo, encoding='utf8') 
        yield file
    except Exception as error:
        print('An error has occurred', error)
    finally:
        print('Fechando arquivo')
        file.close()
    
    


with my_open('context_manager.txt', 'w') as file:
    file.write('Line 1\n', 2)
    file.write('Line 2\n')
    file.write('Line 3\n')
    file.write('Line 4\n')
    print('WITH', file)

'''
Context manager utilizando função, mas que na verdade
é um generator

De uma forma mais simples, podemos utilizar uma função no Python da biblioteca contextlib
Então, vamos começar com from contextlib import contextmanager

Logo de cara, precisamos decorar a função que será responsável
pela abertura e fechamento do arquivo, sem a necessidade
de usar __enter__ e __exit__

- Decorar a def my_open com @contextmanager.

- A def my_open(caminho_arquivo, modo) recebe dois
parâmetros. Não será necessário instanciá-los, pois
não se trata de __init__

- Exibir mensagem de abertura de arquivo

- Atribuir a função open() a uma variável e receber
os parâmetros da def my open + a formatação enconding='utf8'

- Ao invés de usar o return, comumente utilizado em funções,
vamos chamar yield, o que tornará essa função um 
generator:

- yield file

- Exibir mensagem de fechamento do arquivo

- Fechar o arquivo com file.close()

- Com a função with, vamos executar a def my_open,
passando seus argumentos posicionais referentes 
ao caminho_arquivo e modo as file, como feito
em context manager com __enter__ exit__

- Adicionar as linhas com file.write()

- Para tratar exceção, vamos utilizar try/except/finally,
porem, o recomendado é deixar try/finally, pois se
tratar a exceção, o programa pode rodar e fechar 
o arquivo mesmo com o erro, ja com try/finally,
o desenvolvedor será obrigado a ajustar o código.










'''