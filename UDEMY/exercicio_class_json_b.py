import json
from exercicio_class_json_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

fazer_dump()


with open(CAMINHO_ARQUIVO, 'r') as file:
    dados = json.load(file)
    
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3= Pessoa(**dados[2])

    print(p1.nome, p1.idade, sep=', idade: ')
    print(p2.nome, p2.idade, sep=', idade: ')
    print(p3.nome, p3.idade, sep=', idade: ')


"""
Continuando o exercício, agora, em outro arquivo, precisamos
carregar os dados json para o Python.

O primeiro passo é import json, e na sequência, trazer a constante CAMINHO_ARQUVO,
a class Pessoa e a def fazer_dump() através de:
from exercicio_class_json_a import 'tudo o que eu quero trazer'

Chamar a def fazer(dump) para adiar a execução no arquivo a, assim, o dump
 de valores será apenas no arquivo b, como o exercício propõe, e também foi
feito através de if __name__ == '__main__'

Para carregar os dados nesse arquivo, o procedimento é similar ao de abertura
with open(CAMINHO_ARQUIVO, 'r') as file: 
    dados = json.load(file)

(modo 'r' é para leitura)

Para que todas as instâncias sejam exibidas, é necessário chamá-las
e expandi-las com ** e com seus respectivo índices. 
Não é necessário escrever os valores novamente. 

Vamos exibir as três instâncias, chamando print(p1.nome, p1.idade),
com sep=', idade: ') somente para ficar melhor ilustrado.






"""