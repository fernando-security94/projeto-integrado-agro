'''
O que este script entrega

Graph + dijkstra (com reconstrução de caminho).

metric_closure: calcula distâncias mínimas entre cidades com Dijkstra (base para TSP em redes esparsas).

tsp_nearest_neighbor: heurística simples para obter um circuito.

tour_cost: custo do circuito.

expand_tour_on_network: expande cada aresta do circuito (entre cidades) para o caminho real na rede (útil quando há nós-interseção).

Testes com unittest cobrindo Dijkstra, fecho métrico, TSP e expansão de caminhos.


'''

from __future__ import annotations
from typing import Dict, List, Tuple, Iterable, Optional
from heapq import heappush, heappop
import math
import unittest


class Graph:
    """
    Grafo ponderado (por padrão, não-direcionado) representado por lista de adjacência.
    Cada aresta tem peso não-negativo (pré-requisito para Dijkstra).
    """
    def __init__(self, directed: bool = False):
        self.adj: Dict[str, List[Tuple[str, float]]] = {}
        self.directed = directed



    def add_node(self, u: str) -> None:
        self.adj.setdefault(u, [])

    def add_edge(self, u: str, v: str, w: float) -> None:
        """
        Adiciona aresta u->v com peso w. Se o grafo não for direcionado, adiciona v->u também.
        """
        if w < 0:
            raise ValueError("Dijkstra requer pesos não-negativos.")
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))


    @property
    def nodes(self) -> List[str]:
        return list(self.adj.keys())

    def neighbors(self, u: str) -> Iterable[Tuple[str, float]]:
        return self.adj.get(u, [])


