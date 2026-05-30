# Exercicio - Salvar a classe em json
# Salvar os dados da classe em json
# e depois, criar novamente as instâncias
# da classe com os dados salvos
# Fazer em arquivos separados

import json

CAMINHO_ARQUIVO = 'exercicio_class.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Fernando', 30)
p2 = Pessoa('Poliane', 43)
p3 = Pessoa('Laura', 1)
dados = [vars(p1), vars(p2), p3.__dict__]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as file:
        print('FAZENDO DUMP')
        json.dump(dados, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('Ele é o __main__')
    fazer_dump()


"""
A proposta do exercício é salvar a classe e seus dados em json
e depois, em um arquivo separado, criar novamente suas instâncias.

A primeira parte é simples, import json e depois, criar uma
constante que será CAMINHO_ARQUIVO, ou seja, uma variável que sabemos
que não será mudada. 

O próximo passo será criar a class Pessoa, e terá dois atributos, nome e idade.
Após criar 3 variáveis com os atributos para a classe, vamos atribuí-los
a uma outra variável dados, que receberá os atributos consumidos com
vars() ou __dict__

Criamos uma def fazer dump(), mas somente para o final, não será
relevante agora, pois ainda não depositamos os dados em um arquivo
json. Apesar disso, essa def servirá de escopo, e receberá
with open(CAMINHO_ARQUIVO, 'w') as file:
    json.dump()

Ou seja, vamos salvar o arquivo json dentro do escopo da def fazer dump()
para que de fato, o dump dos dados e carregamento seja feito apenas
no outro arquivo.

É importante frisar, que ao abrir with open, é necessário usar 'w' para escrita.

Uma condicional foi criada somente para exibir onde o dump será feito.
if __name__ == '__main__', executar fazer dump().





"""