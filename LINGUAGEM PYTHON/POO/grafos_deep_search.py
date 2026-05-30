# Classe Grafo implementando lista de adjacência
class Grafo: 
    def __init__(self): 
        # Dicionário para armazenar os vértices e suas adjacências
        self.vertices = {}  

    def adicionar_vertice(self, vertice): 
        """
        Adiciona um vértice ao grafo.
        Caso já exista, não faz nada.
        """
        if vertice not in self.vertices: 
            self.vertices[vertice] = []  # Inicializa a lista de adjacências vazia

    def adicionar_aresta(self, origem, destino): 
        """
        Adiciona uma aresta direcionada de 'origem' para 'destino'.
        Só funciona se ambos os vértices já existirem.
        """
        if origem in self.vertices and destino in self.vertices: 
            self.vertices[origem].append(destino)  

    def mostrar_vertices(self): 
        """Mostra todos os vértices do grafo"""
        print("\n--- Vértices do Grafo ---")
        for vertice in self.vertices: 
            print(vertice) 

    def mostrar_arestas(self): 
        """Mostra todas as arestas do grafo"""
        print("\n--- Arestas do Grafo ---")
        for origem in self.vertices: 
            for destino in self.vertices[origem]: 
                print(f"{origem} -> {destino}") 

    def __str__(self):
        """
        Representação do grafo em forma de lista de adjacências.
        Ex: A: ['B', 'C']
        """
        return "\n".join(f"{v}: {adj}" for v, adj in self.vertices.items())


# ============================
# TESTES PRÁTICOS
# ============================

# Criando o grafo
grafo = Grafo()

# Adicionando vértices
grafo.adicionar_vertice('A') 
grafo.adicionar_vertice('B') 
grafo.adicionar_vertice('C') 
grafo.adicionar_vertice('D') 

# Adicionando arestas
grafo.adicionar_aresta('A', 'B') 
grafo.adicionar_aresta('A', 'C') 
grafo.adicionar_aresta('B', 'C') 
grafo.adicionar_aresta('C', 'D') 

# Teste 1: Mostrar vértices
grafo.mostrar_vertices()  # Esperado: A, B, C, D

# Teste 2: Mostrar arestas
grafo.mostrar_arestas()  
# Esperado:
# A -> B
# A -> C
# B -> C
# C -> D

# Teste 3: Representação geral
print("\n--- Estrutura do Grafo (lista de adjacências) ---")
print(grafo)
# Esperado:
# A: ['B', 'C']
# B: ['C']
# C: ['D']
# D: []
