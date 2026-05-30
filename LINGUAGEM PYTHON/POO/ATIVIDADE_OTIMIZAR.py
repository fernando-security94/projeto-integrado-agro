# Atividade de Avaliação e Otimização de Modelo
# Aplicar métricas de avaliação AUC-ROC
# Construir e interpretar a matriz de confusão
# Calcular e analisar métricas como Precision, Recall e f1-score
# Otimizar um modelo de classificação com base nas métricas avaliadas

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, roc_curve, confusion_matrix, classification_report
from sklearn.datasets import make_classification

# Geração do dataset
X, y = make_classification(
    n_samples=1000, n_features=10, n_informative=5, n_redundant=2,
    random_state=42, n_classes=2
)

# Dividir as variáveis em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(f'Treino: {X_train.shape}, Teste: {X_test.shape}\n\n')


# Treinamento do modelo
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Previsões de probabilidades
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]
# print(f'Previsões: {y_pred}\n')
# print(f'Probabilidades: {y_proba}\n')


# AUC e curva ROC
# Calculo de AUC
auc_score = roc_auc_score(y_test, y_proba)
print(f'AUC: {auc_score:.2f}\n')

# Plotagem da curva ROC
fpr, tpr, _ = roc_curve(y_test, y_proba)
plt.figure(figsize=(8,6))
plt.plot(fpr, tpr, label=f'AUC = {auc_score:.2f}')
plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
plt.xlabel('Taxa de Falsos Positivos')
plt.ylabel('Taxa de Verdadeiros Positivos')
plt.title('Curva ROC')
plt.tight_layout()
plt.legend()
plt.show()

# Plotagem da matriz de confusão
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Classe 0', 'Classe 1'], yticklabels=['Classe 0', 'Classe 1'])
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.tight_layout()
plt.show()


# Aplicação de Precision, Recall e F1-Score
report = classification_report(y_test, y_pred, target_names=['Classe 0', 'Classe 1'])
print("Resultado do report:")
print(report)

# Comparação de Thresholds
thresholds = np.arange(0.1, 1.0, 0.1)
for threshold in thresholds:
    y_pred_threshold = (y_proba >= threshold).astype(int)
    print(f'Threshold: {threshold:.1f}')
    print(confusion_matrix(y_test, y_pred_threshold))
    print(classification_report(y_test, y_pred_threshold, target_names=['Class 0', 'Class 1']))
    print("-" * 50)


'''
Responda às seguintes perguntas:
1) Qual foi o valor da AUC? O que ele indica sobre o modelo?
R: AUC: 0.99 e indica que, por estar muito próximo de 1.0, que o modelo consegue
distinguir muito bem entre as classes 0 e 1, com capacidade de separação ótima.

2) A matriz de confusão mostra um bom equilíbrio entre classes?
R: Apesar do modelo apresentar 8 falsos positivos na classe 0 e 10 falsos negativos na classe 1,
a performance pode ser considerada equilibrada por ter um número próximo de erros, mas ainda pode ser otimizada.

3) Quais são os valores de Precision, Recall e F1-Score para a Classe 1?
R: Precision: 0.94 | Recall: 0.93 | F1-Score: 0.94
Com taxas de erro de 6%, 7% ,respectivamente, o modelo apresenta bom rendimento
em classificar a classe 1, com leve tendência de perda no Recall, porem, o F1-Score reforça
o bom equilibrio entre as duas métricas.
4) Como a mudança do threshold afeta a performance do modelo?
R: A alteração do threshold modifica o ponto de corte usado 
para classificar uma amostra como Classe 1. 
Thresholds mais baixos aumentam o recall, mas reduzem a precision, 
enquanto thresholds mais altos fazem o oposto. 
Testar diferentes valores permite ajustar o modelo conforme o objetivo da tarefa 
(ex: minimizar falsos negativos ou falsos positivos).

5) Baseado nos resultados, qual threshold parece mais adequado?
R: Pensando em manter equilibrio e uma alta perfomance geral, 
o threshold 0.5 com resultados 0.94 | 0.93 | 0.94 parece ser mais adequado, 
por ter apresentado um bom desempenho nas duas métricas.



'''