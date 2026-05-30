'''
Atividade de Arvore AVL para gerenciamento de Pokémon

Objetivos do Exercício: 
1. Implementação da Árvore AVL: - 
Implemente uma Árvore AVL que armazene informações sobre cada Pokémon. 
Os nós da árvore devem conter o nome do Pokémon e seu valor de força.

2. Funcionalidade de Busca: - Desenvolva uma função para buscar Pokémon na árvore pelo nome. 
Esta função deve retornar informações sobre o Pokémon, incluindo seu valor de força, s
e ele estiver presente na árvore. 3. Funcionalidade de Listagem: 
- Crie uma função para listar todos os Pokémon da árvore em ordem decrescente de força. 
Isso permitirá que os jogadores vejam os Pokémon mais fortes primeiro. 
4. Busca e Remoção: - Além da busca por nome, implemente funções para remover Pokémon da árvore por nome. 
A remoção deve manter as propriedades da Árvore AVL. Detalhes Adicionais: 
- A Árvore AVL deve ajustar-se automaticamente para manter o equilíbrio após inserções e remoções. 
- Você deve garantir que as operações de busca, remoção e listagem mantenham uma 
complexidade de tempo logarítmica. 
Testes: - Após implementar a árvore, teste sua implementação buscando vários Pokémon por nome 
para verificar a precisão e eficiência da busca. 
- Liste os Pokémon para verificar se a ordem decrescente de força está correta. 
- Teste as funções de remoção para diferentes casos, garantindo que a árvore se mantenha balanceada


'''

from dataclasses import dataclass
from typing import Any, Optional, List, Tuple

# Criação dos nodes AVL
class AVLNode:
    def __init__(self, key:Any, value:Any):
        self.key = key
        self.value = value
        self.left: Optional["AVLNode"] = None
        self.right: Optional["AVLNode"] = None
        self.height: int = 1    # altura de um novo nó = 1 (contando o próprio nó)


# Criação de uma arvore AVL genérica (ordenada por "key")



