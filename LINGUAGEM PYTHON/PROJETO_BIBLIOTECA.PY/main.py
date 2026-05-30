# Arquivo controlador do sistema e funções
# de acordo com as escolhas do usuario

from interface import interface_principal
from sistema_biblioteca import criar_tabelas

if __name__ == "__main__":
    criar_tabelas()  # criará as tabelas automaticamente caso nao existam
    interface_principal() # inicia a interface do sistema
    