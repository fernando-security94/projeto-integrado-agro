import networkx as nx
import matplotlib.pyplot as plt

def criar_rede_viaria():
    """
    Cria um grafo direcionado representando a rede viária urbana.
    Cada nó = interseção.
    Cada aresta = via entre interseções (com direção e peso = distância).
    """
    G = nx.DiGraph()

    # Adicionando arestas (via: de -> para, distância em km)
    G.add_edge("A", "B", peso=2)
    G.add_edge("B", "C", peso=3)
    G.add_edge("C", "D", peso=2)
    G.add_edge("A", "D", peso=10)
    G.add_edge("B", "E", peso=4)
    G.add_edge("E", "D", peso=1)
    G.add_edge("C", "E", peso=2)

    return G


def bloquear_via(G, origem, destino, bloqueadas):
    """
    Bloqueia uma via removendo a aresta correspondente
    e registra no conjunto de bloqueadas.
    """
    if G.has_edge(origem, destino):
        G.remove_edge(origem, destino)
        bloqueadas.add((origem, destino))
        print(f"🚧 Via bloqueada: {origem} -> {destino}")
    else:
        print(f"⚠️ Via {origem} -> {destino} não existe ou já está bloqueada.")


def rota_disponivel(G, origem, destino):
    """
    Verifica se existe algum caminho alternativo entre dois pontos,
    considerando as restrições de direção e bloqueios.
    """
    try:
        caminho = nx.shortest_path(G, source=origem, target=destino, weight="peso")
        distancia = nx.shortest_path_length(G, source=origem, target=destino, weight="peso")
        return caminho, distancia
    except nx.NetworkXNoPath:
        return None, None


def desenhar_grafo(G, bloqueadas=None, caminho=None):
    """
    Desenha o grafo com matplotlib.
    - Vias normais = cinza
    - Vias bloqueadas = vermelho
    - Caminho encontrado = verde
    """
    pos = nx.spring_layout(G, seed=42)  # Layout para organizar os nós
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

    # Todas as arestas que sobraram no grafo
    todas_arestas = list(G.edges())

    # Define arestas do caminho em verde
    caminho_arestas = []
    if caminho and len(caminho) > 1:
        caminho_arestas = [(caminho[i], caminho[i+1]) for i in range(len(caminho)-1)]

    # Desenhar arestas normais em cinza
    nx.draw_networkx_edges(G, pos, edgelist=todas_arestas, edge_color="gray", arrows=True)

    # Desenhar arestas do caminho em verde
    if caminho_arestas:
        nx.draw_networkx_edges(G, pos, edgelist=caminho_arestas, edge_color="green", width=2.5, arrows=True)

    # Desenhar arestas bloqueadas em vermelho
    if bloqueadas:
        nx.draw_networkx_edges(G, pos, edgelist=list(bloqueadas), edge_color="red", style="dashed", width=2, arrows=True)

    # Exibir pesos (distâncias)
    labels = nx.get_edge_attributes(G, 'peso')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Rede Viária - Rotas e Bloqueios")
    plt.axis("off")
    plt.show()


# =====================================
# Simulação do problema
# =====================================
if __name__ == "__main__":
    G = criar_rede_viaria()
    bloqueadas = set()

    origem, destino = "A", "D"

    # Rota inicial
    caminho, dist = rota_disponivel(G, origem, destino)
    print(f"\nMelhor rota de {origem} até {destino}: {caminho} (distância = {dist} km)")
    desenhar_grafo(G, bloqueadas, caminho)

    # Bloqueando uma via
    bloquear_via(G, "B", "C", bloqueadas)
    caminho, dist = rota_disponivel(G, origem, destino)
    print(f"\nRota após bloqueio: {caminho} (distância = {dist} km)")
    desenhar_grafo(G, bloqueadas, caminho)

    # Bloqueando outra via
    bloquear_via(G, "E", "D", bloqueadas)
    caminho, dist = rota_disponivel(G, origem, destino)
    if caminho:
        print(f"\nRota alternativa ainda disponível: {caminho} (distância = {dist} km)")
    else:
        print("\nNenhuma rota alternativa disponível!")
    desenhar_grafo(G, bloqueadas, caminho)

