# =============================================================================
# PROJETO INTEGRADO — EmpresaX Agronegócio
# Passo 1: Probabilidade e Estatística para Análise de Dados
# Bloco 2: Estatísticas Descritivas (Média, Desvio Padrão e Correlação)
# =============================================================================
# OBJETIVO DESTE BLOCO:
#   Calcular e interpretar as principais métricas descritivas do dataset,
#   entendendo o comportamento individual de cada variável e a relação
#   entre chuva e produtividade.
#
# PRÉ-REQUISITO:
#   Rodar o Bloco 1 antes, pois este script lê o arquivo CSV gerado lá.
# =============================================================================


# -----------------------------------------------------------------------------
# IMPORTAÇÃO DAS BIBLIOTECAS
# -----------------------------------------------------------------------------
import pandas as pd
import numpy as np
from scipy import stats      # biblioteca científica — usaremos para correlação
import matplotlib.pyplot as plt  # para gerar o gráfico de dispersão


# -----------------------------------------------------------------------------
# LEITURA DO DATASET
# -----------------------------------------------------------------------------
# Carregamos o CSV gerado no Bloco 1.
# Em vez de reger os dados novamente, reutilizamos o arquivo salvo —
# boa prática: cada bloco tem uma responsabilidade única.

df = pd.read_csv("dados_agricolas_parana.csv")

print("=" * 55)
print("  BLOCO 2 — ESTATÍSTICAS DESCRITIVAS")
print("=" * 55)
print(f"\nDataset carregado com sucesso: {len(df)} registros\n")


# -----------------------------------------------------------------------------
# MÉDIA
# -----------------------------------------------------------------------------
# A média aritmética representa o valor "central" da distribuição.
# Em R: mean(df$chuva_mm)
# Em Python/Pandas: df['coluna'].mean()

media_chuva = df['chuva_mm'].mean()
media_temp  = df['temperatura_c'].mean()
media_prod  = df['produtividade_sacas_ha'].mean()

print("-" * 55)
print("MÉDIAS")
print("-" * 55)
print(f"  Chuva média:         {media_chuva:.1f} mm")
print(f"  Temperatura média:   {media_temp:.1f} °C")
print(f"  Produtividade média: {media_prod:.2f} sacas/ha")


# -----------------------------------------------------------------------------
# DESVIO PADRÃO
# -----------------------------------------------------------------------------
# O desvio padrão mede a dispersão dos dados em torno da média.
# Quanto maior, mais os valores variam entre as propriedades.
#
# ATENÇÃO — ddof (Delta Degrees of Freedom):
#   ddof=1 → desvio padrão AMOSTRAL (divide por n-1) ← correto para amostras
#   ddof=0 → desvio padrão POPULACIONAL (divide por n)
#
#   Como temos uma AMOSTRA de 50 propriedades (não o universo todo),
#   usamos ddof=1. Em R, sd() já usa ddof=1 por padrão.
#
# Em R: sd(df$chuva_mm)
# Em Python: df['coluna'].std(ddof=1)  ← ddof=1 é o padrão do Pandas também

dp_chuva = df['chuva_mm'].std(ddof=1)
dp_temp  = df['temperatura_c'].std(ddof=1)
dp_prod  = df['produtividade_sacas_ha'].std(ddof=1)

print("\n" + "-" * 55)
print("DESVIOS PADRÃO (amostral, ddof=1)")
print("-" * 55)
print(f"  Chuva:         {dp_chuva:.1f} mm")
print(f"  Temperatura:   {dp_temp:.1f} °C")
print(f"  Produtividade: {dp_prod:.2f} sacas/ha")


# -----------------------------------------------------------------------------
# CORRELAÇÃO DE PEARSON — chuva x produtividade
# -----------------------------------------------------------------------------
# Medimos a força e a direção da relação LINEAR entre chuva e produtividade.
#
# DUAS FORMAS DE CALCULAR — vamos ver as duas:
#
# FORMA 1: Pandas — df.corr()
#   Retorna uma MATRIZ de correlação entre todas as colunas numéricas.
#   Prático quando queremos ver várias correlações de uma vez.
#   Equivalente ao cor() do R aplicado a um data.frame.

matriz_correlacao = df[['chuva_mm', 'temperatura_c', 'produtividade_sacas_ha']].corr()

