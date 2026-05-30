# Código desenvolvido seguindo os procedimentos
# do roteiro de aula
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generating random data
X, _ = make_blobs(n_samples=200, centers=3, cluster_std=1.5, random_state=42)

# Adjusting to positive values
X = X - X.min(axis=0)  # extract the minimum from each column

# creating DataFrame
df = pd.DataFrame(X, columns=["Renda Mensal", "Gasto Mensal"])
print(df.head())


# Applying K-means (k=3)
k_means = KMeans(n_clusters=3, random_state=42, n_init=10)
k_means.fit(df)
df["Cluster"] = k_means.labels_



# Scatter plot before clustering
plt.figure(figsize=(8, 5))
plt.scatter(df["Renda Mensal"], df["Gasto Mensal"], color="#2196F3", alpha=0.6,
            edgecolors="white", linewidths=0.5, s=60)
plt.xlabel("Renda Mensal (R$)", fontsize=12)
plt.ylabel("Gasto Mensal (R$)", fontsize=12)
plt.title("Dispersão dos Dados – Antes da Clusterização", fontsize=13, fontweight="bold")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("grafico_dispersao.png", dpi=150)
plt.show()


# Plot with clusters and centroids
colors = {0: '#E53935', 1: '#43A047', 2: '#1E88E5'}
labels_map = {0: 'Econômicos Engajados', 1: 'Conservadores Frugais', 2: 'Consumidores Premium'}
 
fig, ax = plt.subplots(figsize=(9, 6))
for c in sorted(df['Cluster'].unique()):
    sub = df[df['Cluster'] == c]
    ax.scatter(sub['Renda Mensal'], sub['Gasto Mensal'],
               color=colors[c], label=labels_map[c],
               alpha=0.70, edgecolors='white', linewidths=0.5, s=70, zorder=3)
 
# Centroides em X amarelo com borda preta
cx = k_means.cluster_centers_
for i, (x, y) in enumerate(cx):
    ax.scatter(x, y, marker='X', s=600, color='yellow',
               edgecolors='black', linewidths=2.5, zorder=10,
               label='Centroide' if i == 0 else '_nolegend_')
 
ax.set_xlabel('Renda Mensal (R$)', fontsize=13)
ax.set_ylabel('Gasto Mensal (R$)', fontsize=13)
ax.set_title('Clusterização de Clientes – K-Means (K=3)', fontsize=14, fontweight='bold')
ax.legend(fontsize=10, loc='upper left', framealpha=0.9)
ax.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('grafico_clusters.png', dpi=150)
plt.show()



# elbow coeficient
inertias = []
ks = range(1, 9)
for k in ks:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(df[['Renda Mensal', 'Gasto Mensal']])
    inertias.append(km.inertia_)
 
plt.figure(figsize=(7, 4.5))
plt.plot(list(ks), inertias, marker='o', color='#1E88E5', linewidth=2, markersize=8)
plt.axvline(x=3, color='#E53935', linestyle='--', linewidth=1.5, label='K=3 (escolhido)')
plt.xlabel('Número de Clusters (K)', fontsize=12)
plt.ylabel('Inércia (WCSS)', fontsize=12)
plt.title('Método do Cotovelo – Escolha de K', fontsize=13, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig('grafico_elbow.png', dpi=150)
plt.show()
