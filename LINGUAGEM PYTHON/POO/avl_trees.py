class NodoAVL:
    def __init__(self, chave):
        self.chave = chave        # Valor armazenado no nodo
        self.esquerda = None      # Filho à esquerda
        self.direita = None       # Filho à direita
        self.altura = 1           # Altura inicial do nodo


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    # ----------------------------
    # Funções auxiliares
    # ----------------------------
    def obter_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def fator_balanceamento(self, nodo):
        if not nodo:
            return 0
        return self.obter_altura(nodo.esquerda) - self.obter_altura(nodo.direita)

    def atualizar_altura(self, nodo):
        nodo.altura = 1 + max(self.obter_altura(nodo.esquerda),
                              self.obter_altura(nodo.direita))

    # ----------------------------
    # Rotações
    # ----------------------------
    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        # Rotação
        x.direita = y
        y.esquerda = T2

        # Atualizar alturas
        self.atualizar_altura(y)
        self.atualizar_altura(x)

        return x  # Nova raiz

    def rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        # Rotação
        y.esquerda = x
        x.direita = T2

        # Atualizar alturas
        self.atualizar_altura(x)
        self.atualizar_altura(y)

        return y  # Nova raiz

    # ----------------------------
    # Inserção
    # ----------------------------
    def inserir(self, nodo, chave):
        # Inserção BST normal
        if not nodo:
            return NodoAVL(chave)
        elif chave < nodo.chave:
            nodo.esquerda = self.inserir(nodo.esquerda, chave)
        else:
            nodo.direita = self.inserir(nodo.direita, chave)

        # Atualizar altura
        self.atualizar_altura(nodo)

        # Obter fator de balanceamento
        balanceamento = self.fator_balanceamento(nodo)

        # Casos de desbalanceamento
        # Caso 1 - Esquerda Esquerda
        if balanceamento > 1 and chave < nodo.esquerda.chave:
            return self.rotacao_direita(nodo)

        # Caso 2 - Direita Direita
        if balanceamento < -1 and chave > nodo.direita.chave:
            return self.rotacao_esquerda(nodo)

        # Caso 3 - Esquerda Direita
        if balanceamento > 1 and chave > nodo.esquerda.chave:
            nodo.esquerda = self.rotacao_esquerda(nodo.esquerda)
            return self.rotacao_direita(nodo)

        # Caso 4 - Direita Esquerda
        if balanceamento < -1 and chave < nodo.direita.chave:
            nodo.direita = self.rotacao_direita(nodo.direita)
            return self.rotacao_esquerda(nodo)

        return nodo

    # ----------------------------
    # Remoção
    # ----------------------------
    def remover(self, nodo, chave):
        if not nodo:
            return nodo

        # Remoção padrão BST
        if chave < nodo.chave:
            nodo.esquerda = self.remover(nodo.esquerda, chave)
        elif chave > nodo.chave:
            nodo.direita = self.remover(nodo.direita, chave)
        else:
            # Caso 1: nodo folha ou 1 filho
            if not nodo.esquerda:
                return nodo.direita
            elif not nodo.direita:
                return nodo.esquerda

            # Caso 2: nodo com 2 filhos → pegar sucessor (menor valor da subárvore direita)
            sucessor = self.minimo(nodo.direita)
            nodo.chave = sucessor.chave
            nodo.direita = self.remover(nodo.direita, sucessor.chave)

        if not nodo:
            return nodo

        # Atualizar altura
        self.atualizar_altura(nodo)

        # Balancear
        balanceamento = self.fator_balanceamento(nodo)

        # Casos de rotação
        if balanceamento > 1 and self.fator_balanceamento(nodo.esquerda) >= 0:
            return self.rotacao_direita(nodo)

        if balanceamento > 1 and self.fator_balanceamento(nodo.esquerda) < 0:
            nodo.esquerda = self.rotacao_esquerda(nodo.esquerda)
            return self.rotacao_direita(nodo)

        if balanceamento < -1 and self.fator_balanceamento(nodo.direita) <= 0:
            return self.rotacao_esquerda(nodo)

        if balanceamento < -1 and self.fator_balanceamento(nodo.direita) > 0:
            nodo.direita = self.rotacao_direita(nodo.direita)
            return self.rotacao_esquerda(nodo)

        return nodo

    # ----------------------------
    # Utilitários
    # ----------------------------
    def minimo(self, nodo):
        atual = nodo
        while atual.esquerda:
            atual = atual.esquerda
        return atual

    def pre_ordem(self, nodo):
        if not nodo:
            return []
        return [nodo.chave] + self.pre_ordem(nodo.esquerda) + self.pre_ordem(nodo.direita)


