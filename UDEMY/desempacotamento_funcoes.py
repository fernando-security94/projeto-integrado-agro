'''
Desempacotamento em chamadas de métodos e funções

'''

string = 'ABC'
lista = ['Maria', 'Helena',1, 2, 3, 4, 5,  'Eduarda']
tupla = 'Python', 'é', 'legal'

primeiro, segundo, terceiro, *_, ap, ultimo = lista
print(primeiro, ap, ultimo,)

# iterando sobre a lista usando for 
for nome in lista:
    print(nome, end=' ')
print()

# iterando sobre a lista usando função *  direto com print. É o mesmo que usar o for + end=' '
print(*lista)

for i in string:
    print(i)

print(*string)

print()

for j in tupla:
    print(j)

print(*tupla)



'''
Dissertando desempacotamento em chamadas
No caso da lista, foi utilizado uma chamada para cada valor que a lista possui,
e quando houver *_ significa que todos os valores dalí em diante, serão agregados a variável _, que 
não será utilizada, ou em qualquer outro nome, porém, caso *_ não seja a última chamada, os valores agregados
dependerão da quantidades de chamadas que vierem depois.

Exemplo: lista = ['Maria', 'Helena',1, 2, 3, 4, 5,  'Eduarda']
primeiro, segundo, terceiro, *_, ultimo = lista

Nesse caso, *_ está englobando os valores '2, 3, 4, 5', ja que "último" receberá 'Eduarda',
pois somente uma chamada foi adicionada após *_



'''