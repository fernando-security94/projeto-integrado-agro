from collections import deque

def bfs(graph, start):
    """
    Executa a busca em largura (BFS - Breadth-First Search) em um grafo.

    Parâmetros:
        graph (dict): Grafo representado como um dicionário de listas de adjacência.
        start (str): Vértice inicial para começar a busca.

    Retorna:
        ordem_visita (list): Lista com a ordem dos vértices visitados.
    """
    visited = set()          # Conjunto para armazenar os nós já visitados (evita repetição)
    queue = deque([start])   # Fila de exploração, começando pelo nó inicial
    ordem_visita = []        # Lista para registrar a ordem de visita

    while queue:  # Enquanto houver elementos na fila
        vertex = queue.popleft()  # Remove o primeiro elemento da fila (FIFO)

        if vertex not in visited:      # Se ainda não foi visitado
            visited.add(vertex)        # Marca o nó como visitado
            ordem_visita.append(vertex)  # Registra a visita

            # Adiciona os vizinhos do vértice atual que ainda não foram visitados
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return ordem_visita


# =============================
# Exemplo de uso
# =============================
if __name__ == "__main__":
    # Grafo representado como dicionário de listas de adjacência
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    resultado = bfs(graph, 'A')
    print("Ordem de visita:", resultado)  
    # Esperado: ['A', 'B', 'C', 'D', 'E', 'F']


    # =============================
    # Testes Simples
    # =============================
    def test_bfs():
        assert bfs(graph, 'A') == ['A', 'B', 'C', 'D', 'E', 'F']
        assert bfs(graph, 'B') == ['B', 'A', 'D', 'E', 'C', 'F']
        assert bfs(graph, 'C') == ['C', 'A', 'F', 'B', 'E', 'D']
        print("✅ Todos os testes passaram!")

    test_bfs()
