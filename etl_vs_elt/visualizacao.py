import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def gerar_grafico(resultado_etl: pd.DataFrame, resultado_elt: pd.DataFrame,
                  salvar_em: str = "grafico_etl_vs_elt.png") -> None:
    """
    Gera e salva o gráfico comparativo ETL vs ELT.
    O arquivo é salvo na mesma pasta do script.
    """
    etl = resultado_etl.sort_values('nome')
    elt = resultado_elt.sort_values('nome')

    clientes    = etl['nome'].tolist()
    valores_etl = etl['valor_total'].tolist()
    valores_elt = elt['valor_total'].tolist()

    x       = np.arange(len(clientes))
    largura = 0.35

    fig, ax = plt.subplots(figsize=(10, 5))

    barras_etl = ax.bar(x - largura / 2, valores_etl, largura, label='ETL', color='#4472C4')
    barras_elt = ax.bar(x + largura / 2, valores_elt, largura, label='ELT', color='#ED7D31')

    # Rótulos em cima de cada barra
    for barra in barras_etl:
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height() + 30,
            f'R$ {barra.get_height():,.0f}',
            ha='center', va='bottom', fontsize=9, fontweight='bold'
        )
    for barra in barras_elt:
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height() + 30,
            f'R$ {barra.get_height():,.0f}',
            ha='center', va='bottom', fontsize=9, fontweight='bold'
        )

    ax.set_xlabel('Cliente', fontsize=12)
    ax.set_ylabel('Valor Total de Compra (R$)', fontsize=12)
    ax.set_title('Comparação ETL vs ELT por Cliente', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(clientes, fontsize=11)
    ax.set_ylim(0, max(valores_etl + valores_elt) * 1.2)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'R$ {v:,.0f}'))
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()

    caminho = Path(salvar_em)
    plt.savefig(caminho, dpi=150, bbox_inches='tight')
    plt.close()

    print(f"  Gráfico salvo em: {caminho.resolve()}")
