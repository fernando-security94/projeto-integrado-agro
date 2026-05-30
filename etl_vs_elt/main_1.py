"""
ETL vs ELT — Pipeline de Dados
================================
Disciplina : Engenharia de Dados
Aula       : A4 — Extração e Processamento

Execute com:
    python main.py
"""

from dados import extrair_pedidos, extrair_crm
from etl   import executar_etl
from elt   import executar_elt
from performance import medir_performance, exibir_performance
from visualizacao import gerar_grafico

def imprimir_dataframe(titulo: str, df) -> None:
    print(f"\n{titulo}")
    print("-" * len(titulo))
    print(df.to_string(index=False))
    print()


def main():
    # --------------------------------------------------
    # Extração dos dados brutos
    # --------------------------------------------------
    pedidos = extrair_pedidos()
    crm     = extrair_crm()

    imprimir_dataframe("Dados brutos — Pedidos", pedidos)
    imprimir_dataframe("Dados brutos — CRM", crm)

    # --------------------------------------------------
    # Processo ETL
    # --------------------------------------------------
    resultado_etl = executar_etl(pedidos, crm)
    imprimir_dataframe("Resultado ETL", resultado_etl)

    # --------------------------------------------------
    # Processo ELT
    # --------------------------------------------------
    resultado_elt = executar_elt(pedidos, crm)
    imprimir_dataframe("Resultado ELT", resultado_elt)

    tempos = medir_performance(pedidos, crm)
    exibir_performance(tempos)

    gerar_grafico(resultado_etl, resultado_elt)

if __name__ == "__main__":
    main()
