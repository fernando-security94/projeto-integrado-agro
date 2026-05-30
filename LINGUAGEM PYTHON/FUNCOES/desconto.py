# calculadora de desconto 

valor_produto = float(input("Valor do produto: $ "))
valor_desconto_percentual = float(input("Digite o valor do desconto: % "))


# funcao que calcula desconto
def calcula_desconto(desconto):
    desconto = valor_produto *(valor_desconto_percentual/100)
    return desconto

# poderia ter feito o calculo direto na variavael valor_desconto
# valor_desconto = valor_produto*(valor_desconto_percentual/100)

valor_desconto = calcula_desconto(valor_desconto_percentual)
valor_final = valor_produto - valor_desconto

if valor_desconto < 0 and valor_desconto >= 100:
    print("Desconto incorreto!")
else:
    print(f'Valor do desconto: ${valor_desconto:.2f}')

print(f'Valor do produto com desconto: ${valor_final:.2f}')