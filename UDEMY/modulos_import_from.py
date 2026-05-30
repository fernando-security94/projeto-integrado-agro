"""
Import, from as e *

"""

"""
Importar módulos inteiros 

import nome_modulo
Vantagens: Ter o namespace do módulo
Desvantagens: Nomes grandes

Importar módulo em partes 

from nome_modulo import objeto1, objeto2
Vantagens: nomes pequenos
Desvantagens: Sem namespace do módulo

Importar modulo com alias - as
from nome_modulo import objeto1 as apelido
Vantagens: Você pode reservar nomes para o código
Desvantagens: Pode ficar fora do padrão da linguagem

Má pratica de importação de módulo

from nome_modulo import *
Vantagens: Importa tudo do módulo
Desvantagens: Importa tudo do módulo

"""

print('Este módulo se chama', __name__)