'''
🔎 Como funciona esse ajuste:

Cada produto é categorizado de acordo com etiqueta % 15.

Ex: 101 % 15 = 11 → produto vai para a classe 11.

202 % 15 = 7 → produto vai para a classe 7.

Colisões são tratadas naturalmente:

Se outro produto cai na mesma classe, apenas incrementamos a contagem.

Isso é útil porque estamos classificando grupos, não armazenando itens individualmente.

Testes incluídos:

Vários produtos são inseridos automaticamente.

Depois consultamos algumas classes para verificar a contagem.

'''

# ==============================================
# Script de Tabela Hash para Categorização de Produtos
# ==============================================

# Importa a biblioteca array para manipular arrays fixos de inteiros
import array as arr

# Número de classes de produtos (buckets da tabela hash)
m = 15  

# Inicializa a tabela hash como um array de inteiros com m posições
# Cada posição inicia com 0 (nenhum produto categorizado ainda)
hashtable = arr.array('i', [0] * m)

# ------------------------------
# Função hash
# ------------------------------
def hashfunct(v, mh):
    """
    Aplica o método da divisão para encontrar a posição de um produto na tabela hash.
    v : código ou etiqueta do produto (int)
    mh: número de classes da tabela hash (int)
    """
    return v % mh  

# ------------------------------
# Inserção de produto
# ------------------------------
def insereTC(valor):
    """
    Insere (ou incrementa) um produto em sua classe correspondente na tabela hash.
    """
    indice = hashfunct(valor, m)  # Calcula o índice com base na etiqueta
    hashtable[indice] += 1        # Incrementa a contagem da classe
    print(f"Produto {valor} categorizado na classe {indice}.")

# ------------------------------
# Consulta de quantidade por classe
# ------------------------------
def retornaV(valor):
    """
    Retorna a quantidade de produtos de uma determinada classe.
    """
    indice = hashfunct(valor, m)
    return hashtable[indice]

# ------------------------------
# Exibição formatada da tabela hash
# ------------------------------
def exibir_tabela():
    """
    Exibe o estado atual da tabela hash de forma organizada.
    """
    print("\nEstado atual da Tabela Hash:")
    for i, qtd in enumerate(hashtable):
        print(f"Classe {i:2}: {qtd} produto(s)")
    print("-" * 30)

# ==============================================
# Testes práticos
# ==============================================

print("Tabela Hash inicial:")
exibir_tabela()

# Inserindo alguns produtos simulados
produtos = [101, 202, 305, 410, 512, 678, 890, 999, 45, 60, 75, 150, 225, 330]

for p in produtos:
    insereTC(p)

# Exibe tabela após inserções
exibir_tabela()

# Consultando quantos produtos existem em algumas classes específicas
consultas = [101, 202, 305, 410, 512]

print("\nConsultas por classe:")
for c in consultas:
    print(f"Classe {hashfunct(c, m)} contém {retornaV(c)} produto(s).")
