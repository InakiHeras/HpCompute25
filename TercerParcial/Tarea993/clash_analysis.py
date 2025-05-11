import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from elasticsearch import Elasticsearch
from itertools import combinations
from collections import Counter

es = Elasticsearch("http://localhost:9200", verify_certs=False)
index_name = "clashroyale_2025"

os.makedirs("docs", exist_ok=True)

# Extraer todos los documentos
res = es.search(
    index=index_name,
    query={"match_all": {}},
    size=1000
)
df = pd.DataFrame([doc["_source"] for doc in res["hits"]["hits"]])

# Asegurar que las columnas relevantes existan
if "Card" not in df.columns or "maxLevel" not in df.columns:
    raise ValueError("Faltan columnas requeridas en los datos: 'card_name' o 'card_level'.")

# GRÁFICO 1: Top 10 cartas con mayor Win Rate
def plot_top_winrate(df, top_n=10):
    top_winrate = df[['Card', 'Win Rate']].sort_values(by='Win Rate', ascending=False).head(top_n)
    plt.figure(figsize=(8, 5))
    plt.barh(top_winrate['Card'][::-1], top_winrate['Win Rate'][::-1], color='green')
    plt.xlabel("Tasa de victoria")
    plt.title(f"Top {top_n} cartas con mayor Win Rate")
    plt.tight_layout()
    plt.savefig("docs/1_top_winrate.png")
    plt.close()

# GRÁFICO 2: Elixir vs Win Rate
def plot_elixir_vs_winrate(df):
    plt.figure(figsize=(8, 5))
    plt.scatter(df['elixirCost'], df['Win Rate'], alpha=0.7, color='orange')
    plt.xlabel("Costo de Elixir")
    plt.ylabel("Win Rate")
    plt.title("Relación entre elixir y tasa de victoria")
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.savefig("docs/2_elixir_vs_winrate.png")
    plt.close()

# GRÁFICO 3: Uso vs Win Rate (tamaño = nivel máximo)
def plot_usage_vs_winrate(df):
    plt.figure(figsize=(8, 5))
    scatter = plt.scatter(df['Usage'], df['Win Rate'], s=df['maxLevel']*10, alpha=0.6, c=df['elixirCost'], cmap='viridis')
    plt.xlabel("Uso (%)")
    plt.ylabel("Win Rate")
    plt.title("Uso vs Win Rate (tamaño = maxLevel)")
    cbar = plt.colorbar(scatter)
    cbar.set_label("Costo de Elixir")
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.savefig("docs/3_uso_winrate_bubble.png")
    plt.close()

# GRÁFICO 4: Promedio de elixir por rareza
def plot_elixir_by_rarity(df):
    if 'rarity' in df.columns and 'elixirCost' in df.columns:
        rarity_elixir = df.groupby('rarity')['elixirCost'].mean().sort_values()
        plt.figure(figsize=(8, 5))
        rarity_elixir.plot(kind='bar', color='purple')
        plt.ylabel("Promedio de elixir")
        plt.title("Costo promedio de elixir por rareza")
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.savefig("docs/4_elixir_por_rareza.png")
        plt.close()

plot_top_winrate(df)
plot_elixir_vs_winrate(df)
plot_usage_vs_winrate(df)
plot_elixir_by_rarity(df)