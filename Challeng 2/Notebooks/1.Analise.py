# ==================================================
# 1. IMPORTAÇÃO DAS BIBLIOTECAS
# ==================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ==================================================
# 2. LEITURA DA BASE
# ==================================================

# df = pd.read_csv('C:/Users/Aname/OneDrive/Desktop/Tech Challeng/Challeng 2/vinho-tech-challenge/WineQT.csv')
BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_DADOS = BASE_DIR / "vinho-tech-challenge" / "WineQT.csv"

df = pd.read_csv(CAMINHO_DADOS)

print("\n===== ESTRUTURA DA BASE =====")

print("Quantidade de registros:", df.shape[0])
print("Quantidade de colunas:", df.shape[1])

print("\nColunas disponíveis:")
print(df.columns.tolist())


# ==================================================
# 3. VISUALIZAÇÃO DOS DADOS
# ==================================================

print("\n===== PRIMEIROS REGISTROS =====")

print(df.head())

print("\n===== INFORMAÇÕES DAS COLUNAS =====")

df.info()

print("\n===== ESTATÍSTICAS DESCRITIVAS =====")

print(df.describe().round(2))


# ==================================================
# 4. VERIFICAÇÃO DA QUALIDADE DOS DADOS
# ==================================================

print("\n===== VALORES AUSENTES =====")

print(df.isnull().sum())

print("\nTotal de valores ausentes:")
print(df.isnull().sum().sum())

print("\n===== REGISTROS DUPLICADOS =====")

print(df.duplicated().sum())


# ==================================================
# 5. DISTRIBUIÇÃO DA QUALIDADE ORIGINAL
# ==================================================

print("\n===== DISTRIBUIÇÃO DAS NOTAS =====")

print(df["quality"].value_counts().sort_index())

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="quality",
    color="steelblue"
)

plt.title("Distribuição das Notas de Qualidade")
plt.xlabel("Nota de qualidade")
plt.ylabel("Quantidade de vinhos")

plt.tight_layout()
plt.show()


# ==================================================
# 6. CRIAÇÃO DA VARIÁVEL-ALVO
# ==================================================

df["quality_class"] = (
    df["quality"] >= 7
).astype(int)

print("\n===== CLASSIFICAÇÃO BINÁRIA =====")

print(df[["quality", "quality_class"]].head(10))


# ==================================================
# 7. BALANCEAMENTO DAS CLASSES
# ==================================================

quantidade_classes = (
    df["quality_class"]
    .value_counts()
    .sort_index()
)

percentual_classes = (
    df["quality_class"]
    .value_counts(normalize=True)
    .sort_index() * 100
)

print("\n===== QUANTIDADE POR CLASSE =====")

print(quantidade_classes)

print("\n===== PERCENTUAL POR CLASSE =====")

print(percentual_classes.round(2))


plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="quality_class",
    color="cornflowerblue"
)

plt.title("Distribuição das Classes de Qualidade")
plt.xlabel("Classe (0 = Baixa/Média, 1 = Alta)")
plt.ylabel("Quantidade de vinhos")

plt.tight_layout()
plt.show()


# ==================================================
# 8. DISTRIBUIÇÃO DAS VARIÁVEIS FÍSICO-QUÍMICAS
# ==================================================

variaveis = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol"
]

df[variaveis].hist(
    figsize=(15, 12),
    bins=20,
    edgecolor="black"
)

plt.suptitle(
    "Distribuição das Variáveis Físico-Químicas",
    fontsize=16
)

plt.tight_layout()
plt.show()


# ==================================================
# 9. CORRELAÇÃO COM A QUALIDADE
# ==================================================

correlacoes = df[variaveis + ["quality"]].corr()

print("\n===== CORRELAÇÃO COM A QUALIDADE =====")

print(
    correlacoes["quality"]
    .drop("quality")
    .sort_values(ascending=False)
    .round(3)
)


plt.figure(figsize=(12, 9))

sns.heatmap(
    correlacoes,
    annot=True,
    cmap="coolwarm",
    center=0,
    fmt=".2f"
)

plt.title("Correlação entre Variáveis e Qualidade")

plt.tight_layout()
plt.show()


print("\n===== ANÁLISE INICIAL CONCLUÍDA =====")
