"""
Objetivo:
- Investigar possíveis outliers nas variáveis físico-químicas da base WineQT.csv;
- Utilizar o método IQR (intervalo interquartil);
- Salvar tabelas e gráficos em uma pasta chamada "resultados_outliers".

Importante:
Um valor identificado pelo IQR é um POSSÍVEL outlier, não necessariamente um erro.
Não removemos nem alteramos dados neste script.
"""

from pathlib import Path

import pandas as pd

import matplotlib
matplotlib.use("Agg")  # Permite salvar gráficos sem abrir uma janela interativa.
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Definir caminhos dos arquivos
# Mantém a lógica original dos caminhos do seu projeto.
PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_BASE = PASTA_PROJETO / "vinho-tech-challenge" / "WineQT.csv"

# Todos os resultados ficam na pasta "resultados_outliers", dentro de Notebooks.
PASTA_RESULTADOS = Path(__file__).resolve().parent / "resultados_outliers"
PASTA_RESULTADOS.mkdir(parents=True, exist_ok=True)


# 2. Ler a base de dados
if not ARQUIVO_BASE.exists():
    raise FileNotFoundError(
        f"Não encontrei o arquivo em: {ARQUIVO_BASE}\n"
        "Confira o caminho em ARQUIVO_BASE e ajuste-o à estrutura das suas pastas."
    )

df = pd.read_csv(ARQUIVO_BASE)

print("=" * 70)
print("ANÁLISE DE POSSÍVEIS OUTLIERS — BASE WINEQT")
print("=" * 70)
print(f"Quantidade de registros: {df.shape[0]}")
print(f"Quantidade de colunas: {df.shape[1]}")


# 3. Selecionar as 11 variáveis físico-químicas.
# Excluímos 'quality' (nota-alvo) e 'Id' (identificador).
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
    "alcohol",
]
variaveis = [coluna for coluna in variaveis if coluna in df.columns]

if not variaveis:
    raise ValueError("Nenhuma das variáveis esperadas foi encontrada na base.")


# 4. Calcular Q1, Q3, IQR, limites e quantidade de possíveis outliers.
resultados = []

for coluna in variaveis:
    q1 = df[coluna].quantile(0.25)
    q3 = df[coluna].quantile(0.75)
    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    mascara_outliers = (
        (df[coluna] < limite_inferior) |
        (df[coluna] > limite_superior)
    )
    quantidade = int(mascara_outliers.sum())
    percentual = quantidade / len(df) * 100 if len(df) else 0

    resultados.append({
        "variavel": coluna,
        "Q1": q1,
        "Q3": q3,
        "IQR": iqr,
        "limite_inferior": limite_inferior,
        "limite_superior": limite_superior,
        "quantidade_possiveis_outliers": quantidade,
        "percentual_possiveis_outliers": percentual,
    })

    print(f"\nVariável: {coluna}")
    print(f"  Q1: {q1:.4f}")
    print(f"  Q3: {q3:.4f}")
    print(f"  IQR: {iqr:.4f}")
    print(f"  Limite inferior: {limite_inferior:.4f}")
    print(f"  Limite superior: {limite_superior:.4f}")
    print(f"  Possíveis outliers: {quantidade} ({percentual:.2f}%)")

tabela_outliers = pd.DataFrame(resultados)
arquivo_tabela = PASTA_RESULTADOS / "resumo_outliers.csv"
tabela_outliers.to_csv(arquivo_tabela, index=False, encoding="utf-8-sig")


# 5. Gráfico de barras horizontais: comparação da quantidade por variável.
# É mais fácil comparar as variáveis do que no boxplot padronizado.
resumo_barras = tabela_outliers.sort_values(
    "quantidade_possiveis_outliers", ascending=True
)

