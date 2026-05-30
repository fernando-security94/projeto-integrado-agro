import sys  

class Grafo: 
    def __init__(self, vertices): 
        """
        Inicializa o grafo como uma matriz de adjacência.
        :param vertices: número de vértices do grafo
        """
        self.V = vertices 
        self.grafo = [[0] * vertices for _ in range(vertices)] 

    def distancia_minima(self, distancias, visitados): 
        """
        Retorna o vértice com a menor distância ainda não visitado.
        :param distancias: lista de distâncias conhecidas até agora
        :param visitados: lista de vértices já processados
        """
        minimo = sys.maxsize 
        vertice_minimo = -1

        for v in range(self.V): 
            if distancias[v] < minimo and not visitados[v]: 
                minimo = distancias[v] 
                vertice_minimo = v 
        return vertice_minimo 

    def imprimir_caminho(self, antecessores, j): 
        """
        Imprime o caminho reconstruído a partir da lista de antecessores.
        :param antecessores: lista que guarda o vértice anterior no caminho
        :param j: vértice final
        """
        if antecessores[j] == -1: 
            print(j, end="")  # vértice inicial
            return 
        self.imprimir_caminho(antecessores, antecessores[j]) 
        print(f" -> {j}", end="")  # caminho passo a passo

    def dijkstra(self, origem): 
        """
        Implementa o algoritmo de Dijkstra.
        :param origem: vértice de partida
        """
        distancias = [sys.maxsize] * self.V 
        distancias[origem] = 0 
        visitados = [False] * self.V 
        antecessores = [-1] * self.V 

        for _ in range(self.V): 
            u = self.distancia_minima(distancias, visitados) 
            if u == -1:  # Caso de grafo desconexo
                break
            visitados[u] = True 

            # Atualiza distâncias dos vizinhos de u
            for v in range(self.V): 
                if (self.grafo[u][v] > 0 and not visitados[v] 
                    and distancias[v] > distancias[u] + self.grafo[u][v]): 
                    distancias[v] = distancias[u] + self.grafo[u][v] 
                    antecessores[v] = u 

        # Exibe resultados
        print("Vértice\tDistância\tCaminho")
        for i in range(self.V): 
            print(f"{i}\t{distancias[i]}\t\t", end="") 
            self.imprimir_caminho(antecessores, i) 
            print()


# =====================
# TESTES DO ALGORITMO
# =====================
if __name__ == "__main__":
    g = Grafo(5)
    
    # Definição da matriz de adjacência
    # Exemplo: grafo não direcionado
    g.grafo = [
        [0, 10, 0, 30, 100],
        [10, 0, 50, 0, 0],
        [0, 50, 0, 20, 10],
        [30, 0, 20, 0, 60],
        [100, 0, 10, 60, 0]
    ]

    print("Resultado do Algoritmo de Dijkstra (origem = 0):")
    g.dijkstra(0)
