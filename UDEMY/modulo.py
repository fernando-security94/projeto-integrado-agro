import json 
import os

# people = [
#     {
#         'nome': 'Maria',
#         'sobrenome': 'Santos',
#         'idade': 35,
#         'ativo': False,
#         'notas': ['A', 'A+'],
#         'telefones': {
#             'residencial': '00 0000-0000',
#             'celular': '00 00000-0000',
#         },
#     },
#     {
#         'nome': 'Joana',
#         'sobrenome': 'Moretti',
#         'idade': 85,
#         'ativo': True,
#         'notas': ['B', 'A'],
#         'telefones': {
#             'residencial': '11 1111-1111',
#             'celular': '11 11111-1111',
#         },
#     },
# ]
# BASE_DIR = os.path.dirname(__file__)
# SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python.json')

# with open(SAVE_TO, 'w') as file:
#     json.dump(people, file, indent=2)  # função dump executa e despeja esses dados em um arquivo.json

# print(json.dumps(people, indent=2))  # dumps é um dump em uma string, que será exibido no terminal
#                            # do próprio código, sem a necessidade de criar um arquivo.json


# Carregando arquivo json

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')

'''with open(JSON_FILE, 'r') as file:  # usando r para read o arquivo carregado
    people = json.load(file)  # função load carrega o arquivo json
    
    for person in people:
        print(person['nome'])  # laço for para acessar e retornar os valores da chave nome
                               # caso nao use for, a lista inteira será exibida.
'''


