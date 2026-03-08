import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações iniciais
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Carregamento do arquivo CSV
df = pd.read_csv("data/datatran2024.csv", sep=";", encoding="latin1")

# ===========================
# CLASSIFICAÇÃO DOS ACIDENTES
# ===========================
classificacao = df["classificacao_acidente"].value_counts()
percent = classificacao / classificacao.sum() * 100

print("== CLASSIFICAÇÃO DOS ACIDENTES ==")
for tipo in classificacao.index:
    print(f"{tipo}: {classificacao[tipo]} ({percent[tipo]:.1f}%)")

# ===========================
# TIPOS DE ACIDENTES
# ===========================
tipos_acidentes = df["tipo_acidente"].value_counts()

print("\n== TIPOS DE ACIDENTES (TODOS) ==")
for tipo, valor in tipos_acidentes.items():
    print(f"{tipo}: {valor}")

# ===========================
# GRÁFICO 1: Classificação dos Acidentes
# ===========================
plt.figure()
sns.barplot(x=classificacao.index, y=classificacao.values, palette="Set2")
plt.title("Classificação dos Acidentes")
plt.xlabel("Tipo de Classificação")
plt.ylabel("Número de Acidentes")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("images/grafico_classificacao_acidentes.png", dpi=300)
plt.show()

# ===========================
# GRÁFICO 2: Top 10 Tipos de Acidente
# ===========================
top10 = tipos_acidentes.nlargest(10)

plt.figure()
sns.barplot(y=top10.index, x=top10.values, palette="Blues_d")
plt.title("Top 10 Tipos de Acidentes")
plt.xlabel("Número de Ocorrências")
plt.ylabel("Tipo de Acidente")
plt.tight_layout()
plt.savefig("images/grafico_top_10_acidentes.png", dpi=300)
plt.show()