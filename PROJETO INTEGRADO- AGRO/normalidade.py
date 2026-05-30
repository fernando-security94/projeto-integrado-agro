# =============================================================================
# PROJETO INTEGRADO — EmpresaX Agronegócio
# Passo 1: Probabilidade e Estatística para Análise de Dados
# Bloco 4: Teste de Normalidade dos Dados de Produtividade
# =============================================================================
# OBJETIVO DESTE BLOCO:
#   Verificar se os dados de produtividade seguem uma distribuição normal,
#   condição importante para validar os métodos estatísticos utilizados
#   nos blocos anteriores e no modelo de regressão do Passo 5.
#
# TESTE ESCOLHIDO: Shapiro-Wilk
#   Motivo: nossa amostra tem n=50, dentro da faixa onde Shapiro-Wilk
#   é o teste mais poderoso e recomendado pela literatura estatística.
#   O Kolmogorov-Smirnov seria mais apropriado para n > 50.
#
# HIPÓTESES:
#   H0: os dados seguem distribuição normal
#   H1: os dados NÃO seguem distribuição normal
#
# REGRA DE DECISÃO:
#   p > 0.05 → não rejeitamos H0 → normalidade compatível com os dados
#   p ≤ 0.05 → rejeitamos H0 → dados provavelmente não normais
# =============================================================================


# -----------------------------------------------------------------------------
# IMPORTAÇÃO DAS BIBLIOTECAS
# -----------------------------------------------------------------------------
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# LEITURA DO DATASET
# -----------------------------------------------------------------------------
df = pd.read_csv("dados_agricolas_parana.csv")
prod = df['produtividade_sacas_ha'].values  # array NumPy da produtividade

print("=" * 60)
print("  BLOCO 4 — TESTE DE NORMALIDADE (Shapiro-Wilk)")
print("=" * 60)
print(f"\nAmostra: {len(prod)} propriedades agrícolas")


# -----------------------------------------------------------------------------
# TESTE DE SHAPIRO-WILK
# -----------------------------------------------------------------------------
# stats.shapiro() recebe o array de dados e retorna dois valores:
#   statistic → o valor W do teste (quanto mais próximo de 1, mais normal)
#   p_value   → a probabilidade de observar esses dados SE H0 fosse verdade
#
# Em R você faria: shapiro.test(prod)

statistic, p_value = stats.shapiro(prod)

print(f"\nResultado do Teste de Shapiro-Wilk:")
print(f"  Estatística W:  {statistic:.4f}")
print(f"  P-valor:        {p_value:.4f}")

# Interpretação automática
print(f"\nInterpretação:")
if p_value > 0.05:
    print(f"  p = {p_value:.4f} > 0.05 → NÃO rejeitamos H0.")
    print(f"  Os dados são COMPATÍVEIS com distribuição normal.")
    conclusao = "compatíveis com normalidade"
else:
    print(f"  p = {p_value:.4f} ≤ 0.05 → REJEITAMOS H0.")
    print(f"  Os dados NÃO seguem distribuição normal.")
    conclusao = "não normais"


# -----------------------------------------------------------------------------
# VISUALIZAÇÃO — 3 GRÁFICOS COMPLEMENTARES
# -----------------------------------------------------------------------------
# Nenhum teste estatístico substitui a inspeção visual.
# Usamos três gráficos em conjunto para uma análise mais completa:
#
#   1. Histograma com curva normal sobreposta
#      → mostra a forma geral da distribuição
#
#   2. Q-Q Plot (Quantile-Quantile Plot)
#      → compara os quantis dos dados com os quantis de uma normal teórica
#      → se os pontos seguirem a linha diagonal, os dados são normais
#
#   3. Boxplot
#      → mostra mediana, quartis e possíveis outliers

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))


# --- Gráfico 1: Histograma com curva normal teórica sobreposta ---
ax1.hist(prod, bins=12, density=True,  # density=True normaliza para área = 1
         color='steelblue', edgecolor='white', alpha=0.7, label='Dados observados')

