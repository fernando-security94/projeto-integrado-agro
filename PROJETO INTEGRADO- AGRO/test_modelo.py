# ============================================================
# PROJETO INTEGRADO — EmpresaX Agronegócio
# Passo 4: Testes Unitários — Modelo de Regressão Linear
# ============================================================
import pytest
import numpy as np
from sklearn.linear_model import LinearRegression


# Testa se o modelo retorna R² acima do mínimo aceitável
def test_r2_aceitavel():
    X = np.array([[1500, 21], [1600, 22], [1700, 23], [1800, 24]])
    y = np.array([55.0, 58.0, 61.0, 64.0])
    modelo = LinearRegression().fit(X, y)
    r2 = modelo.score(X, y)
    assert r2 > 0.70


# Testa se a predição retorna valor positivo
def test_predicao_positiva():
    X = np.array([[1500, 21], [1600, 22], [1700, 23]])
    y = np.array([55.0, 58.0, 61.0])
    modelo = LinearRegression().fit(X, y)
    pred = modelo.predict([[1700, 22]])[0]
    assert pred > 0


# Testa se o modelo aceita exatamente 2 features como entrada
def test_numero_features():
    X = np.array([[1500, 21], [1600, 22], [1700, 23]])
    y = np.array([55.0, 58.0, 61.0])
    modelo = LinearRegression().fit(X, y)
    assert modelo.coef_.shape[0] == 2


# Testa se MAE é calculado corretamente
def test_mae_manual():
    reais    = np.array([55.0, 60.0, 65.0])
    preditos = np.array([54.0, 61.0, 64.0])
    mae = np.mean(np.abs(reais - preditos))
    assert round(mae, 2) == 1.0



test_r2_aceitavel()