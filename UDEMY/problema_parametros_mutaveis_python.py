# Problema dos Parâmetros Mutáveis em funções Python

'''
def add_clients(name, list=[]):
    list.append(name)
    return list

client1 = add_clients('Fernando')
add_clients('Poliane', client1)
print(client1)

'''

# Forma ideal de utilizar funções sem valores mutáveis como parâmetros padrão
# evitando a reptição a cada execução.

def add_clients(name, list=None):
    if list is None:
        list = []
    list.append(name)
    return list

client1 = add_clients('Fernando')
add_clients('Poliane', client1)
add_clients('Felipe', client1)
add_clients('Arthur', client1)
client1.append('Tamires')


client2 = add_clients('Marlos')
add_clients('Edna', client2)

client3 = add_clients('Fábio')
add_clients('Edson', client3)
add_clients('Raquel', client3)

print(client1)
print(client2)
print(client3)