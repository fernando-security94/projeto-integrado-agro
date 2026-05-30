'''
Exercício
Peça ao usuário para digitar seu nome;
Peça ao usuário para digitar sua idade;
Se o nome e idade forem digitados:
    Exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Se seu nome contém espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A ultima letra do seu nome é
Se nada for exibido em nome ou idade:
    exiba: "Desculpe, voce deixou campos vazios"

'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade != '':
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')

    if ' ' in nome:
        print(f'{nome} contém espaço!')
    else:
        print(f'{nome} não contém espaço!')

    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe! Você precisa preencher todos os dados.')


'''
Exercício de perguntas:
Variável nome receberá um input com o nome do usuário. Variável idade receberá input com idade do usuário.
Condição if para se nome e idade forem diferentes de string vazia, exiba Fstring com nome e o nome invertido através do índice ::-1
Outra condição if, agora se houver espaço no nome, exiba uma mensagem dizendo que contém espaço, caso contrário, exiba mensagem
dizendo que não possui espaço.
Exibir Fstring com a quantidade de letras em nome.
Exibir a primeira letra do nome através do índice 0.
Exibir a última letra do nome através do índice -1.
Caso falte preencher algum input, retornar uma mensagem de erro. Esse else está relacionado ao primeiro if. 




'''