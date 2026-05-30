import pandas as pd



def transformar(df: pd.DataFrame) -> pd.DataFrame:
    print("[TRANSFORM] Calculando metricas...")

    df = df.sort_values(["ticker", "data"]).copy()

    # Retorno diário
    df["retorno_diario"] = (
        df.groupby("ticker")["preco_fechamento"]
        .pct_change() * 100
    )

    # Remove nulos antes de calcular volatilidade
    df = df.dropna(subset=["retorno_diario"])

    # Médias móveis
    df["media_movel_7d"] = (
        df.groupby("ticker")["preco_fechamento"]
        .transform(lambda x: x.rolling(7).mean())
    )

    df["media_movel_30d"] = (
        df.groupby("ticker")["preco_fechamento"]
        .transform(lambda x: x.rolling(30).mean())
    )

    # Volatilidade
    df["volatilidade_21d"] = (
        df.groupby("ticker")["retorno_diario"]
        .transform(lambda x: x.rolling(21).std())
    )

    df = df.dropna()

    print(f"[TRANSFORM] {len(df)} registros após transformação.")
    return df