class AVLTree:
    def __init__(self):
        self.root = Optional[AVLNode] = None
    
    # Métodos úteis de altura e balance
    def _altura(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def _fator_equilibrio(self, node: Optional[AVLNode]) -> int:
        if not node:
            return 0
        return self._altura(node.left) - self._altura(node.right)
    
    def _atualiza_altura(self, node: AVLNode) -> None:
        node.height = 1 + max(self._altura(node.left), self._altura(node.right))

    
    # realizando rotações
    def _rotate_right(self, y = AVLNode) -> AVLNode:
        x = y.left
        T2 = x.right if x else None

        # Rotação
        x.right = y
        y.left = T2
    
        # Atualizando altura
        self._atualiza_altura(y)
        self._atualiza_altura(x)
        return x
    
    def _rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        T2 = y.left if y else None

        # Rotação
        y.left = x
        x.right = T2

        # Atualiza alturas
        self._atualiza_altura(x)
        self._atualiza_altura(y)
        return y
    
    # Rebalanceamento
    def _rebalance(self, node:AVLNode) -> AVLNode:
        self._atualiza_altura(node)
        bf = self._fator_equilibrio(node)

        # Caso Esquerda-Esquerda (LL)
        if bf > 1 and self._fator_equilibrio(node.left) >= 0:
            return self._rotate_right(node)
        
        # Caso Esquerda-Direita (LR)
        if bf > 1 and self._fator_equilibrio(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Caso Direita-Direita(RR)
        if bf < -1 and self._fator_equilibrio(node.right) <= 0:
            return self._rotate_left(node)
        
        # Caso Direita-Esquerda(RL)
        if bf < -1 and self._fator_equilibrio(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    

    # Método de inserções
    def inserir(self, key: Any, value: Any) -> None:
        def _inserir(node: Optional[AVLNode], key: Any, value: Any) -> AVLNode:
            if not node:
                return AVLNode(key, value)
            if key < node.key:
                node.left = _inserir(node.left, key, value)
            elif key > node.key:
                node.right = _inserir(node.right, key, value)
            else:
                # Chave ja existente > atualiza o valor
                node.value = value
                return node
            return self._rebalance(node)
        
        self.root = _inserir(self.root, key, value)

    # Método de busca
    def buscar(self, key: Any) -> Optional[Any]:
            current = self.root
            while current:
                if key < current.key:
                    current = current.left
                elif key > current.key:
                    current = current.right
                else:
                    return current.value
            return None
        
    # Node mínimo da subárvore
    def _node_minimo(self, node: AVLNode) -> AVLNode:
            while node.left:
                node = node.left
            return node
    
    # Método de remoção
    def remover(self, key: Any) -> None:
        def _remover(node: Optional[AVLNode], key: Any) -> Optional[AVLNode]:
            if not node:
                return None
            
            if key < node.key:
                node.left = _remover(node.left, key)
            elif key > node.key:
                node.right = _remover(node.right, key)
            else:
                # Encontrou o nó para remover
                if node.left and not node.right:
                    return None
                elif not node.left:
                    return node.righ
                elif not node.right:
                    return node.left
                else:
                    # Substitui pelo sucessor (menor da direita)
                    sucessor = self._menor_node(node.right)
                    node.key, node.value = sucessor.key, sucessor.value
                    node.right = _remover(node.right, sucessor.key)

            return self._rebalance(node) if node else None
        
        self.root = _remover(self.root, key)

    # Percurso in-order (ordenado por key)
    def in_order(self, reverse: bool = False) -> List[Tuple[Any, Any]]:
        out = List[Tuple[Any, Any]] = []

        def _in(node: Optional[AVLNode]):
            if not node:
                return
            if reverse:
                _in(node.right)
                out.append((node.key, node.value))
                _in(node.left)
            else:
                _in(node.left)
                out.append((node.key, node.value))
                _in(node.right)
        
        _in(self.root)
        return out
    

    # Verificação simples do balanceamento; ideal para testes
    def is_avl(self) -> bool:
        ok = True

        def _check(node: Optional[AVLNode]) -> int:
            nonlocal ok
            if not node:
                return 0
            left_right = _check(node.left)
            right_left = _check(node.right)
            if abs(left_right - right_left) > 1:
                ok = False
            return 1 + max(left_right, right_left)
        
        _ = +_check(self.root)
        return ok
    
# Domínio Pokémon
class Pokemon:
    name: str
    strength: int


class PokemonManagerAVL:
    '''
    Mantém as duas árvores:
    - name_tree: AVL indexada por nome (chave: str) -> Pokémon
    - strenght_tree: AVL indexada por força (strength, name)

    Permitindo:
    - Busca/remoção por nome
    - Listar em ordem decrescente de força após um percurso completo

    '''

    def __init__(self):
        self.name_tree = AVLTree()
        self.strength_tree = AVLTree()

    
    def insert(self, name: str, strength: int) -> None:
        existing = self.name_tree.get(name)
        if existing is not None:
            # Atualiza removendo antigo por força e insere com valor atualizado
            old: Pokemon = existing
            self.strength_tree.delete((old.strength, old.name))
        p = Pokemon(name=name, strength=strength)
        self.name_tree.insert(name, p)

        # Usa força, nome para desempatar quando forças forem iguais
        self.strength_tree.insert((strength, name), p)

    
    def search_by_name(self, name: str) -> Optional[Pokemon]:
        result = self.name_tree.get(name)
        return result
    
    def remove_by_name(self, name: str) -> bool:
        existing = self.name_tree.get(name)
        if existing is None:
            return False
        p: Pokemon = existing
        # Remove o pokemon das duas arvores
        self.name_tree.delete(name)
        self.strength_tree.delete((p.strength, p.name))
        return True
    
    def list_by_strength_desc(self) -> List[Pokemon]:
        # Percurso in-order reverso pela arvore de força
        ordered = self.strength_tree.in_order(reverse=True)
        return [val for _, val in ordered]
    
    def is_balanced(self) -> bool:
        return self.name_tree.is_avl() and self.strength_tree.is_avl()
    
# Execução dos testes

if __name__ == "__main__":
    pokedex = PokemonManagerAVL()

    # Inserindo Pokemon
    print("Inserção de Pokémon: ")
    entries = [
        ("Pikachu", 60), 
        ("Charizard", 140), 
        ("Bulbassauro", 48), 
        ("Squirtle", 45), 
        ("Hitmonlee", 75), 
        ("Gastly", 120), 
        ("Mewlee", 160), 
        ("Zapdos", 140),  # empatado com Charizard 
    ]
    for name, strength in entries:
        pokedex.insert(name, strength)
        assert pokedex.is_balanced, "Árvore balanceada após inserção"

    
    # Execução de Busca por nome
    print("Buscar por nome:")
    searching = ["Pikachu", "Mewlee", "Gayrados"]  # Gayrados não foi inserido
    for name in searching:
        p = pokedex.search_by_name(name)
        if p:
            print(f"Pokémon encontrado: {p.name} (força: {p.strength})")
        else:
            print(f'{p.name} não encontrado!')

    
    # Listagem por força decrescente (Mais forte - Mais fraco)
    print("Lista de Pokémon por força decrescente: ")
    ranked = pokedex.list_by_strength_desc()
    for p in ranked:
        print(f'{p.name:< 10} -> {p.strength}')

    
    # Verificação simples de ordem decrescente
    strengths = [p.strength for p in ranked]
    assert strengths == sorted(strengths, reverse=True), "Ordem Decrescente incorreta!"

    # atualização
    # --- Atualização de força (reinserir nome existente) ---
    print("\n== Atualizando força do Pikachu para 95 ==")
    pokedex.insert("Pikachu", 95)
    p = pokedex.search_by_name("Pikachu")
    print(f"Pikachu agora tem força {p.strength}")
    assert p.strength == 95
    assert pokedex.is_balanced(), "Árvore desbalanceada após atualização de força!"

    # --- Remoções ---
    print("\n== Remoções por nome ==")
    # Caso 1: remover folha provável (depende da estrutura, mas cobrimos logicamente)
    removed = pokedex.remove_by_name("Mewlee")
    print("Removeu Mewlee?", removed)
    assert removed

    # Caso 2: remover nó com 1 filho (depende do estado; garantimos que operação funciona)
    removed = pokedex.remove_by_name("Squirtle")
    print("Removeu Squirtle?", removed)
    assert removed

    # Caso 3: remover nó com 2 filhos (mais provável em nomes medianos)
    removed = pokedex.remove_by_name("Hitmonlee")
    print("Removeu Hitmonlee?", removed)
    assert removed

    # Remover ausente
    removed = pokedex.remove_by_name("Gayrados")
    print("Removeu Gayrados (ausente)?", removed)
    assert removed is False

    # Após remoções, ainda balanceada?
    assert pokedex.is_balanced(), "Árvore desbalanceada após remoções!"

    # Re-listagem para ver ranking atualizado
    print("\n== Ranking após remoções ==")
    ranked = pokedex.list_by_strength_desc()
    for p in ranked:
        print(f"{p.name:<10} -> {p.strength}")

    print("\n✅ Todos os testes passaram com sucesso!")
    