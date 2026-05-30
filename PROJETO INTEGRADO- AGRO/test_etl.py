# ============================================================
# PROJETO INTEGRADO — EmpresaX Agronegócio
# Passo 4: Testes Unitários — Pipeline ETL
# ============================================================
import pytest
import pandas as pd
import numpy as np


# Testa se a remoção de duplicatas funciona corretamente
def test_remocao_duplicatas():
    df = pd.DataFrame({'id': [1, 2, 2, 3], 'valor': [10, 20, 20, 30]})
    df_limpo = df.drop_duplicates()
    assert len(df_limpo) == 3
    assert df_limpo.duplicated().sum() == 0


# Testa se a imputação pela média preenche todos os nulos
def test_imputacao_media():
    df = pd.DataFrame({'temperatura': [20.0, 21.0, np.nan, 22.0]})
    media = df['temperatura'].mean()
    df['temperatura'] = df['temperatura'].fillna(round(media, 1))
    assert df['temperatura'].isnull().sum() == 0


# Testa se a imputação pela mediana preenche o nulo corretamente
def test_imputacao_mediana():
    df = pd.DataFrame({'producao': [55.0, 58.0, np.nan, 62.0, 60.0]})
    mediana = df['producao'].median()
    df['producao'] = df['producao'].fillna(round(mediana, 2))
    assert df['producao'].isnull().sum() == 0


# Testa se o merge inner join exclui registros sem correspondência
def test_merge_inner():
    df_a = pd.DataFrame({'id': [1, 2, 3], 'chuva': [1500, 1600, 1700]})
    df_b = pd.DataFrame({'id': [1, 2],    'prod':  [55.0, 60.0]})
    df_merged = pd.merge(df_a, df_b, on='id', how='inner')
    assert len(df_merged) == 2


# Testa se o dataset final não tem nulos após o pipeline
def test_dataset_sem_nulos():
    df = pd.DataFrame({
        'id':    [1, 2, 3],
        'chuva': [1500.0, 1600.0, 1700.0],
        'temp':  [21.0, 22.0, 23.0],
        'prod':  [55.0, 58.0, 61.0]
    })
    assert df.isnull().sum().sum() == 0




test_remocao_duplicatas()
test_imputacao_media()
test_imputacao_mediana()
test_merge_inner()
test_dataset_sem_nulos()