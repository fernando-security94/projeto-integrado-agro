rent = 730
net = 250
food = 500
card = 8100

total_BRL = rent + net + food + card

print(f'Total em real: {total_BRL}\n')

total_USD = total_BRL / 5.58

print(f'Total em USD: {total_USD:.2f}\n')


cartao_poli_BRL = 3585
loan_BRL =2870

total_poli = cartao_poli_BRL + loan_BRL 
print(f'Total Poli BRL: {total_poli}\n')

total_poli_USD = (total_poli / 5.58)
print(f'Total Poli USD: {total_poli_USD:.2f}\n')


MANDAR_BR = total_poli_USD + total_USD
print(MANDAR_BR)