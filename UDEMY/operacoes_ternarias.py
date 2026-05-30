'''
Operação ternária (condição de uma linha)
<valor> if <condição> else <outro valor>

É uma forma de utilizar condicional if resumida em uma linha. Recomendada apenas para pequenas condiçoes
'''

digito = 9
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito

print(novo_digito)