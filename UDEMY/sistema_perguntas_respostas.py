"""
Exercício:
Crie um sistema de perguntas e respostas

"""

# perguntas = [
#     {
#         'Pergunta': 'Qual o nome do atual presidente do Brasil?',
#         'Opções': ['Dilma Roussef', 'Jair Bolsonaro', 'João Goulart', 'Lula da Silva'],
#         'Resposta': 'Lula da Silva',
#     },
    
#     {
#         'Pergunta': 'Qual o nome do atual presidente dos Estados Unidos?',
#         'Opções': ['Barack Obama', 'George W Bush', 'Joe Biden', 'Donald Trump'],
#         'Resposta': 'Joe Biden',
#     },

#     {
#         'Pergunta': 'Quanto é 5 * 5 ?',
#         'Opções': ['35', '55', '25', '10'],
#         'Resposta': '25'
#     }
# ]

# respostas_certas = 0

# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opções']
#     resposta_certa = pergunta['Resposta']
#     for i, opcao in enumerate(pergunta['Opções']):
#         print(f'{i})', opcao)
#     print()

#     escolha = input('Escolha uma opção: ')
#     if escolha == resposta_certa:
#         respostas_certas += 1
#         print('Você acertou!')
#     else:
#         print('Você errou!')

#     print()

# print(f'Você acertou {respostas_certas}')
# print(f'de', len(perguntas), 'perguntas.')


"""
Resolução professor feita apenas com operações aritméticas
"""

perguntas_2 = [
    {
        'Pergunta': 'Quanto é 10 + 10?',
        'Opções': ['30', '45', '20', '5'],
        'Resposta': '20',
    },
    
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['20', '15', '10', '25'],
        'Resposta': '25',
    },

    {
        'Pergunta': 'Quanto é 5 - 5 ?',
        'Opções': ['0', '10', '25', '35'],
        'Resposta': '0'
    },
    {
        'Pergunta': 'Qual o nome do atual presidente do Brasil?',
        'Opções': ['Jair Messias Bolsonaro', 'Luiz Inácio Lula da Silva', 'Dilma Roussef', 'Getúlio Vargas'],
        'Resposta': 'Luiz Inácio Lula da Silva'
    },
]

qtde_acertos = 0
for pergunta2 in perguntas_2:
    print('Pergunta:', pergunta2['Pergunta'])
    print()

    opcoes = pergunta2['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtde_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtde_opcoes:
            if opcoes[escolha_int] == pergunta2['Resposta']:
                acertou = True
    
    print()
    if acertou:
        qtde_acertos += 1
        print('Acertou!')
    else:
        print('Errou!')


    print()

print(f'Você acertou {qtde_acertos} de', len(perguntas_2), 'perguntas.')

