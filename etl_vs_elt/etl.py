import pandas as pd


def executar_etl(pedidos: pd.DataFrame, crm: pd.DataFrame) -> pd.DataFrame:
    """
    Processo ETL — transforma os dados ANTES de carregar.

    Etapas:
        1. Transforma  → calcula valor_total
        2. Integra     → faz o merge com o CRM
        3. Agrega      → soma os valores por cliente
        4. (Carregar)  → em produção, aqui viria o INSERT no Data Warehouse
    """
    # 1. Transformação (antes do carregamento)
    pedidos = pedidos.copy()
    pedidos['valor_total'] = pedidos['quantidade'] * pedidos['preco_unitario']

    # 2. Integração com CRM
    resultado = pd.merge(pedidos, crm, on='id_cliente')

    # 3. Agregação por cliente
    resultado = (
        resultado
        .groupby(['id_cliente', 'nome', 'email'])
        .agg({'valor_total': 'sum'})
        .reset_index()
        .sort_values('nome')
    )

    return resultado
