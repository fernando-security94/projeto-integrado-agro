import os

""" 
Criando arquivos com Python
Usamos a função open para abrir 
um arquivo em Python (Ele pode ou não existir)

Modos:
- r (read), w(write), b(binary)
- t (text), + (read and write)
- a (escreve no final do arquivo)
- context manager com with (abre e fecha)

Métodos úteis:
- write, read (escrever e ler)
- writeline (escrever várias linhas)
- seek (move o cursor)
- readline (ler linha)
- readlines (ler linhas)

O módulo os será mais abordado, mas:
- os.remove ou unlink - apaga o arquivo
- os.rename - troca o nome ou move o arquivo

O módulo json tbm será mais abordado, mas:
- json.dump - Gera um arquivo json
- json.load - 

"""

# Abrir arquivo e criando ao mesmo tempo

file_path = 'C:\\Users\\Fernando Ribeiro\\OneDrive\\Área de Trabalho\\curso_python_udemy\\Nova Pasta do curso\\'
file_path += 'criando_arquivos_com_python.txt'

# file = open(file_path, 'r')  # Vai apresentar erro pq ainda nao existe nenhum arquivo 

# file = open(file_path, 'w')

# file.close()  # sempre que abrir um arquivo, deve fechar imediatamente


# Abrindo e fechando arquivo com context manager:

with open(file_path, 'w+') as file:
    print(type(file))
    file.write('Line one - Hello World!\n')
    file.write('Line two - How is everything?\n')
    file.write('Line three - Everything is great! What about you?\n')
    file.writelines(
    ('Line four - Jesus is the only way\n', 'Line five - He is my Lord and Savior\n')
    )
    print('Lendo...')
    file.seek(0, 0)
    print(file.readline(), end='')
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.readline())

    print('READLINES')  
    file.seek(0, 0)
    for line in file.readlines():  # Lendo todas as linhas de uma vez
         print(line.strip())       # atraves do laço for

print()

# Lendo o arquivo com read, mas primeiro precisa abrir o arquivo novamente

# with open(file_path, 'r') as file:
#     print(file.read())


# O modo 'w' apaga e escreve novamente tudo o que for alterado.

# O modo 'a' de append, somente adiciona ao fim do arquivo sempre
# que executado, a diferença é que não apaga nada. Então, se eu executar
# o mesmo código diversas vezes, mesmo sem alterações, todos os valores
# serão adicionados. O que pode ser interessante para arquivos de log.

with open(file_path, 'w+', encoding='utf8') as file:  # enconding= foi utilizado para padronizar a codificação de caracteres

# with open(file_path, 'a+') as file:
    ...

    file.write('Line one - Hello World!\n')
    file.write('Line two - How is everything?\n')
    file.write('Line three - Everything is great! What about you?\n')
    file.write('Line three - Everything is great! What about you?\n')  # repetindo para ver alteração no arquivo.
    file.write('Line three - Everything is great! What about you?\n')  # repetindo para ver alteração no arquivo.
    file.writelines(
    ('Line four - Jesus is the only way\n', 'Line five - He is my Lord and Savior\n',
     'Line six - ATENÇÃO\n')
    )

    print('READING...')
    file.seek(0, 0)
    for line in file.readlines():  # lendo todas as linhas com laço for + .readlines()
        print(line.strip())


# Módulo os:
'''
- os.remove ou unlink - apaga o arquivo
- os.rename - troca o nome ou move o arquivo
'''

# Formas de apagar o arquivo:

# os.remove(file_path)  
# ou
# os.unlink(file_path)

# Para renomear:

# os.rename(file_path, 'novo nome endereço') - os.rename recebe dois argumentos, o primeiro é o arquivo(caminho do arquivo) em si,
# e o segundo é referente ao novo nome ou endereço. 


# with open abre e fecha o arquivo sem a necessidade de .close()

'''
Tipos de dados em json

number - 1234.12
bool - true
null - nulo
"string"- texto
[] array - lista em Python
{} objeto - dicionário em Pyton

'''