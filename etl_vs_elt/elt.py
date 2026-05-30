import pandas as pd


def executar_elt(pedidos: pd.DataFrame, crm: pd.DataFrame) -> pd.DataFrame:
    """
    Processo ELT — carrega os dados brutos e transforma DEPOIS.

    Etapas:
        1. (Carregar)  → dados brutos vão direto ao destino (simulado com .copy())
        2. Integra     → faz o merge dentro do ambiente de destino
        3. Transforma  → calcula valor_total já no destino
        4. Agrega      → soma os valores por cliente
    """
    # 1. "Carga" dos dados brutos (sem transformação prévia)
    pedidos_brutos = pedidos.copy()
    crm_brutos = crm.copy()

    # 2. Integração dentro do ambiente de destino
    resultado = pd.merge(pedidos_brutos, crm_brutos, on='id_cliente')

    # 3. Transformação (depois do carregamento)
    resultado['valor_total'] = resultado['quantidade'] * resultado['preco_unitario']

    # 4. Agregação por cliente
    resultado = (
        resultado
        .groupby(['id_cliente', 'nome', 'email'])
        .agg({'valor_total': 'sum'})
        .reset_index()
        .sort_values('nome')
    )

    return resultado
