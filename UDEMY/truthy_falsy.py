# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [listas], {dicionários} set()
# Imutáveis (tupla) 'string' 0  0.0  None False range(0, 10)

# Tudo o que for vazio, será falsy. Se tiver um espaço em branco
# será considerado não-vazio, portanto, thruthy

lista = []
dicionario = {}
conjunto = set()
tupla= ()
string = ''
inteiro = 0
flutuante = 0.0
nao_valor = None
falso = False
alcance = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'thruthy'

print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nao_valor=}', falsy(nao_valor))
print(f'{falso=}', falsy(falso))
print(f'{alcance=}', falsy(alcance))
