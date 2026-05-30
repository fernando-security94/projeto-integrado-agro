# =============================================================================
# PROJETO INTEGRADO — EmpresaX Agronegócio
# Passo 1: Probabilidade e Estatística para Análise de Dados
# Bloco 1: Simulação dos Dados
# =============================================================================
# OBJETIVO DESTE BLOCO:
#   Gerar um dataset simulado com 50 propriedades agrícolas do Paraná,
#   contendo as variáveis: chuva (mm), temperatura média (°C) e
#   produtividade (sacas/hectare).
#
# POR QUE SIMULAR?
#   Como não temos acesso direto ao banco de dados real da EmpresaX,
#   simulamos dados com parâmetros baseados em médias reais do Paraná.
#   Isso é uma prática comum em ciência de dados para desenvolver e
#   testar pipelines antes dos dados reais estarem disponíveis.
# =============================================================================


# -----------------------------------------------------------------------------
# IMPORTAÇÃO DAS BIBLIOTECAS
# -----------------------------------------------------------------------------
# numpy  → operações numéricas e geração de números aleatórios
# pandas → estruturar os dados em tabela (DataFrame), similar ao data.frame do R
import numpy as np
import pandas as pd


# -----------------------------------------------------------------------------
# SEED DE REPRODUTIBILIDADE
# -----------------------------------------------------------------------------
# A seed garante que, toda vez que o script rodar, os mesmos números
# aleatórios sejam gerados — essencial para que outros possam reproduzir
# exatamente os mesmos resultados.
#
# Em R você faria: set.seed(42)
# Em Python/NumPy: np.random.seed(42)
np.random.seed(42)


# -----------------------------------------------------------------------------
# PARÂMETROS DA SIMULAÇÃO
# -----------------------------------------------------------------------------
# Definimos os parâmetros em variáveis separadas para facilitar ajustes.
# Se quisermos mudar a média da chuva, alteramos só aqui — não precisamos
# caçar o número espalhado pelo código.

N_PROPRIEDADES = 50          # número de propriedades a simular

# Chuva (mm) — média anual do Paraná
CHUVA_MEDIA = 1600           # mm — valor de referência para o Paraná
CHUVA_DESVIO = 200           # desvio padrão: a variação típica entre propriedades

# Temperatura média anual (°C)
TEMP_MEDIA = 21.0            # °C — média anual típica do Paraná
TEMP_DESVIO = 2.0            # desvio padrão: variação entre regiões (norte/sul do PR)

# Produtividade de soja (sacas/hectare)
PROD_MEDIA = 58.0            # sacas/ha — média do Paraná (fonte: CONAB/EMBRAPA)
PROD_DESVIO = 8.0            # desvio padrão: variação entre propriedades


# -----------------------------------------------------------------------------
# GERAÇÃO DOS DADOS ALEATÓRIOS
# -----------------------------------------------------------------------------
# np.random.normal() gera números seguindo uma distribuição normal (gaussiana).
# Parâmetros:
#   loc   = média da distribuição (o centro da "curva em sino")
#   scale = desvio padrão (quão "espalhados" os valores ficam)
#   size  = quantos valores gerar

chuva = np.random.normal(loc=CHUVA_MEDIA, scale=CHUVA_DESVIO, size=N_PROPRIEDADES)

temperatura = np.random.normal(loc=TEMP_MEDIA, scale=TEMP_DESVIO, size=N_PROPRIEDADES)

# A produtividade não depende só do acaso — na realidade, mais chuva e
# temperatura adequada tendem a aumentar a produtividade.
# Vamos modelar isso adicionando uma influência positiva da chuva
# e da temperatura sobre a produtividade:
#
#   efeito_chuva: a cada 100mm acima da média, produtividade sobe ~1 saca/ha
#   efeito_temp:  a cada 1°C acima da média, produtividade sobe ~0.8 saca/ha
#   ruido:        variação aleatória residual (fatores não explicados)
#
# Isso cria uma correlação realista entre as variáveis — importante
# para os cálculos do Bloco 2.

efeito_chuva = (chuva - CHUVA_MEDIA) * 0.01    # coeficiente: 0.01 saca por mm
efeito_temp  = (temperatura - TEMP_MEDIA) * 0.8 # coeficiente: 0.8 saca por °C
ruido        = np.random.normal(0, 3, N_PROPRIEDADES)  # ruído aleatório

produtividade = PROD_MEDIA + efeito_chuva + efeito_temp + ruido

# Garantir que nenhum valor seja negativo ou absurdo
# (np.clip limita os valores entre um mínimo e um máximo)
chuva         = np.clip(chuva, 800, 2400)
temperatura   = np.clip(temperatura, 15, 28)
produtividade = np.clip(produtividade, 30, 90)


# -----------------------------------------------------------------------------
# MONTAGEM DO DATAFRAME
# -----------------------------------------------------------------------------
# Um DataFrame do Pandas é equivalente ao data.frame do R.
# Organizamos os arrays em colunas com nomes claros.

df = pd.DataFrame({
    'propriedade_id': range(1, N_PROPRIEDADES + 1),  # ID de 1 a 50
    'chuva_mm':       np.round(chuva, 1),            # arredondado para 1 casa decimal
    'temperatura_c':  np.round(temperatura, 1),
    'produtividade_sacas_ha': np.round(produtividade, 2)
})


# -----------------------------------------------------------------------------
# VISUALIZAÇÃO RÁPIDA DOS DADOS
# -----------------------------------------------------------------------------
print("=" * 55)
print("  DATASET SIMULADO — 50 PROPRIEDADES AGRÍCOLAS DO PARANÁ")
print("=" * 55)

# .head(10) mostra as 10 primeiras linhas — equivalente ao head() do R
print("\nPrimeiras 10 linhas do dataset:")
print(df.head(10).to_string(index=False))

# .describe() gera um resumo estatístico completo — parecido com o summary() do R
print("\nResumo estatístico do dataset:")
print(df.describe().round(2).to_string())


# -----------------------------------------------------------------------------
# EXPORTAÇÃO DO CSV
# -----------------------------------------------------------------------------
# Salvamos o dataset para ser reutilizado nos próximos blocos e passos.
# index=False evita que o Pandas adicione uma coluna de índice desnecessária.

CAMINHO_CSV = "dados_agricolas_parana.csv"
df.to_csv(CAMINHO_CSV, index=False, encoding='utf-8')

print(f"\nDataset salvo em: {CAMINHO_CSV}")
print(f"Total de registros gerados: {len(df)}")