# ----------------------------
# Testes
# ----------------------------
if __name__ == "__main__":
    avl = ArvoreAVL()

    # Inserindo valores
    valores = [10, 20, 30, 40, 50, 25]
    for v in valores:
        avl.raiz = avl.inserir(avl.raiz, v)

    print("Árvore em pré-ordem após inserções:", avl.pre_ordem(avl.raiz))

    # Removendo um valor
    avl.raiz = avl.remover(avl.raiz, 40)
    print("Árvore em pré-ordem após remover 40:", avl.pre_ordem(avl.raiz))


print()
print()
print()
print()
print()

# avl_tree.py

class VerticeAVL:
    """
    Classe que representa um vértice (nó) de uma árvore AVL.
    Contém chave, referências para pai e filhos, altura, métodos de inserção,
    remoção, balanceamento e rotações.
    """

    # --------------------- Parte 1: Construtor, Inserir, Imprimir ---------------------
    def __init__(self, chave, pai=None):
        self.chave = chave          # Valor armazenado no nó
        self.pai = pai              # Referência para o nó pai
        self.esquerdo = None        # Subárvore esquerda
        self.direito = None         # Subárvore direita
        self._altura = 0            # Altura do nó

    def __str__(self):
        return str(self.chave)

    def __repr__(self):
        return str(self.chave)

    def imprimir_subarvore(self, recuo=0, sentido=""):
        """
        Imprime visualmente a subárvore a partir deste nó.
        """
        if self.direito:
            self.direito.imprimir_subarvore(recuo + 10, sentido="R")
        print(" " * recuo + "{}----> [{}] (h={}, fb={})".format(
            sentido, self.chave, self.altura, self.fator_de_balanceamento))
        if self.esquerdo:
            self.esquerdo.imprimir_subarvore(recuo + 10, sentido="L")

    def inserir(self, chave_nova):
        """
        Insere uma nova chave na árvore AVL mantendo o balanceamento.
        """
        print("{} (atual={})".format(chave_nova, self.chave))
        if chave_nova == self.chave:
            return self  # Chave já existe

        raiz_da_subarvore = self
        if chave_nova < self.chave:
            if self.esquerdo:
                raiz_da_subarvore = self.esquerdo.inserir(chave_nova)
            else:
                self.esquerdo = VerticeAVL(chave_nova, self)
        else:
            if self.direito:
                raiz_da_subarvore = self.direito.inserir(chave_nova)
            else:
                self.direito = VerticeAVL(chave_nova, self)

        # Atualiza altura e balanceia
        raiz_da_subarvore.atualizar_altura()
        raiz_da_subarvore = raiz_da_subarvore.balancear()
        return raiz_da_subarvore.pai or raiz_da_subarvore

    # --------------------- Parte 2: Remover ---------------------
    def _remover_folha(self):
        """
        Remove o nó folha.
        """
        print("{}: vértice folha, filho de {}".format(self.chave, self.pai.chave if self.pai else None))
        pai = self.pai
        if self.pai:
            if self.pai.esquerdo is self:
                self.pai.esquerdo = None
            else:
                self.pai.direito = None
            self.pai = None
        return pai

    def _remover_pai_de_um_filho(self):
        """
        Remove um nó com apenas um filho.
        """
        print("{}: pai de {}".format(self.chave, (self.esquerdo or self.direito).chave))
        meu_pai = self.pai
        meu_filho = self.esquerdo or self.direito

        if meu_pai is None:
            # Se for raiz, troca com filho
            meu_filho.chave, self.chave = self.chave, meu_filho.chave
            return meu_filho.remover(meu_filho.chave)

        meu_filho.pai = meu_pai
        if meu_pai.esquerdo is self:
            meu_pai.esquerdo = meu_filho
        else:
            meu_pai.direito = meu_filho

        self.pai = self.esquerdo = self.direito = None
        return meu_pai

    def _remover_pai_de_dois_filhos(self):
        """
        Remove um nó com dois filhos.
        """
        print("{}: pai de {} e {}".format(self.chave, self.esquerdo.chave, self.direito.chave))
        esq = self.direito.buscar_vertice_menor_chave_na_subarvore()
        print("Substituto:", esq)
        self.chave, esq.chave = esq.chave, self.chave
        return esq.remover(esq.chave)

    def remover(self, chave):
        """
        Remove a chave da árvore e rebalanceia.
        """
        print("{} (chave atual: {})".format(chave, self.chave))
        if self.chave == chave:
            print("{} para remover".format(chave))
            if self.esquerdo and self.direito:
                raiz_da_subarvore = self._remover_pai_de_dois_filhos()
            elif self.esquerdo or self.direito:
                raiz_da_subarvore = self._remover_pai_de_um_filho()
            else:
                raiz_da_subarvore = self._remover_folha()
            return raiz_da_subarvore

        raiz_da_subarvore = self
        if chave < self.chave:
            raiz_da_subarvore = self.esquerdo and self.esquerdo.remover(chave)
        elif chave > self.chave:
            raiz_da_subarvore = self.direito and self.direito.remover(chave)

        if raiz_da_subarvore:
            raiz_da_subarvore.atualizar_altura()
            raiz_da_subarvore = raiz_da_subarvore.balancear()
        return raiz_da_subarvore.pai or raiz_da_subarvore

    def buscar_vertice_menor_chave_na_subarvore(self):
        if self.esquerdo:
            return self.esquerdo.buscar_vertice_menor_chave_na_subarvore()
        return self

    # --------------------- Parte 3: Altura, Fator, Balancear, Rotações ---------------------
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

    def balancear(self):
        fb = self.fator_de_balanceamento
        print("{} = {}".format(self.chave, fb))
        if fb == 2:
            return self._balancear_subarvore_direita()
        if fb == -2:
            return self._balancear_subarvore_esquerda()
        return self

    def _balancear_subarvore_direita(self):
        print("Balanceando à direita:", self.chave)
        if self.direito.fator_de_balanceamento == -1:
            print("{} à direita + Rotação à esquerda".format(self.direito))
            self.direito._rotacao_para_direita()
        return self._rotacao_para_esquerda()

    def _balancear_subarvore_esquerda(self):
        print("Balanceando à esquerda:", self.chave)
        if self.esquerdo.fator_de_balanceamento == 1:
            print("{} à esquerda + Rotação à direita".format(self.esquerdo))
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
        v1.atualizar_altura()
        v2.atualizar_altura()
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
    Encapsulador da árvore AVL.
    Mantém referência à raiz e delega inserção, remoção e impressão.
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


# --------------------- Testes práticos ---------------------
if __name__ == "__main__":
    avl = ArvoreAVL()
    valores = [30, 20, 40, 10, 25, 35, 50, 5, 15]
    print("Inserindo valores:", valores)
    for v in valores:
        avl.inserir(v)

    print("\nÁrvore após inserções:")
    avl.imprimir()

    remover_valores = [20, 30]
    print("\nRemovendo valores:", remover_valores)
    for v in remover_valores:
        avl.remover(v)

    print("\nÁrvore após remoções:")
    avl.imprimir()