# Curva normal teórica com a mesma média e DP dos dados
x = np.linspace(prod.min(), prod.max(), 200)
media = np.mean(prod)
dp = np.std(prod, ddof=1)
curva_normal = stats.norm.pdf(x, loc=media, scale=dp)
ax1.plot(x, curva_normal, color='tomato', linewidth=2.5, label='Normal teórica')

ax1.set_xlabel("Produtividade (sacas/ha)", fontsize=10)
ax1.set_ylabel("Densidade", fontsize=10)
ax1.set_title("Histograma + Curva Normal", fontsize=11)
ax1.legend(fontsize=8)
ax1.grid(True, linestyle='--', alpha=0.4)


# --- Gráfico 2: Q-Q Plot ---
# stats.probplot calcula os quantis teóricos e observados
# plot=ax2 já desenha no eixo que passamos
(quantis_teoricos, quantis_observados), (slope, intercept, r) = stats.probplot(
    prod, dist="norm", plot=ax2
)

# Personalizando o visual gerado pelo probplot
ax2.get_lines()[0].set(color='steelblue', markersize=5, alpha=0.8)  # pontos
ax2.get_lines()[1].set(color='tomato', linewidth=2)                  # linha de referência

ax2.set_title("Q-Q Plot", fontsize=11)
ax2.set_xlabel("Quantis Teóricos (Normal)", fontsize=10)
ax2.set_ylabel("Quantis Observados", fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.4)

# Anotação com o resultado do teste
ax2.annotate(
    f'Shapiro-Wilk\nW = {statistic:.4f}\np = {p_value:.4f}',
    xy=(0.05, 0.78), xycoords='axes fraction',
    fontsize=8.5, color='darkred',
    bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', edgecolor='gray')
)


# --- Gráfico 3: Boxplot ---
bp = ax3.boxplot(prod, patch_artist=True,  # patch_artist=True permite colorir
                 widths=0.5,
                 medianprops=dict(color='tomato', linewidth=2.5),
                 boxprops=dict(facecolor='steelblue', alpha=0.6),
                 whiskerprops=dict(linewidth=1.5),
                 capprops=dict(linewidth=1.5),
                 flierprops=dict(marker='o', color='gray',  # outliers
                                 markerfacecolor='tomato', markersize=7))

# Linha horizontal na média (diferente da mediana — boa comparação visual)
ax3.axhline(media, color='darkblue', linewidth=1.5,
            linestyle='--', label=f'Média: {media:.2f}')

ax3.set_ylabel("Produtividade (sacas/ha)", fontsize=10)
ax3.set_title("Boxplot da Produtividade", fontsize=11)
ax3.set_xticks([])  # remove ticks desnecessários no eixo x
ax3.legend(fontsize=8)
ax3.grid(True, linestyle='--', alpha=0.4, axis='y')


plt.suptitle(
    f"Análise de Normalidade — Produtividade Agrícola (n=50)\n"
    f"Shapiro-Wilk: W={statistic:.4f}, p={p_value:.4f} → dados {conclusao}",
    fontsize=12, y=0.98
)
plt.tight_layout(rect=[0, 0 , 1, 0.93])
plt.savefig("grafico_normalidade.png", dpi=150, bbox_inches='tight')
plt.show()
print("\nGráfico salvo: grafico_normalidade.png")


# -----------------------------------------------------------------------------
# RESUMO FINAL DO BLOCO 4
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("  RESUMO — BLOCO 4")
print("=" * 60)
print(f"""
  Teste utilizado:   Shapiro-Wilk
  Justificativa:     Amostra com n=50, faixa onde Shapiro-Wilk
                     é mais poderoso que Kolmogorov-Smirnov.

  Estatística W:     {statistic:.4f}
  P-valor:           {p_value:.4f}
  Conclusão:         Dados {conclusao}.

  Implicação:        Os métodos estatísticos utilizados nos blocos
                     anteriores (IC, correlação de Pearson) e o modelo
                     de regressão linear do Passo 5 são adequados,
                     pois assumem (ou são robustos a) normalidade
                     dos dados.
""")