import time
import pandas as pd
from etl import executar_etl
from elt import executar_elt


def medir_performance(pedidos: pd.DataFrame, crm: pd.DataFrame) -> dict:
    """
    Mede o tempo de execução de cada abordagem e retorna os resultados.
    Os prints das etapas intermediárias são suprimidos durante a medição.
    """
    import io
    import sys

    # Suprime os prints intermediários durante a medição
    _stdout = sys.stdout
    sys.stdout = io.StringIO()

    inicio_etl = time.perf_counter()
    executar_etl(pedidos, crm)
    fim_etl = time.perf_counter()

    inicio_elt = time.perf_counter()
    executar_elt(pedidos, crm)
    fim_elt = time.perf_counter()

    sys.stdout = _stdout  # restaura o stdout

    return {
        'tempo_etl': fim_etl - inicio_etl,
        'tempo_elt': fim_elt - inicio_elt,
    }


def exibir_performance(tempos: dict) -> None:
    separador = "-" * 38
    print(separador)
    print(f"  {'Abordagem':<12} {'Tempo (s)':>10}  {'Mais rápido?':>12}")
    print(separador)

    etl = tempos['tempo_etl']
    elt = tempos['tempo_elt']
    mais_rapido_etl = "✔" if etl <= elt else ""
    mais_rapido_elt = "✔" if elt < etl else ""

    print(f"  {'ETL':<12} {etl:>10.6f}  {mais_rapido_etl:>12}")
    print(f"  {'ELT':<12} {elt:>10.6f}  {mais_rapido_elt:>12}")
    print(separador)
    print()