fig, ax = plt.subplots(figsize=(11, 7))
barras = ax.barh(
    resumo_barras["variavel"],
    resumo_barras["quantidade_possiveis_outliers"],
    color="#72B7C9",
)
rotulos = [
    f"{int(qtd)} ({pct:.2f}%)"
    for qtd, pct in zip(
        resumo_barras["quantidade_possiveis_outliers"],
        resumo_barras["percentual_possiveis_outliers"],
    )
]
ax.bar_label(barras, labels=rotulos, padding=4, fontsize=8)
ax.set_title("Comparação de possíveis outliers por variável", weight="bold", pad=12)
ax.set_xlabel("Quantidade de registros sinalizados pelo método IQR")
ax.set_ylabel("Variável físico-química")
ax.set_xlim(0, max(resumo_barras["quantidade_possiveis_outliers"]) * 1.30)
fig.tight_layout()
fig.savefig(
    PASTA_RESULTADOS / "comparacao_outliers_barras.png",
    dpi=180,
    bbox_inches="tight",
)
plt.close(fig)


# 6. Gráfico de barras horizontais: comparação percentual.
resumo_percentual = tabela_outliers.sort_values(
    "percentual_possiveis_outliers", ascending=True
)

fig, ax = plt.subplots(figsize=(11, 7))
barras = ax.barh(
    resumo_percentual["variavel"],
    resumo_percentual["percentual_possiveis_outliers"],
    color="#F2B66D",
)
ax.bar_label(
    barras,
    labels=[f"{pct:.2f}%" for pct in resumo_percentual["percentual_possiveis_outliers"]],
    padding=4,
    fontsize=8,
)
ax.set_title("Percentual de possíveis outliers por variável", weight="bold", pad=12)
ax.set_xlabel("Percentual dos registros")
ax.set_ylabel("Variável físico-química")
ax.set_xlim(0, max(resumo_percentual["percentual_possiveis_outliers"]) * 1.25)
fig.tight_layout()
fig.savefig(
    PASTA_RESULTADOS / "percentual_outliers_barras.png",
    dpi=180,
    bbox_inches="tight",
)
plt.close(fig)


# 7. Salvar boxplots individuais.
# Mantemos esses gráficos para inspecionar a distribuição de cada variável.
for coluna in variaveis:
    fig, ax = plt.subplots(figsize=(9, 4))
    sns.boxplot(
        x=df[coluna],
        ax=ax,
        color="#8ECAE6",
        flierprops={
            "marker": "o",
            "markerfacecolor": "#E76F51",
            "markeredgecolor": "#9D0208",
            "markersize": 4,
            "alpha": 0.75,
        },
    )
    ax.set_title(f"Distribuição e possíveis outliers — {coluna}", weight="bold")
    ax.set_xlabel(coluna)
    ax.set_ylabel("")
    fig.tight_layout()

    nome_seguro = coluna.replace(" ", "_").replace("/", "_")
    caminho_grafico = PASTA_RESULTADOS / f"boxplot_{nome_seguro}.png"
    fig.savefig(caminho_grafico, dpi=180, bbox_inches="tight")
    plt.close(fig)


# 8. Relatório final no terminal.
print("\\n" + "=" * 70)
print("RESUMO DA ANÁLISE DE OUTLIERS")
print("=" * 70)
print(
    tabela_outliers[
        ["variavel", "quantidade_possiveis_outliers", "percentual_possiveis_outliers"]
    ].sort_values("quantidade_possiveis_outliers", ascending=False).to_string(
        index=False,
        formatters={"percentual_possiveis_outliers": lambda valor: f"{valor:.2f}%"},
    )
)

print("\\nNenhum dado foi removido ou alterado.")
print(f"Tabela CSV salva em: {arquivo_tabela}")
print(f"Gráficos salvos na pasta: {PASTA_RESULTADOS}")
print("Novos gráficos comparativos:")
print("- comparacao_outliers_barras.png")
print("- percentual_outliers_barras.png")
print("Também foram salvos boxplots individuais para cada variável.")
