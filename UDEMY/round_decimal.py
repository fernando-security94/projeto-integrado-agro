'''
Imprecisão de ponto flutuante

'''
import decimal  # módulo que possui uma classe para calcular e corrigir precisamente as casas decimais

# Apesar de extremamente preciso, não há a necessidade de usar esse módulo, a não ser em situações muito específicas
# onde a exata precisão seja fundamental para o funcionamento do programa.
# Para evitar um distúrbio com números muito grandes, a funcão decimal.Decimal pode receber uma string, assim poderá aplicar a lógica de 
# arredondamento automáticamente

# numero_1 = 0.1
# numero_2 = 0.7
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2

print(numero_1)
print(numero_2)

print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))  # após chamar a função round, selecionar o número a ser arredondado e depois qtde de casas decimais
print(type(numero_3))  # Uma vez que utilizada a função decimal.Decimal, o typo de dado deixa de ser float e passa a ser decimal.Decimal