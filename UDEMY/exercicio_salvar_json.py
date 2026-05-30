import json
import os

# Salvar lista de tarefas em banco de dados json

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

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'exercicio_salvar_json.json'
tarefas = ler([], CAMINHO_ARQUIVO)
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
    salvar(tarefas, CAMINHO_ARQUIVO)


"""
Esse exercício consiste em salvar em a lista de tarefas
em um arquivo json, como um banco de dados

Duas novas funções foram criadas para de fato, executar
a ação de json. Mas antes de tudo, é preciso import json

A função def ler foi criada para fazer a leitura do arquivo, 
porém, se executada, apresentará erro pois o arquivo ainda não
existe. Essa função recebe dois parâmetros.
Depois, uma lista vazia é atribuida aos dados que serão salvos
futuramente.

Em uma condição try, vamos tentar abrir with open o parâmetro
caminho_arquivo em 'r'(leitura) as arquivo, e json.load(arquivo) foi atribuido
à variável dados, para carregar os dados salvos a cada execução do código.
Se não for possível,
except como FileNotFoundError (o arquivo ainda não foi criado),
e uma mensagem será exibida e return dados.

Uma def salvar foi criada, também com dois parâmetros, igual
a def ler. O parâmetro tarefas foi atribuido a variável dados.
Vamos abrir with open o caminho_arquivo em modo de 'w'(escrita) as arquivo.

A variável dados receberá json.dump(para salvar no arquivo .json)
com parâmetro tarefas e arquivo, lembrando de indent=2 e ensure_ascii=False,
e return dados.

Vamos criar uma constante, ou seja, uma variável que não vai ser alterada,
escrita com letras maiúsculas.

A variável tarefas, que antes era uma lista vazia, agora chama a def ler,
recebendo uma lista vazia e a constante CAMINHO_ARQUIVO.

Para finalizar e de fato criar o arquivo .json, vamos executar a def salvar
dentro da def ler(), com seus dois parâmetros.


"""
    
