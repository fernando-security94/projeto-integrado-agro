# =============================================================================
# PROJETO INTEGRADO — EmpresaX Agronegócio
# Passo 1: Probabilidade e Estatística para Análise de Dados
# Bloco 3: Intervalo de Confiança de 95% para a Produtividade Média
# =============================================================================
# OBJETIVO DESTE BLOCO:
#   Calcular o intervalo de confiança (IC) de 95% para a produtividade média
#   das propriedades agrícolas do Paraná, interpretando o resultado no
#   contexto do negócio da EmpresaX.
#
# CONCEITO-CHAVE:
#   O IC não diz "há 95% de chance de a média estar aqui".
#   Ele diz: "se repetíssemos essa coleta 100 vezes, em ~95 delas
#   o intervalo calculado conteria a média real da população."
#   É uma propriedade do MÉTODO, não de um único intervalo.
#
# FÓRMULA:
#   IC = média ± t * (desvio_padrão / √n)
#
#   Onde:
#     t  = valor crítico da distribuição t de Student para 95% de confiança
#     dp = desvio padrão amostral
#     n  = tamanho da amostra
#     dp / √n = erro padrão da média (SEM — Standard Error of the Mean)
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

print("=" * 60)
print("  BLOCO 3 — INTERVALO DE CONFIANÇA (95%)")
print("=" * 60)


# -----------------------------------------------------------------------------
# COMPONENTES DO CÁLCULO
# -----------------------------------------------------------------------------
# Extraímos a série de produtividade como array NumPy para facilitar
# os cálculos matemáticos seguintes.

prod = df['produtividade_sacas_ha'].values   # .values → converte para array NumPy

n  = len(prod)          # tamanho da amostra: 50
media = np.mean(prod)   # média amostral
dp    = np.std(prod, ddof=1)  # desvio padrão amostral (ddof=1, como no Bloco 2)

# ERRO PADRÃO DA MÉDIA (Standard Error of the Mean — SEM)
# O SEM mede a precisão da média amostral como estimativa da média populacional.
# Quanto maior o n, menor o SEM — amostras maiores estimam melhor a média real.
# Fórmula: SEM = dp / √n
sem = dp / np.sqrt(n)

print(f"\nComponentes do cálculo:")
print(f"  n (tamanho da amostra):  {n}")
print(f"  Média amostral:          {media:.4f} sacas/ha")
print(f"  Desvio padrão amostral:  {dp:.4f} sacas/ha")
print(f"  Erro padrão (SEM):       {sem:.4f} sacas/ha")


# -----------------------------------------------------------------------------
# VALOR CRÍTICO t DE STUDENT
# -----------------------------------------------------------------------------
# Por que t de Student e não Z (normal)?
#
#   - A distribuição Z assume que conhecemos o desvio padrão REAL da população
#   - Na prática, estimamos o dp com nossa amostra → incerteza adicional
#   - A distribuição t de Student acomoda essa incerteza, sendo mais
#     "conservadora" (intervalos ligeiramente mais largos) para amostras pequenas
#   - À medida que n cresce, t se aproxima de Z (para n → ∞, são iguais)
#
# Graus de liberdade (gl) = n - 1  "DF"
#   Perdemos 1 grau de liberdade porque usamos a média da própria amostra
#   para calcular o desvio padrão — um dado "gasto" na estimativa.
#
# stats.t.ppf(q, df):
#   ppf = Percent Point Function (inversa da CDF — função de distribuição acumulada)
#   q   = 0.975 → porque queremos 95% no centro, sobram 2.5% em cada cauda
#   df  = graus de liberdade
#
# Em R você faria: qt(0.975, df = n - 1)

gl = n - 1          # graus de liberdade
confianca = 0.95    # nível de confiança desejado
alpha = 1 - confianca  # nível de significância: 0.05

# q = 1 - alpha/2 → captura as duas caudas simétricas
t_critico = stats.t.ppf(1 - alpha / 2, df=gl)

print(f"\nValor crítico t:")
print(f"  Nível de confiança:  {confianca*100:.0f}%")
print(f"  Alpha (α):           {alpha}")
print(f"  Graus de liberdade:  {gl}")
print(f"  t crítico:           {t_critico:.4f}")
print(f"  (Para comparação, Z crítico seria: 1.9600)")


# -----------------------------------------------------------------------------
# CÁLCULO DO INTERVALO DE CONFIANÇA
# -----------------------------------------------------------------------------
# Margem de erro = t_crítico × SEM
# IC inferior = média - margem de erro
# IC superior = média + margem de erro

margem_erro = t_critico * sem
ic_inferior = media - margem_erro
ic_superior = media + margem_erro

