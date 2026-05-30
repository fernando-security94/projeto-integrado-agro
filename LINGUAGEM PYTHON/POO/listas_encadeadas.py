# Exemplo de listas encadeadas - linked lists

class ItemLista:
    def __init__(self, data=0, nextItem=None):
        self.data = data
        self.next = nextItem

    def __repr__(self):
        return "%s => %s"%(self.data, self.next)
    
# __repr__ fornece uma representação em string do objeto,
# exibindo o item adicionado e o próximo item na sequência

# Criação da classe que irá representar a lista encadeada

class ListaEncadeada:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        return "%s"%(self.head)
    

    # Criação de método de inserção de elementos

    def insere(self, lista, data):
        # cria objeto para retornar novo item na lista
        item = ItemLista(data)

        # head é apontado como próximo item
        item.next = lista.head

        # o item atual se torna head
        lista.head = item


    # Criação do método de remoção de itens
    def remover(self, valor):
        # Item a ser removido é o head
        if self.head and self.head.data == valor:
            self.head = self.head.next
            return

        # Inicializando os ponteiros
        before = None
        navegar = self.head

        # Percorre a lista até encontrar o valor
        while navegar and navegar.data != valor:
            before = navegar
            navegar = navegar.next

        # Remove o item se encontrar
        if navegar:
            before.next = navegar.next
        else:
            print(f'Item {valor} não encontrado na lista')    

    # Criação do método de busca de elementos
    def buscar(self, valor):
        # Percorre a lista em busca do valor
        navegar = self.head

        while navegar:
            if navegar.data == valor:
                return "Item encontrado"  # Valor encontrado
            navegar = navegar.next
        return "Item não encontrado"  # Valor não encontrado
    
    # Criação de contagem dos elementos na lista
    def contar(self):
        # Conta quantos elementos existem na lista
        contador = 0
        navegar = self.head

        while navegar:
            contador += 1
            navegar = navegar.next
        return contador

# Esse método aciona a class, passando o dado como argumento e armazenando
# o resultado na variável 'item'. Em seguida, o atributo 'nextItem'
# do novo item é configurado para apontar para o atual item da lista ('head),
# e então, o 'head' da lista é atualizado para ser o novo item, o que efetivamente
# coloar o novo item no início da lista.

# MODULAÇÃO DO CÓDIGO - Criar arquivo processar.py para importar a class


'''
| Ponto            | Explicação                                                                                                        |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |
| `self`           | Dentro de métodos da classe, você deve usar `self` para acessar os atributos e outros métodos da instância atual. |
| `return`         | Usado para encerrar a função logo após remover o `head`.                                                          |
| `print` opcional | Pode ser mantido como feedback, ou removido se quiser uma função silenciosa.                                      |
| `navegar.data`   | Sempre bom verificar se `navegar` é válido antes de acessar `.data`, o que já é garantido pelo `while`.           |



'''
