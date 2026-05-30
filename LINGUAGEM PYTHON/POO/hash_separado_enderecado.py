# ===============================
# Exemplo de Tabela Hash em Python
# Comparando:
#   1) Encadeamento Separado
#   2) Endereçamento Aberto (Linear Probing)
# ===============================

# -------------------------------
# Função Hash (método da divisão)
# -------------------------------
def hash_function(valor, m):
    return valor % m


# -------------------------------
# 1) Tabela Hash com Encadeamento Separado
# -------------------------------
class HashTableEncadeada:
    def __init__(self, m):
        self.m = m
        self.tabela = [[] for _ in range(m)]  # cada bucket é uma lista

    def inserir(self, valor):
        indice = hash_function(valor, self.m)
        self.tabela[indice].append(valor)  # se já existir algo, apenas empilha

    def __str__(self):
        return "\n".join([f"{i}: {bucket}" for i, bucket in enumerate(self.tabela)])


# -------------------------------
# 2) Tabela Hash com Endereçamento Aberto (Linear Probing)
# -------------------------------
class HashTableLinear:
    def __init__(self, m):
        self.m = m
        self.tabela = [None] * m  # cada bucket começa vazio

    def inserir(self, valor):
        indice = hash_function(valor, self.m)

        # Se o espaço já está ocupado, procuramos o próximo
        passos = 0
        while self.tabela[indice] is not None:
            passos += 1
            indice = (indice + 1) % self.m  # move para o próximo índice
            if passos >= self.m:
                raise Exception("Tabela Hash está cheia!")

        self.tabela[indice] = valor

    def __str__(self):
        return "\n".join([f"{i}: {self.tabela[i]}" for i in range(self.m)])


# -------------------------------
# Testes práticos
# -------------------------------
if __name__ == "__main__":
    valores = [235, 578, 1024, 96, 32, 18]  # 18 colide com 578

    print("===== Encadeamento Separado =====")
    hash_encadeada = HashTableEncadeada(m=10)
    for v in valores:
        hash_encadeada.inserir(v)
    print(hash_encadeada)

    print("\n===== Endereçamento Aberto (Linear Probing) =====")
    hash_linear = HashTableLinear(m=10)
    for v in valores:
        hash_linear.inserir(v)
    print(hash_linear)
