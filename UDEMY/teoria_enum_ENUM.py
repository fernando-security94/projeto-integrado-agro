# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado numero de coisas.
# Enums tem membros e seus valores constantes.
# Enums em Python:
#  - São um conjunto de nomes simbólicos (membros) ligados a valores unicos
#  - Podem ser iterados para retornar seus membros canônicos na ordem de
#   definição.
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
# diretamente (mesmo assim, ENUMS não são classes normais em Python).
# Enum pode ser usado com type annotations, com isinstance e 
# outras coisas relacionadas com o tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum



# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])
class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()


print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(2).name, Direcoes.ESQUERDA.value)


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direcao nao encontrada')
    
    print(f'Movendo para {direcao.name} ({direcao.value})')

print()
mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
# mover('esquerda')
# mover('direita')
# mover('cima')


