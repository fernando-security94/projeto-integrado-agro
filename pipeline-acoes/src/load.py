import pandas as pd
from sqlalchemy import create_engine
import os  # adiciona essa linha

def carregar(df: pd.DataFrame, db_path: str = "data/acoes.db"):
    print("[LOAD] Salvando no banco de dados...")

    os.makedirs("data", exist_ok=True)  # adiciona essa linha

    engine = create_engine(f"sqlite:///{db_path}")

    df.to_sql("cotacoes", con=engine, if_exists="replace", index=False)

    print(f"[LOAD] Dados salvos em {db_path} na tabela 'cotacoes'.")