# avl_tree.py

import matplotlib.pyplot as plt
import networkx as nx

class VerticeAVL:
    """
    Vértice de uma árvore AVL.
    Contém métodos para inserir, remover, balancear e rotacionar.
    """
    def __init__(self, chave, pai=None):
        self.chave = chave
        self.pai = pai
        self.esquerdo = None
        self.direito = None
        self._altura = 0

    def __str__(self):
        return str(self.chave)

    def __repr__(self):
        return str(self.chave)

    def imprimir_subarvore(self, recuo=0, sentido="-"):
        if self.direito:
            self.direito.imprimir_subarvore(recuo+10, sentido="/")
        print(" " * recuo + sentido + " [{}] (h={}, fb={})".format(self.chave, self.altura, self.fator_de_balanceamento))
        if self.esquerdo:
            self.esquerdo.imprimir_subarvore(recuo+10, sentido="\\")

    def inserir(self, chave_nova):
        if chave_nova == self.chave:
            return self  # chave já existe
        raiz_sub = self
        if chave_nova < self.chave:
            if self.esquerdo:
                raiz_sub = self.esquerdo.inserir(chave_nova)
            else:
                self.esquerdo = VerticeAVL(chave_nova, self)
        else:
            if self.direito:
                raiz_sub = self.direito.inserir(chave_nova)
            else:
                self.direito = VerticeAVL(chave_nova, self)
        raiz_sub.atualizar_altura()
        raiz_sub = raiz_sub.balancear()
        return raiz_sub.pai or raiz_sub

    # -------------------- Remoção --------------------
    def _remover_folha(self):
        pai = self.pai
        if self.pai:
            if self.pai.esquerdo is self:
                self.pai.esquerdo = None
            else:
                self.pai.direito = None
            self.pai = None
        return pai

    def _remover_pai_de_um_filho(self):
        meu_pai = self.pai
        meu_filho = self.esquerdo or self.direito
        if meu_pai is None:
            meu_filho.chave, self.chave = self.chave, meu_filho.chave
            return meu_filho.remover(meu_filho.chave)
        meu_filho.pai = meu_pai
        if meu_pai.esquerdo is self:
            meu_pai.esquerdo = meu_filho
        else:
            meu_pai.direito = meu_filho
        self.pai = None
        self.esquerdo = None
        self.direito = None
        return meu_pai

    def _remover_pai_de_dois_filhos(self):
        esq = self.direito.buscar_vertice_menor_chave_na_subarvore()
        self.chave, esq.chave = esq.chave, self.chave
        return esq.remover(esq.chave)

    def remover(self, chave):
        if self.chave == chave:
            if self.esquerdo and self.direito:
                raiz_sub = self._remover_pai_de_dois_filhos()
            elif self.esquerdo or self.direito:
                raiz_sub = self._remover_pai_de_um_filho()
            else:
                raiz_sub = self._remover_folha()
            return raiz_sub
        elif chave < self.chave and self.esquerdo:
            raiz_sub = self.esquerdo.remover(chave)
        elif chave > self.chave and self.direito:
            raiz_sub = self.direito.remover(chave)
        else:
            return self
        raiz_sub.atualizar_altura()
        raiz_sub = raiz_sub.balancear()
        return raiz_sub.pai or raiz_sub

    def buscar_vertice_menor_chave_na_subarvore(self):
        if self.esquerdo:
            return self.esquerdo.buscar_vertice_menor_chave_na_subarvore()
        return self

    # -------------------- Altura e balanceamento --------------------
    @property
    def altura(self):
        return self._altura

    def atualizar_altura(self):
        self._altura = 1 + max(self.altura_esquerda, self.altura_direita)

    @property
    def altura_esquerda(self):
        return self.esquerdo.altura if self.esquerdo else -1

    @property
    def altura_direita(self):
        return self.direito.altura if self.direito else -1

    @property
    def fator_de_balanceamento(self):
        return self.altura_direita - self.altura_esquerda

    # -------------------- Balanceamento --------------------
    def balancear(self):
        fb = self.fator_de_balanceamento
        if fb == 2:
            return self._balancear_subarvore_direita()
        elif fb == -2:
            return self._balancear_subarvore_esquerda()
        return self

    def _balancear_subarvore_direita(self):
        if self.direito.fator_de_balanceamento == -1:
            self.direito._rotacao_para_direita()
        return self._rotacao_para_esquerda()

    def _balancear_subarvore_esquerda(self):
        if self.esquerdo.fator_de_balanceamento == 1:
            self.esquerdo._rotacao_para_esquerda()
        return self._rotacao_para_direita()

    def _rotacao_para_esquerda(self):
        v1 = self
        v2 = v1.direito
        s2 = v2.esquerdo
        v2.esquerdo = v1
        v1.direito = s2
        v2.pai = v1.pai
        v1.pai = v2
        if s2:
            s2.pai = v1
        v2.atualizar_altura()
        v1.atualizar_altura()
        return v2

    def _rotacao_para_direita(self):
        v3 = self
        v2 = v3.esquerdo
        s3 = v2.direito
        v2.direito = v3
        v3.esquerdo = s3
        v2.pai = v3.pai
        v3.pai = v2
        if s3:
            s3.pai = v3
        v3.atualizar_altura()
        v2.atualizar_altura()
        return v2


class ArvoreAVL:
    """
    Encapsula a árvore AVL, gerenciando a raiz.
    """
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz:
            self.raiz = self.raiz.inserir(chave)
        else:
            self.raiz = VerticeAVL(chave)

    def remover(self, chave):
        if self.raiz:
            self.raiz = self.raiz.remover(chave)

    def imprimir(self):
        if self.raiz:
            self.raiz.imprimir_subarvore()
        else:
            print("Árvore vazia")

    def desenhar(self):
        if not self.raiz:
            print("Árvore vazia")
            return
        G = nx.DiGraph()
        labels = {}
        def adicionar_nos_e_arestas(no):
            labels[no.chave] = str(no.chave)
            if no.esquerdo:
                G.add_edge(no.chave, no.esquerdo.chave)
                adicionar_nos_e_arestas(no.esquerdo)
            if no.direito:
                G.add_edge(no.chave, no.direito.chave)
                adicionar_nos_e_arestas(no.direito)
        adicionar_nos_e_arestas(self.raiz)
        pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
        nx.draw(G, pos, with_labels=True, labels=labels, arrows=False,
                node_size=1500, node_color='lightblue', font_size=12)
        plt.show()


if __name__ == "__main__":
    arvore = ArvoreAVL()
    # Inserir valores
    for valor in [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]:
        arvore.inserir(valor)
    print("Árvore após inserções:")
    arvore.imprimir()
    arvore.desenhar()

    # Remover alguns valores
    for valor in [70, 30, 50]:
        arvore.remover(valor)
        print(f"\nÁrvore após remover {valor}:")
        arvore.imprimir()
        arvore.desenhar()
