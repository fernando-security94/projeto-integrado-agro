"""
Utilizando lógica em um problema para liberar acesso de salas específicas a funcionários específicos,
onde cada funcionário tem permissões diferentes.

Utilizei um loop While para que o código continue executando após o retorno do resultado
do input, independente de qual seja.

"""

while True:
    employee_name = input("Employee name: ")
    room_A = False
    room_B = False
    room_C = False
    if employee_name == 'Alice':
        room_A = True
        print('Access to room A granted!')
    elif employee_name == 'Bob':
        room_A = True
        print("Access to room A granted!")
    elif employee_name == 'Bob':
        room_B = True
        print("Access to room B granted!")
    elif employee_name == 'Carol':
        room_C = True
        print("Access to room C granted")
    else:
        print("Access denied! Try it again")
    pass