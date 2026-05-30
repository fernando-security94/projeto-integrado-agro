# Sistema de cinema que 
# checa a idade do usuario
# recebe quantidade de ingressos disponiveis
# recebe quantidade de ingressos a serem comprados
# exibe ingressos disponiveis apos a compra
# exibe o filme adequado de acordo a idade

ingressos_totais = 10  # fora do laço while para atualizar a cada execução

while True:
    
    print(f'Ingressos disponiveis: {ingressos_totais}\n')

    usuario1 = int(input("Qual a idade do usuario 1: "))
    usuario2 = int(input("Qual a idade do usuario 2: "))
    ingresso_ususario1 = int(input("Quantos ingressos para o usuario 1: "))
    ingresso_ususario2 = int(input("Quantos ingressos para o usuario 2: "))
    ingressos_venda = ingresso_ususario1 + ingresso_ususario2


    # condicao para idade menor que zero
    if usuario1 <= 0 and usuario2 <= 0:
        print("Não existe idade menor ou igual a zero.")
        continue

    if ingressos_venda > ingressos_totais:
        print("Ingressos indisponíveis!")   
        break
    
    # subtrai os ingressos vendidos dos totais
    ingressos_totais -= ingressos_venda  

    

    # condicao de faixa etária
    if usuario1 and usuario2 < 18:
        print("Indicados para assistir o FILME 1.\n")
    elif 18 <= usuario1 <= 60 and 18 <= usuario2 <= 60:
        print("Indicados para assistir o FILME 2.\n")
    elif (usuario1 < 18 and usuario2 >= 18) or (usuario1 >= 18 and usuario2 < 18):
        print("Os usuarios devem assistir filmes diferentes.\n")
    else:
        print("Indicados para assistir o FILME 3.\n")

    # exibe os ingressos restantes após a subtração
    print(f'Ingressos restantes: {ingressos_totais}\n')

    if ingressos_totais == 0:
        print("Não há ingressos disponíveis!")