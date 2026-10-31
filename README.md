# Tech Challenge — Classificação da Qualidade de Vinhos com Machine Learning

## Sobre o projeto

Este projeto utiliza dados físico-químicos da base WineQT para analisar e classificar a qualidade de vinhos por meio de técnicas de análise de dados e Machine Learning.

O trabalho está organizado em três etapas: análise exploratória, preparação dos dados e modelagem.

## Estrutura do repositório

- `Challeng 2/`: análise exploratória, análise de outliers e base WineQT.
- `Etapa3/`: preparação dos dados, notebook, relatório e artefatos gerados.
- `Etapa 4/`: notebook de Machine Learning, relatório e conjuntos de treino e teste.

## Tecnologias utilizadas

- Python
- pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn
- joblib
- Jupyter Notebook

## Preparação do ambiente

Recomenda-se utilizar um ambiente virtual.

**Criar o ambiente:**

```bash
python -m venv .venv
```

**Ativar no Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Instalar as dependências:**

```bash
python -m pip install pandas numpy matplotlib seaborn scikit-learn joblib jupyter ipykernel
```

## Etapa 2 — Análise exploratória

Pasta: `Challeng 2/Notebooks/`

Principais atividades:
- Análise da estrutura e das características da base.
- Estatísticas descritivas.
- Distribuição das notas de qualidade.
- Análise de correlação entre variáveis.
- Investigação de possíveis outliers pelo método IQR.

Scripts principais:

- `1.Analise.py`
- `2_Analise_Outliers.py`

A base utilizada está em `Challeng 2/vinho-tech-challenge/WineQT.csv`.

Para executar os scripts a partir da raiz:

```bash
python "Challeng 2/Notebooks/1.Analise.py"
python "Challeng 2/Notebooks/2_Analise_Outliers.py"
```

## Etapa 3 — Preparação dos dados

Notebook: `Etapa3/Etapa3_Preparacao.ipynb`

Nesta etapa são realizadas:
- Definição da variável-alvo `quality_class`.
- Verificação de valores ausentes e duplicatas.
- Separação entre variáveis preditoras e variável-alvo.
- Divisão estratificada entre treino e teste.
- Padronização dos dados sem vazamento de informações.
- Exportação dos artefatos para `Etapa3/dados_preparados/`.

Abra o notebook no Jupyter ou VS Code e execute as células em ordem. Ele reconhece a execução a partir da raiz do repositório ou da pasta `Etapa3`.

## Etapa 4 — Machine Learning

Notebook: `Etapa 4/Etapa4_Machine_Learning_WineQT.ipynb`

Nesta etapa são desenvolvidos e avaliados modelos de classificação.

O notebook utiliza seis arquivos CSV presentes na própria pasta `Etapa 4`:

- `X_train.csv`
- `X_test.csv`
- `X_train_scaled.csv`
- `X_test_scaled.csv`
- `y_train.csv`
- `y_test.csv`

A primeira célula localiza automaticamente a pasta que contém esses arquivos.

As avaliações incluem métricas como acurácia, precisão, recall e F1-score.

## Reprodutibilidade

- Os dados utilizados nas etapas estão versionados no repositório.
- Os caminhos foram organizados para reduzir a dependência de diretórios específicos de cada computador.
- A Etapa 3 utiliza uma semente fixa na divisão entre treino e teste.
- A padronização é ajustada nos dados de treino, evitando vazamento de dados.

## Observações

Os valores identificados pelo método IQR são tratados como possíveis outliers. Isso não significa que sejam erros ou que devam ser removidos automaticamente.

Execute as células dos notebooks na ordem apresentada, pois algumas dependem de variáveis e arquivos gerados anteriormente.
