"""
É importante tomar cuidado com os excessos de uso de condicionais, 
pois quanto mais condicionais, mais complexo e maior risco de bugs
o código vai encontrar.

O guard clause, guarde code ou guard statement tem como objetivo otimizar as linhas de código,
com menos condicionais.

"""


import os
# Exemplo sem guard clause

def f_noguard(x):
    if isinstance(x, int):
        #code
        #code
        #code
        return x + 1
    else:
        return None
    
# Ao utilizar o primeiro return, o else se faz desnecessário,
# além disso, se a condicional for false, automaticamente a função retornará
# none.

# Exemplo com guard clause

def f_withguard(x):
    if not isinstance(x, int):
        return None
    #code
    #code
    #code
    return x + 1

# Checando a condição ao contrário, ou seja, se a condição if not for verdadeira,
# return none, se for falsa, a sequência de códigos será executada até 
# retornar x + 1. Ps: return sozinho e return None são a mesma coisa

# Exercício de listam de tarefas sem condicional if


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
    listar(tarefas)    

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} foi adicionada novamente.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa ou comando.')
        return
    print(f'{tarefa=} foi adicionada.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


tarefas = []
tarefas_refazer = []




while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()



    # if tarefa == 'listar':
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
    # elif tarefa == 'clear':
    #     os.system('cls')
    #     continue
    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
    #     continue


'''
Foi feita uma forma alternativa de executar as funções
do exercício de lista de tarefas, sem utilizar repetidamente
as condicionais if, elif, else, justamente pelo excesso de 
repetições. Para isso, foi feito através de guard clause e também
de closure, que consiste em adiar a execução de uma função,
através de outra função.

Nesse caso, as funções lambda foram a melhor opção,
por se tratarem de funções anônimas, ocupam pouco espaço
e fazem closure.

Então, a variável comandos receberá um dicionário, tendo
como chaves, as opções a serem escolhidas na lista de tarefas,
e os valores são as funções lambda executando as def listar(),
def desfazer(), def refazer(), def os.system() e 
def adicionar(), sendo 'listar': lambda: listar(tarefas)



'''