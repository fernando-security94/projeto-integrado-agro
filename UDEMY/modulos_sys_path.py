"""
Entendendo os seus próprios módulos Python;
- O primeiro módulo executado chama-se __main__;
- É possível importar outro módulo inteiro ou por partes;
- O Python conhece a pasta onde o __main__ está e as pastas
abaixo dele;
- O programa não reconhece pastas e módulos acima do __main__ por padrão.
- O Python conhece todos os módulos e pacotes presentes nos caminhos
de sys.path

"""

import sys
import modulos_sys_path_m
from modulos_sys_path_m import soma, variavel_modulo 


print('Este módulo se chama', __name__)
print(modulos_sys_path_m.variavel_modulo)
print(variavel_modulo.upper())
print(modulos_sys_path_m.soma(9, 100))
print(soma(9, 100))

print()

print(*sys.path, sep='\n')


"""
A importação de módulos é utilizada para que seu programa possa
ser dividido em arquivos diferentes, facilitando assim a sua manipulação.

Nesse caso o mesmo módulo foi importado de duas formas diferentes, a primeira, 
foi importado inteiro: import modulos_sys_path_m e para chamar algum objeto
específico desse módulo, será o nome_do_modulo.objeto: modulos_sys_path_m.variavel_modulo,
que é "Hello World".

A segunda forma foi em partes, sendo apenas objetos ou funções específicas que queira usar:
from modulos_sys_path_m import soma, variavel_modulo, e para executar, chamar
diretamente pelo nome: print(variável_modulo) que é "Hello World" e também a função soma()
print(soma(9, 100)) que é 109.

O módulo sys é utilizado de forma para acessar endereços dos programas no desktop,
na memória e manipulação do sistema em si.

print(*sys.path, sep='\') , nesse caso, sys mostrará o caminho percorrido para a fonte do arquivo.py
que está sendo manipulado.


"""