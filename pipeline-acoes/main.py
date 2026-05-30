from src.extract import extrair_cotacoes
from src.transform import transformar
from src.load import carregar
from src.visualize import gerar_graficos

# Acoes que queremos analisar
TICKERS = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "WEGE3.SA"]

if __name__ == "__main__":
    print("=== INICIANDO PIPELINES ===\n")

    df_raw = extrair_cotacoes(TICKERS, periodo="6mo")
    df_transformed = transformar(df_raw)
    carregar(df_transformed)
    gerar_graficos()

    print("\n=== PIPELINE CONCLUIDO ===")