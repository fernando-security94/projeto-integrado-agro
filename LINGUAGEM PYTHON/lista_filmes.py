# lista de 5 filmes
filmes = ['Naufrago', 'Avengers','Tarzan','Mogli','A Forja']
# Inicializacao
print("Olá, bem vindo a avaliação de filmes!\n")
print("A seguir, voce deve avaliar os filmes de 1 a 5")
print("Para encerrar as avaliações, digite 0(zero)\n")

notas = []

# iteracao sobre todos os valores de filme
for filme in filmes:
    avaliacao = int(input(f'Qual nota você avalia o filme {filme}? '))

        # range de avaliacao permitido
    if avaliacao < 0 or avaliacao > 5:
        print("Notas não permitidas!")
        continue

    print()
    # opçao de saida
    if avaliacao == 0:
        print("Encerrando avaliação!")
        break

    #exibe o filme e sua respectiva nota
    notas.append(filme)
    notas.append(f'Nota: {avaliacao}')

    print(f'Avaliações: {notas}')

print("Obrigado por avaliar os filmes!")