def dijkstra(g: Graph, source: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
    """
    Dijkstra clássico: retorna distâncias mínimas a partir de 'source' e predecessores para reconstrução de caminho.
    """
    dist = {u: math.inf for u in g.nodes}
    prev: Dict[str, Optional[str]] = {u: None for u in g.nodes}
    dist[source] = 0.0

    pq: List[Tuple[float, str]] = [(0.0, source)]
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue  # entrada desatualizada na heap
        for v, w in g.neighbors(u):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heappush(pq, (nd, v))
    return dist, prev


def metric_closure(g: Graph, cities: Optional[Iterable[str]] = None) -> Tuple[Dict[str, Dict[str, float]], Dict[str, Dict[str, Optional[str]]]]:
    """
    Calcula o 'fecho métrico' entre um subconjunto de nós (cities).
    Para cada cidade s, roda Dijkstra e armazena distâncias para todas as outras cidades.
    Retorna:
      - dist[s][t] = menor distância entre s e t no grafo original
      - prev_map[s] = mapa de predecessores para reconstruir caminhos que saem de s
    """
    if cities is None:
        cities = g.nodes
    cities = list(cities)

    dist_matrix: Dict[str, Dict[str, float]] = {s: {} for s in cities}
    prev_map: Dict[str, Dict[str, Optional[str]]] = {}

    for s in cities:
        dist, prev = dijkstra(g, s)
        prev_map[s] = prev
        for t in cities:
            dist_matrix[s][t] = dist[t]
            if dist[t] == math.inf:
                raise ValueError(f"Não há caminho entre '{s}' e '{t}'. O TSP exige conectividade.")
    return dist_matrix, prev_map


def tsp_nearest_neighbor(dist: Dict[str, Dict[str, float]], start: str) -> List[str]:
    """
    Heurística do Vizinho Mais Próximo (Nearest Neighbor) sobre a matriz de distâncias.
    Gera um circuito iniciando em 'start' e retornando a 'start'.
    """
    cities = list(dist.keys())
    if start not in cities:
        raise ValueError("Cidade inicial não está na matriz de distâncias.")

    unvisited = set(cities)
    unvisited.remove(start)
    tour = [start]
    current = start

    while unvisited:
        nxt = min(unvisited, key=lambda c: dist[current][c])
        tour.append(nxt)
        unvisited.remove(nxt)
        current = nxt

    tour.append(start)  # fecha o circuito
    return tour


def tour_cost(tour: List[str], dist: Dict[str, Dict[str, float]]) -> float:
    """
    Soma os custos ao longo do circuito (A->...->A) usando a matriz de distâncias.
    """
    return sum(dist[u][v] for u, v in zip(tour, tour[1:]))


def reconstruct_segment(prev_map_from_source: Dict[str, Optional[str]], s: str, t: str) -> List[str]:
    """
    Reconstrói o caminho no grafo original do segmento s->t usando o mapa de predecessores calculado a partir de s.
    (Caminho em ordem s ... t). Lança erro se t não for alcançável.
    """
    path = [t]
    cur = t
    while cur != s:
        cur = prev_map_from_source.get(cur)
        if cur is None:
            raise ValueError(f"Sem caminho de {s} para {t} ao reconstruir.")
        path.append(cur)
    path.reverse()
    return path


def expand_tour_on_network(tour: List[str], prev_map: Dict[str, Dict[str, Optional[str]]]) -> List[str]:
    """
    Expande o circuito de cidades para a sequência de vértices do grafo original (incluindo interseções).
    Concatena os segmentos s->t reconstruídos com Dijkstra (de cada s no circuito).
    """
    full_path: List[str] = []
    for s, t in zip(tour, tour[1:]):
        seg = reconstruct_segment(prev_map[s], s, t)
        if full_path:
            # evita duplicar o nó de junção
            full_path.extend(seg[1:])
        else:
            full_path.extend(seg)
    return full_path


# ============================
# Demonstração + Testes
# ============================
class TestDijkstraTSP(unittest.TestCase):
    def setUp(self):
        # Grafo completo com 4 cidades (simétrico e métrico).
        # Distâncias escolhidas para que um circuito ótimo tenha custo 39.
        # A-B=10, B-C=12, C-D=9, D-A=8, A-C=15, B-D=20
        self.G = Graph(directed=False)
        edges = [
            ("A", "B", 10.0),
            ("B", "C", 12.0),
            ("C", "D", 9.0),
            ("D", "A", 8.0),
            ("A", "C", 15.0),
            ("B", "D", 20.0),
        ]
        for u, v, w in edges:
            self.G.add_edge(u, v, w)

    def test_dijkstra_distances(self):
        # Distâncias mínimas saindo de A
        dist, prev = dijkstra(self.G, "A")
        self.assertAlmostEqual(dist["A"], 0.0)
        self.assertAlmostEqual(dist["B"], 10.0)
        # Melhor A->C é direto (15) ou via D (8+9=17); então 15
        self.assertAlmostEqual(dist["C"], 15.0)
        self.assertAlmostEqual(dist["D"], 8.0)
        # Reconstrução A->B
        path = reconstruct_segment(prev, "A", "B")
        self.assertEqual(path, ["A", "B"])

    def test_metric_closure(self):
        dist, prev_map = metric_closure(self.G, ["A", "B", "C", "D"])
        self.assertAlmostEqual(dist["A"]["C"], 15.0)
        self.assertAlmostEqual(dist["B"]["D"], 20.0)
        self.assertIn("C", prev_map)  # temos mapas de predecessores por origem

    def test_tsp_nearest_neighbor_is_optimal_here(self):
        dist, prev_map = metric_closure(self.G, ["A", "B", "C", "D"])
        tour = tsp_nearest_neighbor(dist, start="A")
        cost = tour_cost(tour, dist)
        # Ótimos possíveis: A-B-C-D-A (10+12+9+8=39) ou A-D-C-B-A (8+9+12+10=39)
        self.assertIn(tour, [
            ["A", "B", "C", "D", "A"],
            ["A", "D", "C", "B", "A"],
        ])
        self.assertAlmostEqual(cost, 39.0)

    def test_expand_tour_on_network(self):
        dist, prev_map = metric_closure(self.G, ["A", "B", "C", "D"])
        tour = ["A", "D", "C", "B", "A"]
        network_path = expand_tour_on_network(tour, prev_map)
        # Como é grafo completo, os segmentos são diretos
        self.assertEqual(network_path, ["A", "D", "C", "B", "A"])


if __name__ == "__main__":
    # Execução direta: roda os testes e mostra uma pequena demo.
    print("🧪 Rodando testes...")
    unittest.main(argv=['-v'], exit=False)

    # Demonstração simples
    print("\n=== Demonstração rápida ===")
    G = Graph(directed=False)
    for u, v, w in [
        ("A", "B", 10.0),
        ("B", "C", 12.0),
        ("C", "D", 9.0),
        ("D", "A", 8.0),
        ("A", "C", 15.0),
        ("B", "D", 20.0),
    ]:
        G.add_edge(u, v, w)

    dist, prev_map = metric_closure(G, ["A", "B", "C", "D"])
    tour = tsp_nearest_neighbor(dist, start="A")
    cost = tour_cost(tour, dist)
    print(f"Circuito (vizinho mais próximo): {tour}")
    print(f"Custo total do circuito: {cost}")
