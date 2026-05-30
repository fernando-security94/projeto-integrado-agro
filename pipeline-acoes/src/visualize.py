import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os

def gerar_graficos(db_path: str = "data/acoes.db"):
    engine = create_engine(f"sqlite:///{db_path}")
    df = pd.read_sql("SELECT * FROM cotacoes", con=engine)
    df["data"] = pd.to_datetime(df["data"])

    tickers = df["ticker"].unique()
    os.makedirs("data", exist_ok=True)


    # ── Gráfico 1: Preço de Fechamento ──────────────────────────────
    fig, ax = plt.subplots(figsize=(14, 6))
    for ticker in tickers:
        subset = df[df["ticker"] == ticker]
        ax.plot(subset["data"], subset["preco_fechamento"], label=f"{ticker} - Preco", linewidth=1.5)
        ax.plot(subset["data"], subset["media_movel_30d"], linestyle="--", alpha=0.6, label=f"{ticker} - MM30")
    ax.set_title("Preco de Fechamento e Media Movel 30 dias", fontsize=13, fontweight="bold")
    ax.set_ylabel("R$")
    ax.legend(fontsize=8, ncol=2, loc="upper left")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("data/grafico_preco.png", dpi=150)
    plt.show()


    # ── Gráfico 2: Retorno Diário ────────────────────────────────────
    fig, ax = plt.subplots(figsize=(14, 6))
    for ticker in tickers:
        subset = df[df["ticker"] == ticker]
        ax.plot(subset["data"], subset["retorno_diario"], label=ticker, alpha=0.8, linewidth=1)
    ax.axhline(0, color="black", linewidth=1, linestyle="--")
    ax.set_title("Retorno Diario (%)", fontsize=13, fontweight="bold")
    ax.set_ylabel("%")
    ax.legend(fontsize=9, ncol=2, loc="upper left")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("data/grafico_retorno.png", dpi=150)
    plt.show()


    # ── Gráfico 3: Volatilidade ──────────────────────────────────────
    fig, ax = plt.subplots(figsize=(14, 6))
    for ticker in tickers:
        subset = df[df["ticker"] == ticker]
        ax.plot(subset["data"], subset["volatilidade_21d"], label=ticker, linewidth=1.5)
    ax.set_title("Volatilidade - Desvio Padrao 21 dias", fontsize=13, fontweight="bold")
    ax.set_ylabel("%")
    ax.legend(fontsize=9, ncol=2, loc="upper left")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("data/grafico_volatilidade.png", dpi=150)
    plt.show()

    print("[VIZ] Graficos salvos em data/")