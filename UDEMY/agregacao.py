'''
Agregação é uma forma mais especializada de associação entre dois ou mais objetos.
Cada objeto terá seu ciclo de vida independente.
Geralmente é uma relação de UM para MUITOS, onde um objeto tem um ou vários objetos.

Os objetos podem viver separadamente, mas pode se tratar de uma relação onde 
um objeto precisa de outro para fazer determinada tarefa.

'''



class Carrinho:
    def __init__(self):
        self._produtos = []

    def preco_total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos):
            self._produtos.extend(produtos)
            #  self._produtos += produtos
            #  for produto in produtos:
            #     self._produtos.append(produto)
            return
    
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()
        return



class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print()
print(f'O total é R${carrinho.preco_total()}')

'''
Neste código, temos o modelo de agregação, que é bem similar ao de
associação, porém, normalmente, a relação é de um objeto para muitos,
podendo ou não, serem dependentes um dos outros.

Então, começamos criando a primeira class Carrinho.
Será iniciada com def __init__(self) e receberá 
uma instancia protegida self._produtos = [], essa lista vazia, será
o local onde os produtos serão adicionados.

Criaremos um método que calcula o preço total de todos os produtos do carrinho
Então, def preco_total(self) e faremos através de list comprehension com: return 
sum([p.preco for p in self._produtos]) = somar os preços na medida que self._produto
recebe-los.

Criaremos um método que executa a ação de inserir produtos no 
carrinho.
Então, def inserir_produtos(self, *produtos). Os produtos serão passados
de forma empacotada(fará sentido mais pra frente). Vamos atribuir ._produtos a lista vazia,
através de self._produtos.extend(produtos), ou self._produtos += produtos ou,
for produto in produtos:
    self._produtos.append(produto)

    
Aqui, criaremos um método que lista os produtos de forma iterada, pelo laço for.
Então, def listar_produtos(self) e dentro do laço for, vamos pedir
os produtos in self._produtos, e exibir o nome e o preço (que serão atribuídos como
argumentos posicionais) com print(produto.nome, produto.preco)

Agora, a segunda classe será criada, que estará relacionada aos produtos, de fato, e então,
concluir a agregação.

Criamos class Produto, e foi iniciada com __init__(self, nome, preco), vamos
atribuir self.nome = nome, self.preco = preco

Execuções:
Vamos atribuir class Carrinho a uma variável, e class Produto() em duas variáveis posicionais,
uma vez que elas estão sendo empacotadas em def inserir_produtos, com seus valores,
'Caneta', 1.20 e 'Camiseta, 20, respectivamente.
Vamos executar def inserir_produtos() através de carrinho e atribuir as duas variaveis p1, p2:
carrinho.inserir.produtos(p1, p2) e vamos exibi-los através de
carrinho.listar_produtos()

Por fim, vamos executar def preco_total em uma f'string com 
carrinho.preco_total()

'''