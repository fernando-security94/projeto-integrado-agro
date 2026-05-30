# Criar lista de tarefas interativa

import os

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        print()
        return
    
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa=} foi removida.')
    tarefas_refazer.append(tarefa)
    print()    

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} foi adicionada novamente.')
    tarefas.append(tarefa)
    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa ou comando.')
        return
    print(f'{tarefa=} foi adicionada.')
    tarefas.append(tarefa)
    print()


tarefas = []
tarefas_refazer = []


while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('cls')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue

"""
Rubber duck debuger

Esse exercício consiste em criar uma lista de tarefas,
utilizando diversas funções que executarão ações, como
listar, desfazer e refazer. É necessário também, criar uma 
função que adicione tarefas a lista.

Criando função listar:
Uma def foi criada e recebe um argumento(tarefas). 
Vamos fazer uma condicional if not para checar se existe alguma
tarefa na lista. Se essa condicional for True,
uma mensagem será exibida, print() para pular uma linha,
e return será para encerrar a função.

Criando função desfazer:
Uma def foi criada e recebe dois argumentos(tarefa, tarefas_refazer),
Da mesma forma que foi criada uma condicional if not,
nessa função também será utilizada, e caso seja True
uma mensagem será exibida.

Para acessar o último valor e remove-lo da lista, vamos usar
a função pop() e exibir que a {tarefa=} foi removida.
Para que a terefa removida seja salva em outra lista, e quando
a def refazer for executada e esse valor seja adicionado novamente
a lista, será através de tarefa_refazer.append(tarefa). 
Dessa forma o valor é removido, mas não apagado. Return para
encerrar a função.

Criando função refazer:
A base dessa def é a mesma da def desfazer, da mesma forma,
se não houver tarefa a desfazer, uma mensagem será exibida.

Para readicionar a tarefa anteriormente removida, será o inverso
da def desfazer, ou seja, tarefa = tarefas_refazer.pop(), para 
remover da lista onde foi colocada após ser removida,
e tarefas.append(tarefa) para ser adicionada novamente na lista
de tarefas.

Criando função de adicionar:
Def adicionar criada com dois argumentos(tarefa, tarefas)
Foi formatada com tarefa =  tarefa.strip() para cortar espaços vazios.
Condicional if not se o usuário não digitar nada, uma mensagem
será exibida.

Para adicionar o que o usuário digitou, tarefas.append(tarefa), ou sej
a lista tarefas terá um append da tarefa digitada.

Agora para as execuções das funções, duas listas foram criadas.
Tarefas, que receberá as tarefas de fato, e tarefas_refazer,
que receberá as tarefas que foram removidas.

Dentro de um laço While True, uma mensagem exibindo as opções
para o usuário, e na sequencia, o usuário terá um input para
escrever uma tarefa ou comando.

Então, uma série de condições if/elif para comparar o que o 
usuário digitou, para que a função adequada seja executada.

Então, se tarefa == 'lista', a def listar(tarefas) será executada

Se o usuário digitar 'desfazer', e def desfazer(tarefas, tarefas_desfazer)
será executada. Nessa def, a lista tarefas_desfazer é utilizada
para receber a tarefa removida. E a cada execução de qualquer
função, vamos exibir a lista de tarefas novamente.

Se o usuário digitar 'refazer', a def desfazer(tarefas, tarefas_refazer) receberá os mesmos
argumentos da def refazer, pois precisa acessar a última atividade removida.

Utilizamos import os para limpar o terminal sempre que quiser,
então se o usuário digitar 'clear, os.system('cls') será 
executao.

Por fim, ao escrever qualquer outra coisa, a def adicionar(tarefa, tarefas)
será executada, adicionando uma tarefa a lista de tarefas, de acordo
a ordem dos argumentos.





"""