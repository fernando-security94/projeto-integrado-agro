import yfinance as yf
import pandas as pd

def extrair_cotacoes(tickers: list, periodo: str = "6mo") -> pd.DataFrame:
    """
    Baixa cotacoes historicas de acoes da B3.
    tickers: lista de codigos: ["PETR4.SA", "VALE3.SA"]
    perido: "1mo", "3mo", "6mo", "1y"
    """
    print(f"[EXTRACT] Baixando os dados de {tickers}...")
    
    dados = yf.download(tickers, period=periodo, auto_adjust=True)

    # Pega somente o preco de fechamento
    fechamento = dados["Close"]

    # Transforma em formato longo (long format) - melhor para analise
    df = fechamento.reset_index().melt(
        id_vars="Date",
        var_name="ticker",
        value_name="preco_fechamento"
    )

    df.rename(columns={"Date": "data"}, inplace=True)
    df["data"] = pd.to_datetime(df["data"])
    df = df.dropna()

    print(f"[EXTRACT] {len(df)} registros extraidos")
    return df
