# criação de classe para gerar gráficos
# através de métodos

import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, data, title=None, xlabel=None, ylabel=None):
        self.data = data
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    # método de histogram
    def plot_histogram(self, bins=10, color='blue', figsize=(8,5)):
        plt.figure(figsize=figsize)
        plt.hist(self.data, bins=bins, color=color, edgecolor='blue')
        plt.grid(True, linestyle='--', alpha=0.7)
        self._set_labels()
        plt.tight_layout()
        plt.show()

    # método de barras
    def plot_bar(self, labels=None, xticks_rotation=0, color='green', figsize=(8,5)):
        plt.figure(figsize=figsize)

        # se nao passar labels, usa indice
        if labels is None:
            labels = list(range(len(self.data)))

        plt.bar(labels, self.data, color=color, edgecolor='black')
        plt.xticks(rotation=xticks_rotation)
        plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        self._set_labels()
        plt.tight_layout()
        plt.show()

    def plot_line(self, labels=None, color='purple', marker='o', figsize=(8, 5)):
        plt.figure(figsize=figsize)
        if labels is None:
            labels = list(range(len(self.data)))
        plt.plot(labels, self.data, color=color, marker=marker)
        plt.grid(True, linestyle='--', alpha=0.7)
        self._set_labels()
        plt.tight_layout()
        plt.show()

    # metodo para nomear titulos e labels
    def _set_labels(self):
        if self.title:
            plt.title(self.title)
        if self.xlabel:
            plt.xlabel(self.xlabel)
        if self.ylabel:
            plt.ylabel(self.ylabel)

# Exemplos de uso histogram
data = [10, 11, 12, 13, 30, 50, 30, 20, 10]
plotter = Plotter(data, title='Exemplo de Histograma Otimizado', xlabel='Valores', ylabel='Frequência')
plotter.plot_histogram(bins=8, color='skyblue')

# exemplo de uso de barras
data2 = [10, 20, 30, 40, 90]
plotter_bar = Plotter(data2, title='Exemplo de Barras', xlabel='Índices', ylabel='Valores')
plotter_bar.plot_bar()

vendas = [1, 15, 20, 32, 25, 50, 60, 70, 65, 82, 100, 95]
meses = 'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'
plotter_line = Plotter(vendas, title='Vendas ao Longo dos Meses', xlabel='Meses', ylabel='Vendas')
plotter_line.plot_line(labels=meses, color='orange', marker='s')