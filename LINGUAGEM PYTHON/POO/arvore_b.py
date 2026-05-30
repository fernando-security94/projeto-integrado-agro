"""\
Árvore B (B-tree) para anotações paginadas
-------------------------------------------------
Este arquivo implementa uma Árvore B com:
- Inserção (com divisão de nós/split)
- Busca/consulta por (página, parágrafo)
- Percurso em-ordem (listar anotações ordenadas)
- Visualização com Graphviz (cores por nível)

Grau mínimo t >= 2 (padrão acadêmico).
Cada nó (exceto a raiz) mantém entre t-1 e 2t-1 chaves; a raiz pode ter menos.
Um nó com k chaves tem k+1 filhos. Todas as folhas ficam na mesma profundidade.

Execução (exemplo):
    python b_tree.py
Requisitos para visualizar:
    pip install graphviz
    # No Windows, instale também o Graphviz "dot" e deixe-o no PATH.
"""

from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from typing import List, Optional, Tuple

try:
    from graphviz import Digraph
    _GRAPHVIZ_OK = True
except Exception:
    # Se a lib Python não estiver disponível, ainda dá para usar a árvore sem visualizar
    _GRAPHVIZ_OK = False


# ------------------------------------------------------------
# Modelo de dado (Anotação)
# ------------------------------------------------------------
@dataclass(order=True)
class Anotacao:
    """Anotação associada a (página, parágrafo) com um texto.
       A tupla (pagina, paragrafo) é usada como chave de ordenação lexicográfica.
    """
    pagina: int
    paragrafo: int
    texto: str

    @property
    def chave(self) -> Tuple[int, int]:
        return (self.pagina, self.paragrafo)

    def __repr__(self) -> str:  # ajuda no debug/logs
        return f"Anotacao{self.chave!r}"


# ------------------------------------------------------------
# Nó da Árvore B
# ------------------------------------------------------------
class NodoB:
    """Nó de Árvore B.

    Atributos:
        t       : grau mínimo (t >= 2)
        chaves  : lista de Anotacao (ordenada por .chave)
        filhos  : lista de NodoB (len = len(chaves) + 1 para nós internos)
        folha   : True se nó folha (sem filhos)
    """
    def __init__(self, t: int) -> None:
        self.t: int = t
        self.chaves: List[Anotacao] = []
        self.filhos: List[NodoB] = []
        self.folha: bool = True

    @property
    def cheio(self) -> bool:
        """Retorna True se o nó está cheio (precisa ser dividido antes de descer)."""
        return len(self.chaves) == 2 * self.t - 1


