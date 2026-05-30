# ======================================================
# Implementação de uma Tabela Hash com tratamento de colisões
# usando o método de encadeamento separado (listas em cada bucket)
# ======================================================

# Parte 1: Inicialização da tabela hash como um dicionário vazio
hashtable = {}

m = 10  # Define o número de índices (ou 'buckets') na tabela hash


# Parte 2: Definição da função hash
def hashfunct(v, mh):
    """
    Calcula o índice (bucket) de armazenamento a partir do valor.
    Usa o método da divisão.
    :param v: valor a ser armazenado
    :param mh: tamanho da tabela hash
    :return: índice calculado
    """
    return v % mh


# Parte 3: Inicialização da tabela hash com listas vazias (encadeamento)
for i in range(m):
    hashtable[i] = []  # Cada bucket é uma lista, permitindo armazenar múltiplos valores em caso de colisão


# Parte 4: Inserção de valores na tabela hash
def insert(value):
    """
    Insere um valor na tabela hash com tratamento de colisões.
    :param value: valor inteiro a ser inserido
    """
    index = hashfunct(value, m)  # calcula o índice
    if value not in hashtable[index]:  # evita duplicatas
        hashtable[index].append(value)  # adiciona o valor na lista (encadeamento)


# Parte 5: Busca de valores na tabela hash
def search(value):
    """
    Busca um valor na tabela hash.
    :param value: valor inteiro a ser buscado
    :return: True se encontrado, False caso contrário
    """
    index = hashfunct(value, m)
    return value in hashtable[index]


# Parte 6: Testes práticos
# Inserindo valores
insert(235)
insert(578)
insert(1024)
insert(96)
insert(32)

print("📌 Estado da tabela hash após inserções iniciais:")
print(hashtable)

# Inserção de um valor que gera colisão (18 % 10 = 8, mesmo bucket que 578 e 1024)
insert(18)

print("\n📌 Estado da tabela hash após inserção de 18 (colisão tratada):")
print(hashtable)

# Testando buscas
print("\n🔎 Testes de busca:")
print("235 encontrado?", search(235))  # True
print("18 encontrado?", search(18))    # True
print("999 encontrado?", search(999))  # False
