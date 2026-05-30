# Criando uma classe de carteira digital

class Carteira():
    def __init__(self):
        self.saldo = 0

    def adicionar_valor(self, valor):
        self.saldo += valor
        print('Operação realizada com sucesso')
        return valor

    def remover_valor(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Fundos removidos com sucesso!")
        else:
            print("Saldo insuficiente")

    def exibir_saldo(self):
        print(f'Saldo atual: $ {self.saldo}')
        return self.saldo

# criando classes abstratas e concretas
from abc import ABC, abstractmethod

class CartaoBase(ABC):
    @abstractmethod
    def calcular_cash_back(self, valor):
        pass

class CartaoGold(CartaoBase):
    def calcular_cash_back(self, valor):
        return valor * 0.03
    
class CartaoPlatinum(CartaoBase):
    def calcular_cash_back(self, valor):
        return valor * 0.05
    

class CartaoDiamond(CartaoBase):
    def calcular_cash_back(self, valor):
        return valor * 0.08
    
cartao1 = CartaoGold()
print(f'O cashback do cartão gold foi de R$ {cartao1.calcular_cash_back(2000)}\n')

cartao1 = CartaoPlatinum()
print(f'O cashback do cartão platium foi de R$ {cartao1.calcular_cash_back(2000)}\n')

cartao1 = CartaoDiamond()
print(f'O cashback do cartão diamond foi de R$ {cartao1.calcular_cash_back(2000)}\n')


# Carteira de rendimentos
rendimentos = Carteira()
print(f'Valor adicionado: ${rendimentos.adicionar_valor(500)}')
rendimentos.exibir_saldo()

