import matplotlib.pyplot as plt

# dados de venda
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio"]
vendas = [120, 250, 75, 60, 300]

# criando gráfico de barras
plt.bar(meses, vendas, color="royalblue")

# adicionar rótulos nos eixos
plt.xlabel("Mês")
plt.ylabel("Vendas (em unidades)")

# adicionar título no gráfico
plt.title("Vendas mensais")

# exibe o gráfico
plt.show()