# ------------------------------------------------------------
# Árvore B (inserção, busca, listagem e visualização)
# ------------------------------------------------------------
class ArvoreB:
    def __init__(self, t: int) -> None:
        assert t >= 2, "O grau mínimo t deve ser >= 2"
        self.t: int = t
        self.raiz: NodoB = NodoB(t)
        self.raiz.folha = True

    # ------------------------
    # Busca / Consultar
    # ------------------------
    def consultar(self, pagina: int, paragrafo: int) -> Optional[Anotacao]:
        """Retorna a anotação com (pagina, paragrafo), se existir; senão, None."""
        chave = (pagina, paragrafo)
        return self._buscar(self.raiz, chave)

    def _buscar(self, no: NodoB, chave: Tuple[int, int]) -> Optional[Anotacao]:
        """Busca recursiva em nó de Árvore B.
        Passos:
          1) Encontra o menor índice i tal que chave <= no.chaves[i].chave.
          2) Se chave == no.chaves[i].chave, achou.
          3) Se folha, não achou.
          4) Caso contrário, desce para o filho i.
        """
        i = 0
        # Procura posição onde a chave deveria estar
        while i < len(no.chaves) and chave > no.chaves[i].chave:
            i += 1
        # Verifica igualdade
        if i < len(no.chaves) and chave == no.chaves[i].chave:
            return no.chaves[i]
        # Se é folha, acabou
        if no.folha:
            return None
        # Senão, desce para o filho adequado
        return self._buscar(no.filhos[i], chave)

    # ------------------------
    # Inserção (top-down)
    # ------------------------
    def inserir(self, anotacao: Anotacao) -> None:
        """Insere uma nova anotação na Árvore B.
        Estratégia top-down: se a raiz estiver cheia, cria uma nova raiz,
        faz split e então insere no caminho garantindo que só descemos para nós não cheios.
        """
        r = self.raiz
        if r.cheio:
            # Raiz cheia -> aumenta a altura
            s = NodoB(self.t)
            s.folha = False
            s.filhos = [r]
            self._split_child(s, 0)  # divide antigo filho 0 (a antiga raiz)
            self.raiz = s
            self._insert_nonfull(s, anotacao)
        else:
            self._insert_nonfull(r, anotacao)

    def _split_child(self, x: NodoB, i: int) -> None:
        """Divide o filho cheio y = x.filhos[i] em dois nós (y e z) e promove a mediana para x.
        Passo a passo:
          1) Cria z com o mesmo t e folha = y.folha.
          2) Move as últimas (t-1) chaves de y para z; mantém as primeiras (t-1) em y.
          3) Se não folha, move também os últimos t filhos de y para z.
          4) Promove a mediana (chave no índice t-1 de y original) para x em posição i.
          5) Insere z como novo filho de x na posição i+1.
        """
        t = self.t
        y = x.filhos[i]
        z = NodoB(t)
        z.folha = y.folha

        # Captura a mediana ANTES de fatiar
        mediana = y.chaves[t - 1]

        # Chaves: y fica com as t-1 primeiras; z recebe as t-1 últimas
        z.chaves = y.chaves[t:]
        y.chaves = y.chaves[: t - 1]

        # Filhos: se não folha, divide a lista de filhos
        if not y.folha:
            z.filhos = y.filhos[t:]
            y.filhos = y.filhos[:t]

        # Insere mediana e novo filho no pai x
        x.chaves.insert(i, mediana)
        x.filhos.insert(i + 1, z)

    def _insert_nonfull(self, x: NodoB, anotacao: Anotacao) -> None:
        """Insere anotação em um nó garantidamente não cheio.
        Se for folha, insere na posição ordenada.
        Se for interno, escolhe o filho adequado; se o filho estiver cheio, faz split antes de descer.
        """
        i = len(x.chaves) - 1
        if x.folha:
            # Encontra a posição correta (varrendo de trás para frente)
            while i >= 0 and anotacao.chave < x.chaves[i].chave:
                i -= 1
            x.chaves.insert(i + 1, anotacao)
        else:
            # Decide para qual filho descer
            while i >= 0 and anotacao.chave < x.chaves[i].chave:
                i -= 1
            i += 1
            # Se o filho alvo está cheio, divide antes de descer
            if x.filhos[i].cheio:
                self._split_child(x, i)
                # Após o split, a chave promovida está em x.chaves[i]
                # Precisamos decidir se descemos para o filho i ou i+1
                if anotacao.chave > x.chaves[i].chave:
                    i += 1
            self._insert_nonfull(x.filhos[i], anotacao)

    # ------------------------
    # Percurso em ordem (listar)
    # ------------------------
    def listar_anotacoes(self) -> List[Anotacao]:
        """Retorna todas as anotações em ordem crescente por (página, parágrafo)."""
        saida: List[Anotacao] = []
        self._em_ordem(self.raiz, saida)
        return saida

    def _em_ordem(self, no: NodoB, saida: List[Anotacao]) -> None:
        if no.folha:
            # Folha: só despeja as chaves
            saida.extend(no.chaves)
        else:
            # Interno: filho, chave, filho, chave, ..., último filho
            for i, chave in enumerate(no.chaves):
                self._em_ordem(no.filhos[i], saida)
                saida.append(chave)
            self._em_ordem(no.filhos[-1], saida)

    # ------------------------
    # Visualização com Graphviz
    # ------------------------
    def visualizar(self, nome_arquivo: str = "arvore_b", formato: str = "png") -> Optional[str]:
        """Gera uma imagem (PNG/PDF/SVG) com a estrutura da Árvore B.
        - Usa um BFS para percorrer os níveis e aplica cores diferentes por nível.
        - Cada nó aparece como um "record" com suas chaves.
        Retorna o caminho do arquivo gerado, se Graphviz estiver disponível.
        """
        if not _GRAPHVIZ_OK:
            print("[visualizar] graphviz não disponível no ambiente Python.")
            return None

        paleta = [
            "#BBDEFB",  # nível 0
            "#C8E6C9",  # nível 1
            "#FFE0B2",  # nível 2
            "#D1C4E9",  # nível 3
            "#FFCDD2",  # nível 4
            "#B2DFDB",  # nível 5
        ]

        dot = Digraph(comment="Árvore B")
        dot.attr(rankdir="TB")  # Top-to-Bottom
        dot.attr("node", shape="record", style="rounded,filled", fontname="Helvetica", fontsize="11")

        fila: deque[tuple[NodoB, int]] = deque([(self.raiz, 0)])
        vistos = set()

        def rotulo(no: NodoB) -> str:
            if not no.chaves:
                return "{}"  # nó vazio (pouco comum, mas pode acontecer em raiz inicial)
            # Exibe cada chave como (p, q)
            partes = [f"({a.pagina}, {a.paragrafo})" for a in no.chaves]
            return "{" + " | ".join(partes) + "}"

        while fila:
            no, nivel = fila.popleft()
            node_id = str(id(no))
            if node_id in vistos:
                continue
            vistos.add(node_id)

            cor = paleta[nivel % len(paleta)]
            dot.node(node_id, rotulo(no), fillcolor=cor)

            if not no.folha:
                for filho in no.filhos:
                    filho_id = str(id(filho))
                    dot.edge(node_id, filho_id)
                    fila.append((filho, nivel + 1))

        caminho = dot.render(filename=nome_arquivo, format=formato, cleanup=True)
        return caminho


# ------------------------------------------------------------
# Demonstração básica (insere, consulta, lista, visualiza)
# ------------------------------------------------------------
if __name__ == "__main__":
    # 1) Cria a árvore com grau mínimo t=2
    arvore = ArvoreB(t=2)

    # 2) Insere anotações suficientes para provocar splits
    dados_demo = [
        (1, 1, "Introdução"),
        (1, 2, "Definição"),
        (1, 3, "Conceitos"),
        (2, 1, "Exemplo"),
        (2, 2, "Teorema"),
        (3, 1, "Prova"),
        (4, 1, "Observação"),
        (5, 1, "Resumo"),
    ]
    for p, q, txt in dados_demo:
        arvore.inserir(Anotacao(p, q, txt))

    # 3) Consultas
    achou = arvore.consultar(2, 2)
    print("Consulta (2,2):", achou)
    nao_achou = arvore.consultar(9, 9)
    print("Consulta (9,9):", nao_achou)

    # 4) Listagem em ordem
    print("\nAnotações em ordem:")
    print([a.chave for a in arvore.listar_anotacoes()])

    # 5) Visualização (se Graphviz Python + executável 'dot' estiverem OK)
    caminho = arvore.visualizar("arvore_b_exemplo", formato="png")
    if caminho:
        print(f"\nFigura gerada: {caminho}")
    else:
        print("\nVisualização não gerada (biblioteca graphviz indisponível neste ambiente).")