print("\n" + "-" * 55)
print("MATRIZ DE CORRELAÇÃO DE PEARSON (Pandas)")
print("-" * 55)
print(matriz_correlacao.round(4).to_string())

# FORMA 2: SciPy — stats.pearsonr()
#   Retorna o coeficiente r E o p-valor do teste de significância.
#   O p-valor nos diz se a correlação é estatisticamente significativa
#   ou se pode ter ocorrido por acaso.
#
#   Regra geral do p-valor:
#     p < 0.05 → correlação significativa (rejeitamos H0: r = 0)
#     p ≥ 0.05 → não há evidência suficiente de correlação

r_chuva_prod, p_chuva_prod = stats.pearsonr(
    df['chuva_mm'],
    df['produtividade_sacas_ha']
)

print("\n" + "-" * 55)
print("CORRELAÇÃO: Chuva x Produtividade (SciPy)")
print("-" * 55)
print(f"  Coeficiente r: {r_chuva_prod:.4f}")
print(f"  P-valor:       {p_chuva_prod:.4f}")

# Interpretação automática baseada nos valores calculados
if p_chuva_prod < 0.05:
    significancia = "estatisticamente SIGNIFICATIVA (p < 0.05)"
else:
    significancia = "NÃO significativa (p >= 0.05)"

if r_chuva_prod > 0.7:
    forca = "forte positiva"
elif r_chuva_prod > 0.4:
    forca = "moderada positiva"
elif r_chuva_prod > 0:
    forca = "fraca positiva"
else:
    forca = "negativa ou nula"

print(f"\n  Interpretação: correlação {forca}, {significancia}.")
print(f"  Ou seja: propriedades com mais chuva tendem a ter")
print(f"  maior produtividade — a relação é {forca}.")


# -----------------------------------------------------------------------------
# GRÁFICO DE DISPERSÃO — chuva x produtividade
# -----------------------------------------------------------------------------
# Visualizar a correlação é tão importante quanto calculá-la.
# Um gráfico de dispersão (scatter plot) mostra cada propriedade como
# um ponto no plano, com chuva no eixo X e produtividade no eixo Y.
# Se houver correlação positiva, os pontos devem formar uma tendência
# ascendente da esquerda para a direita.

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(
    df['chuva_mm'],
    df['produtividade_sacas_ha'],
    color='steelblue',
    alpha=0.7,          # transparência: facilita ver pontos sobrepostos
    edgecolors='white',
    linewidths=0.5,
    s=80                # tamanho dos pontos
)

# Linha de tendência (regressão linear simples) — antecipando o Passo 5!
# np.polyfit ajusta uma reta (grau 1) aos dados
coef = np.polyfit(df['chuva_mm'], df['produtividade_sacas_ha'], 1)
linha_x = np.linspace(df['chuva_mm'].min(), df['chuva_mm'].max(), 100)
linha_y = np.polyval(coef, linha_x)
ax.plot(linha_x, linha_y, color='tomato', linewidth=2, label='Tendência linear')

# Anotação com o valor de r no gráfico
ax.annotate(
    f'r = {r_chuva_prod:.3f}  |  p = {p_chuva_prod:.4f}',
    xy=(0.05, 0.92), xycoords='axes fraction',
    fontsize=10, color='darkred',
    bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor='gray')
)

ax.set_xlabel("Chuva (mm)", fontsize=12)
ax.set_ylabel("Produtividade (sacas/ha)", fontsize=12)
ax.set_title("Correlação entre Chuva e Produtividade\n50 Propriedades Agrícolas — Paraná", fontsize=13)
ax.legend()
ax.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.savefig("grafico_correlacao_chuva_produtividade.png", dpi=150)
plt.show()
print("\nGráfico salvo: grafico_correlacao_chuva_produtividade.png")


# -----------------------------------------------------------------------------
# RESUMO FINAL DO BLOCO 2
# -----------------------------------------------------------------------------
print("\n" + "=" * 55)
print("  RESUMO — BLOCO 2")
print("=" * 55)
print(f"  Média produtividade:  {media_prod:.2f} sacas/ha")
print(f"  Desvio padrão:        {dp_prod:.2f} sacas/ha")
print(f"  Correlação (r):       {r_chuva_prod:.4f}")
print(f"  P-valor:              {p_chuva_prod:.4f}")
print(f"  Conclusão:            correlação {forca}, {significancia}.")
print("=" * 55)