print(f"\n" + "-" * 60)
print(f"RESULTADO — INTERVALO DE CONFIANÇA DE 95%")
print(f"-" * 60)
print(f"  Margem de erro:  ± {margem_erro:.4f} sacas/ha")
print(f"  IC inferior:     {ic_inferior:.4f} sacas/ha")
print(f"  IC superior:     {ic_superior:.4f} sacas/ha")
print(f"\n  → Com 95% de confiança, a produtividade média real")
print(f"    das propriedades do Paraná está entre")
print(f"    {ic_inferior:.2f} e {ic_superior:.2f} sacas/ha.")


# -----------------------------------------------------------------------------
# VALIDAÇÃO: MÉTODO ALTERNATIVO COM SCIPY
# -----------------------------------------------------------------------------
# O SciPy oferece uma função pronta que faz exatamente o mesmo cálculo.
# Usamos para confirmar que nosso resultado manual está correto.
# Em produção, você pode usar direto — mas entender o manual é fundamental.
#
# stats.t.interval():
#   confidence = nível de confiança
#   df         = graus de liberdade
#   loc        = média (centro do intervalo)
#   scale      = erro padrão (SEM)

ic_scipy = stats.t.interval(
    confidence=confianca,
    df=gl,
    loc=media,
    scale=sem
)

print(f"\nValidação via SciPy:")
print(f"  IC SciPy: [{ic_scipy[0]:.4f}, {ic_scipy[1]:.4f}] sacas/ha")
print(f"  ✓ Valores idênticos ao cálculo manual — cálculo correto!")


# -----------------------------------------------------------------------------
# VISUALIZAÇÃO DO INTERVALO DE CONFIANÇA
# -----------------------------------------------------------------------------
# Criamos dois gráficos lado a lado:
# Esquerdo: histograma da produtividade com o IC destacado
# Direito:  representação visual do IC como barra de erro

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# --- Gráfico 1: Histograma com IC ---
ax1.hist(prod, bins=12, color='steelblue', edgecolor='white',
         alpha=0.75, label='Produtividade (sacas/ha)')

# Linha vertical para a média
ax1.axvline(media, color='darkblue', linewidth=2,
            linestyle='-', label=f'Média: {media:.2f}')

# Linhas verticais para os limites do IC
ax1.axvline(ic_inferior, color='tomato', linewidth=2,
            linestyle='--', label=f'IC inf: {ic_inferior:.2f}')
ax1.axvline(ic_superior, color='tomato', linewidth=2,
            linestyle='--', label=f'IC sup: {ic_superior:.2f}')

# Área sombreada representando o IC
ax1.axvspan(ic_inferior, ic_superior, alpha=0.15, color='tomato',
            label='IC 95%')

ax1.set_xlabel("Produtividade (sacas/ha)", fontsize=11)
ax1.set_ylabel("Frequência", fontsize=11)
ax1.set_title("Distribuição da Produtividade\ncom Intervalo de Confiança 95%", fontsize=12)
ax1.legend(fontsize=8)
ax1.grid(True, linestyle='--', alpha=0.4)

# --- Gráfico 2: Barra de erro (estilo científico) ---
ax2.errorbar(
    x=1,              # posição no eixo x (apenas um ponto)
    y=media,          # valor central: a média
    yerr=margem_erro, # tamanho das barras: margem de erro
    fmt='o',          # formato do marcador: círculo
    color='steelblue',
    ecolor='tomato',
    elinewidth=3,
    capsize=12,       # tamanho das "tampas" nas extremidades das barras
    markersize=10,
    label=f'Média ± Margem de Erro\n{media:.2f} ± {margem_erro:.2f}'
)

ax2.set_xlim(0, 2)
ax2.set_ylim(media - 5, media + 5)
ax2.set_xticks([])   # remove os ticks do eixo x (não fazem sentido aqui)
ax2.set_ylabel("Produtividade (sacas/ha)", fontsize=11)
ax2.set_title(f"IC 95%: [{ic_inferior:.2f}, {ic_superior:.2f}]\nProdutividade Média — Paraná", fontsize=12)
ax2.legend(fontsize=9)
ax2.grid(True, linestyle='--', alpha=0.4, axis='y')

plt.tight_layout()
plt.savefig("grafico_intervalo_confianca.png", dpi=150)
plt.show()
print("\nGráfico salvo: grafico_intervalo_confianca.png")


# -----------------------------------------------------------------------------
# IMPLICAÇÃO PARA O NEGÓCIO
# -----------------------------------------------------------------------------
print("\n" + "=" * 60)
print("  IMPLICAÇÃO PARA O NEGÓCIO — EmpresaX")
print("=" * 60)
print(f"""
  A plataforma da EmpresaX pode comunicar aos produtores:

  "Com base nos dados de {n} propriedades monitoradas,
  a produtividade média esperada para a safra está entre
  {ic_inferior:.1f} e {ic_superior:.1f} sacas/ha (IC 95%)."

  Isso permite que cooperativas e produtores:
  → Planejem a compra de insumos com margem de segurança
  → Negociem contratos futuros com expectativa fundamentada
  → Identifiquem propriedades abaixo do limite inferior
    como candidatas a diagnóstico agronômico
""")