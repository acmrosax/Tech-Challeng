# Tech Challenge — Classificação da Qualidade de Vinhos com Machine Learning

## Sobre o projeto

Projeto desenvolvido para o Tech Challenge da FIAP com o objetivo de analisar dados físico-químicos de vinhos e construir modelos de Machine Learning para classificar sua qualidade.

A base utilizada é a **WineQT**. A variável-alvo foi definida como:

- **1 — Alta qualidade:** nota `quality >= 7`
- **0 — Baixa/média qualidade:** nota `quality < 7`

O trabalho está organizado em três etapas: análise exploratória, preparação dos dados e modelagem.

## Estrutura do repositório

```text
01_Analise_Exploratoria/
├── Notebooks/
│   ├── 1.Analise.py
│   ├── 2_Analise_Outliers.py
│   ├── analise.ipynb
│   ├── resultados_analises/
│   └── resultados_outliers/
└── vinho-tech-challenge/
    └── WineQT.csv

02_Preparacao_Dos_Dados/
├── Etapa3_Preparacao.ipynb
├── Relatorio_Etapa3_Preparacao_WineQT.pdf
└── dados_preparados/

03_Machine_Learning/
├── Etapa4_Machine_Learning_WineQT.ipynb
├── Relatorio_Machine_Learning_WineQT.docx
└── arquivos CSV de treino e teste

Documentações/
├── Documentacao_Completa_Tech_Challenge_WineQT.pdf
├── POSTECH - DTAT - Tech Challenge - Fase 2.pdf
├── Relatorio_Etapa3_Preparacao_WineQT.pdf
├── Relatorio_Machine_Learning_WineQT.docx
├── WineQT-Tech-Challenge-FIAP_T1_1.pdf
└── Link da apresentação executiva.txt

README.md
requirements.txt
```

## Tecnologias utilizadas

- Python
- pandas e NumPy
- Matplotlib e Seaborn
- scikit-learn
- joblib
- Jupyter Notebook

## Preparação do ambiente

Recomenda-se utilizar um ambiente virtual.

**1. Criar o ambiente virtual:**

```bash
python -m venv .venv
```

**2. Ativar no Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**3. Instalar as dependências na raiz do repositório:**

```bash
python -m pip install -r requirements.txt
```

## Etapa 2 — Análise exploratória

Pasta: `01_Analise_Exploratoria/Notebooks/`

A análise exploratória investiga a estrutura e a qualidade dos dados, incluindo:

- Estatísticas descritivas e distribuição das variáveis;
- Distribuição das notas de qualidade;
- Relações e correlações entre características físico-químicas;
- Identificação e análise de possíveis outliers pelo método IQR.

Arquivos principais:

- `analise.ipynb`
- `1.Analise.py`
- `2_Analise_Outliers.py`

A base original está em:

`01_Analise_Exploratoria/vinho-tech-challenge/WineQT.csv`

Os scripts Python podem ser executados a partir da raiz do repositório:

```bash
python "01_Analise_Exploratoria/Notebooks/1.Analise.py"
python "01_Analise_Exploratoria/Notebooks/2_Analise_Outliers.py"
```

## Etapa 3 — Preparação dos dados

Notebook: `02_Preparacao_Dos_Dados/Etapa3_Preparacao.ipynb`

Nesta etapa são realizadas:

- Definição da variável-alvo `quality_class`;
- Verificação de valores ausentes, duplicatas e inconsistências;
- Separação das variáveis preditoras (`X`) e do alvo (`y`);
- Divisão estratificada em treino e teste;
- Análise de outliers, sem remoção automática dos registros;
- Padronização com `StandardScaler`, ajustado somente nos dados de treino;
- Exportação dos conjuntos e demais artefatos para `02_Preparacao_Dos_Dados/dados_preparados/`.

O notebook localiza automaticamente a raiz do repositório e o arquivo `WineQT.csv`. Abra-o no Jupyter Notebook ou VS Code e execute as células em ordem.

## Etapa 4 — Machine Learning

Notebook: `03_Machine_Learning/Etapa4_Machine_Learning_WineQT.ipynb`

Nesta etapa são treinados e avaliados modelos de classificação, incluindo:

- Regressão Logística, utilizando os dados padronizados;
- Random Forest, utilizando os dados na escala original;
- Avaliação por acurácia, precisão, recall, F1-score, ROC-AUC e matriz de confusão;
- Análise de limiar de decisão e importância das variáveis.

Os arquivos CSV utilizados pela Etapa 4 estão versionados na própria pasta `03_Machine_Learning/`. A primeira célula do notebook localiza automaticamente a pasta que contém os seis arquivos de treino e teste.

## Documentação e apresentação

Os relatórios, a documentação consolidada, o enunciado oficial e a apresentação executiva estão disponíveis na pasta `Documentações/`.

O arquivo `Link da apresentação executiva.txt` contém o endereço do vídeo de apresentação.

## Reprodutibilidade

- A divisão entre treino e teste utiliza uma semente fixa (`random_state=42`).
- A divisão é estratificada para preservar a proporção das classes.
- O `StandardScaler` é ajustado somente com os dados de treino.
- Os notebooks devem ser executados na ordem de suas células, pois há dependência entre etapas e variáveis criadas anteriormente.

## Observação sobre outliers

Os valores sinalizados pelo método IQR são tratados como possíveis outliers. Isso não significa que sejam erros: os registros foram mantidos quando considerados plausíveis, evitando exclusões automáticas que poderiam remover informação relevante.