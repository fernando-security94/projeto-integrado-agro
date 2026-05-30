import pandas as pd

data = {
    'cod_pedido': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
    'valor_venda': [2500, 130, 960, 560, 3450, 400, 900, 1500, 990, 600, 100],
    'quantidade_itens': [14, 4, 8, 6, 17, 5, 8, 12, 10, 6, 4]
}

df = pd.DataFrame(data)

# valor total de vendas
print("Valor total de vendas em R$:")
print(df['valor_venda'].sum())
print()

# Quantidade de itens total vendida
print('Quantidade total de itens vendidos:')
print(df['quantidade_itens'].sum())
print()

# Quantos pedidos foram feitos?
print('Quantidade de pedidos:')
print(df['cod_pedido'].count())
print()

# Valor médio de vendas dos pedidos
print('Valor médio em R$ de venda dos pedidos:')
print(df['valor_venda'].mean())
print()

# Quantidade média de itens vendidos por pedido
print('Quantidade média de itens vendidos:')
print(df['quantidade_itens'].mean())
print()


print('Infos sobre as vendas:')
print(df.describe())