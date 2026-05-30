import importlib  # módulo para recarregar outro módulo

import modulos_sys_path_m  


print(modulos_sys_path_m.variavel_modulo)

for i in range(10):
    print(i)
    import modulos_sys_path_m  # função reload do importlib para recarregar singleton

print('FIM')

"""
Ao importar um módulo, o mesmo é executado apenas uma vez. 
Para que o módulo possa ser recarregado, é necessário importar
o módulo importlib e chamar a sua função 
importlib.reload(módulo a ser importado), assim, o módulo será
recarregado e executado novamente.

Nesse código, foi importado importlib e o modulos_sys_path_m
a variável de um dos módulos foi exibida
e dentro de um range(10) iterado, a cada volta do laço for
o módulo_sys_path_m foi recarregado através da função
importlib.reload(), até o último valor de range(10) que é 9,
e finalizado com print('FIM')



"""