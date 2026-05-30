import pandas as pd


def extrair_pedidos() -> pd.DataFrame:
    """Simula a extração de dados do sistema de pedidos."""
    dados = pd.DataFrame({
        'id_cliente':     [1,          2,       3,         1      ],
        'produto':        ['Notebook', 'Mouse', 'Monitor', 'Mouse'],
        'quantidade':     [1,          2,       1,         3      ],
        'preco_unitario': [3000.00,    100.00,  900.00,    100.00 ],
    })
    return dados


def extrair_crm() -> pd.DataFrame:
    """Simula a extração de dados do sistema de CRM."""
    dados = pd.DataFrame({
        'id_cliente': [1,               2,                 3                ],
        'nome':       ['Ana',           'Bruno',           'Carla'          ],
        'email':      ['ana@email.com', 'bruno@email.com', 'carla@email.com'],
    })
    return dados
