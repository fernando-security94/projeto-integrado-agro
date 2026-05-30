class Grafo:
    def __init__(self, vertices):
        """
        Inicializa o grafo.

        Parâmetros:
            vertices (int): número total de vértices no grafo.
        """
        self.V = vertices               # Número de vértices
        self.grafo = []                 # Lista de arestas (u, v, peso)

    def adicionar_aresta(self, u, v, w):
        """
        Adiciona uma aresta ao grafo.

        Parâmetros:
            u (int): vértice de origem
            v (int): vértice de destino
            w (int): peso da aresta
        """
        self.grafo.append([u, v, w])

    def encontrar(self, pai, i):
        """
        Função de busca do representante de um subconjunto (Union-Find com compressão de caminho).
        """
        if pai[i] != i:
            pai[i] = self.encontrar(pai, pai[i])
        return pai[i]

    def unir(self, pai, rank, x, y):
        """
        Realiza a união de dois subconjuntos pelo rank (Union by Rank).
        """
        raiz_x = self.encontrar(pai, x)
        raiz_y = self.encontrar(pai, y)

        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def kruskal(self):
        """
        Executa o algoritmo de Kruskal e retorna a Árvore Geradora Mínima (MST).
        """
        resultado = []  # Lista que guardará as arestas da MST
        i, e = 0, 0     # i = índice das arestas ordenadas, e = número de arestas na MST

        # Ordena todas as arestas em ordem crescente de peso
        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        pai = [i for i in range(self.V)]   # Inicializa cada vértice como seu próprio pai
        rank = [0] * self.V                # Inicializa os ranks com zero

        # Continuamos até obter V-1 arestas
        while e < self.V - 1 and i < len(self.grafo):
            u, v, w = self.grafo[i]
            i += 1

            x = self.encontrar(pai, u)
            y = self.encontrar(pai, v)

            # Se não formar ciclo, adiciona na MST
            if x != y:
                e += 1
                resultado.append([u, v, w])
                self.unir(pai, rank, x, y)

        return resultado


# =============================
# Testes
# =============================
if __name__ == "__main__":
    # Grafo de exemplo
    g = Grafo(4)
    g.adicionar_aresta(0, 1, 10)
    g.adicionar_aresta(0, 2, 6)
    g.adicionar_aresta(0, 3, 5)
    g.adicionar_aresta(1, 3, 15)
    g.adicionar_aresta(2, 3, 4)

    mst = g.kruskal()
    print("🌐 Arestas na Árvore Geradora Mínima (MST):")
    for u, v, peso in mst:
        print(f"{u} -- {v} == {peso}")

    # Teste esperado: MST com arestas (2-3, 0-3, 0-1) com pesos 4, 5 e 10
    esperado = sorted([[2, 3, 4], [0, 3, 5], [0, 1, 10]])
    assert sorted(mst) == esperado, "❌ Erro: MST não corresponde ao esperado!"

    print("\n✅ Teste passou! MST gerada corretamente.")


'''
No método kruskal(), as arestas são ordenadas por peso e, em seguida, 
são adicionadas ao resultado se não formarem um ciclo. 

Os métodos encontrar() e unir() são usados para encontrar o representante 
de um subconjunto e para unir dois subconjuntos, respectivamente. 

O método adicionar_aresta() é utilizado para adicionar uma aresta ao grafo. 

O código de exemplo cria um grafo com 4 vértices e 5 arestas e 
executa o algoritmo de Kruskal sobre ele, imprimindo as arestas selecionadas 
para a árvore de spanning mínima (Alves, 2021). 




'''