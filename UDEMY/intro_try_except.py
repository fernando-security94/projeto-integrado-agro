'''
Introdução ao try/except
try --> Tentar executar algo do código
execpt --> ocorreu um erro ao tentar executar

'''
numero_str = input('Vou dobrar o número que voce digitar: ')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2}')
# else:
#     print('Value error!')

try:
    print('STR: ', numero_str)
    
    # Assim que um erro for encontrado dentro do laço try, a execeção será executada.
    # Fail fast é um erro prematuro para pular diretamente para a exceção. 
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
    
except:
    print('Isso não é um número!')