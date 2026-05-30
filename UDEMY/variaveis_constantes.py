'''
Constantes são "variáveis" que não vão mudar, ou seja, tem seu valor FIXO.
Muitas condições no mesmo laço if é ruim.
    <-- Contagem de complexidade é ruim.
'''

velocidade = input( 'Velocidade do carro: ')  # velocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # Velocidade máxima permitida pelo radar 1
LOCAL_1 = 100  # Local em que o radar 1 está. 
RADAR_RANGE = 1  # Distancia que o radar pega 

velocidade_carro_radar = int(velocidade) > RADAR_1

# Jogar a expressão em uma variável permite deixar o código mais legível
# e também permite noemar a expressão com uma situação, como no exemplo abaixo:

carro_passou_radar = local_carro >= (LOCAL_1 -  RADAR_RANGE) and \
     local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade_carro_radar  # Se todas essas condições forem verdadeiras
                                                                        # o carro passou pelo radar


if velocidade_carro_radar:
    print("Excedeu o limite de velocidade do radar 1")

if carro_passou_radar:
    print('O carro foi multado pelo radar!')
else:
    print('O carro não foi multado pelo radar! ')

#   O radar vai localizar o carro nos Kms 99 à 101. 
# if local_carro >= (LOCAL_1 -  RADAR_RANGE) and \
#      local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade_carro_radar:
#      print('O carro foi multado pelo radar!')
# else:
#     print('O carro não foi multado!')