# Sistema de cadastro de notas e calculo da média

print("Boletim eletrônico: ")

# Lista vazia que receberá notas
notas = []

# Inserção de notas
nota1 = float(input("Insira a nota1: "))
nota2 = float(input("Insira a nota2: "))
nota3 = float(input("Insira a nota3: "))
nota4 = float(input("Insira a nota4: "))

# Por se tratar de lista e não-iteráveis, usei a funcao
# .append() para adicionar as nota inseridas à lista vazia
notas.append(nota1)
notas.append(nota2)
notas.append(nota3)
notas.append(nota4)

# funcao que calcula media
# poderia ter feito num laço for ou direto em uma variavel
# mas usei função devido ao checklist da atividade
def calcula_media(notas):
    return sum(notas)/len(notas)

# Chamada da função
media_final = calcula_media(notas)

# Exibição das notas e média
print(f'Notas do aluno: {notas}')
print(f'Média final: {media_final:.2f}\n')

# Condicional de aprovação
if media_final < 7:
    print(f'Aluno reprovado. Média {media_final:.2f}')
else:
    print(f'Aluno aprovado! Média {media_final:.2f}')



