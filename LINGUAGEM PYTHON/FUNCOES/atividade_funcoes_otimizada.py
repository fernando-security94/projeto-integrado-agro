materias = ['Materia1', 'Materia2', 'Materia3', 'Materia4']
print("Boletim eletrônico:")
notas = []

for materia in materias:
    entrada = input(f'Qual a nota da matéria {materia}? (ou digite "Finalizar" para sair): ')
    
    if entrada.lower() == 'finalizar':
        print("Avaliação finalizada!")
        break

    try:
        avaliacao = float(entrada)
        if avaliacao < 0 or avaliacao > 10:
            print("Nota não permitida! Insira um valor entre 0 e 10.")
            continue
    except ValueError:
        print("Entrada inválida! Digite um número ou 'Finalizar'.")
        continue

    notas.append(avaliacao)

# Exibir boletim ao final
if notas:
    media = sum(notas) / len(notas)
    print("\nMatérias e suas respectivas notas:")
    for i in range(len(notas)):
        print(f"{materias[i]}: {notas[i]}")

    print(f"\nMédia final: {media:.2f}")
    if media < 7:
        print("Aluno reprovado!")
    else:
        print("Aluno aprovado!")
else:
    print("Nenhuma nota foi registrada.")
