'''
Faça uma lista de compras usando listas
O usuário deve ter a possibilidade de inserir, apagar e listar
valores da sua lista
Não permita que o programa quebre com erros
de indices inexistentes

'''
import os

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        produto = input('Produto: ')
        lista.append(produto)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Não foi possível apagar esse índice. Digite números inteiros')
        except IndexError:
            print('Indice inexistente!')
        except Exception:
            print('Erro desconhecido')
    
    elif opcao == 'l':
        os.system('cls')
    
        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Escolha uma das opções!')
    
    
'''
Dissertando o exercício
Importar módulo os para limpar o terminal a cada opção que o usuário digitar
Dentro de um laço While True para gerar repetição da lista, será exibida uma mensagem 
e uma variável opcao que receberá input para o usuário digitar a opção desejada.
Inserir, apagar ou listar.

Laço if se o usuário digitar [i] de inserir, o terminal será limpo, a variável produto receberá um outro input
para que o usuário digite o produto a ser adicionado, e atraves de lista(append) o produto digitado foi salvo na lista.
Se o usuário digitar [a] de apagar atraves de elif, uma nova variável indice_str receberá um input para o usuário escolher
qual índice será apagado. 

Dentro de um bloco try, como se trata de um índice, uma nova variável "indice"
receberá um input e  haverá um type conversion para int. Caso o type conversion seja feito corretamente, o índice digitado será
apagado através de del lista[indice].
Caso o usuário digite um valor que não possa ser convertido para int, haverá uma exceção com except ValueError,
uma mensagem será exibida , e retornando novamente para escolher qual índice deve ser apagado. 
Caso o usuário digite um índice inexistente, haverá uma exceção com except IndexError, 
uma mensagem será exibida, e retornando novamente para escolher qual índice deve ser apagado.
Caso ocorra algum erro desconhecido, será levantado uma exceção através de except Exception, 
exibindo uma mensagem de erro desconhecido.

Se o usuário através de elif digitar [l] de listar, o terminal será limpo com os.system('cls')
Dentro desse laço, será feito um if, caso o tamanho da lista for == 0, será exibida uma mensagem, caso contrário,
será feito um laço for para iterar em cada item da lista, com dois argumentos i e valor, para receber o índice através 
de enumerate(lista) e o valor digitado pelo usuário em produto.

E por fim, um else para caso nenhuma das opções foram escolhidas pelo usuário, exibindo uma mensagem e voltando
para o começo do laço.


'''
    
    
    
