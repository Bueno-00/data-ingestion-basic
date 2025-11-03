🧠 Projeto 01 – Data Ingestion Básico (ETL com Azure e Power BI)

📘 Visão Geral

Este projeto demonstra um processo completo de ingestão, transformação e carga de dados (ETL/ELT), utilizando Python, SQLite, Azure Blob Storage e Power BI para visualização.
O objetivo é construir uma pipeline simples, mas funcional, que realiza todas as etapas principais de Engenharia de Dados:

Leitura de dados brutos

Limpeza e transformação

Armazenamento em banco de dados

Upload na nuvem (Azure)

Visualização dos resultados (Power BI)

Os dados são pequenos (apenas 6 vendas de 3 produtos) e servem para demonstrar o fluxo completo de ETL.

🗂 Estrutura do Projeto
DATA-ENGINEERING-PORTFOLIO/
│
├── .venv/                     # Ambiente virtual Python
│
├── .vscode/                   # Configurações do VSCode
│
├── 01-data-ingestion-basic/
│   ├── datasets/              # Dados brutos
│   │   └── sample_sales.csv
│   │
│   ├── outputs/               # Resultados processados
│   │   ├── cleaned_sales.csv  # Dados tratados
│   │   └── sales.db           # Banco SQLite
│   │
│   ├── src/                   # Códigos principais
│   │   ├── ingest_transform.py  # Ingestão e transformação
│   │   ├── to_sqlite.py         # Armazenamento em banco
│   │   └── upload_to_azure.py   # Upload para Azure
│   │
│   ├── images/                # Gráficos do Power BI
│   │   ├── x.png
│   │   ├── xx.png
│   │   ├── xxx.png
│   │   └── xxxx.png
│   │
│   ├── .env                   # Chaves Azure (privado)
│   ├── .gitignore             # Arquivos ignorados pelo Git
│   ├── requirements.txt       # Bibliotecas
│   └── README.md              # Documentação

⚙️ Tecnologias e Ferramentas

Python 3.13+

Pandas → leitura e tratamento dos dados

SQLite3 → banco de dados local

Azure CLI → upload para o Azure Blob Storage

Power BI → visualização e dashboards

VSCode → ambiente de desenvolvimento

Ambiente Virtual (.venv) → isolamento de dependências

🧩 Etapas do Processo ETL
1️⃣ Ingestão e Transformação (ingest_transform.py)

Lê o arquivo datasets/sample_sales.csv

Converte datas e tipos de dados

Calcula novas colunas (revenue = price * quantity)

Limpa valores nulos e padroniza nomes de produtos

Exporta os dados tratados em outputs/cleaned_sales.csv

📸 Visualização no VSCode:


2️⃣ Armazenamento no Banco (to_sqlite.py)

Conecta ao SQLite3

Cria o banco sales.db em outputs/

Cria e insere dados na tabela sales

Executa query para sumarizar vendas por produto

📸 Banco de Dados e Query:


3️⃣ Upload para Azure (upload_to_azure.py)

Lê variáveis do .env:

AZURE_STORAGE_ACCOUNT

AZURE_STORAGE_KEY

AZURE_CONTAINER_NAME

Usa o Azure CLI via comando az storage blob upload

Envia arquivos tratados (cleaned_sales.csv, sales.db) para o Blob Storage

📸 Execução do Upload via CLI:


4️⃣ Visualização no Power BI

Após o upload, os dados são consumidos diretamente do Azure e visualizados no Power BI, gerando insights como:

Vendas por produto

Vendas por estado

📊 Gráficos criados no Power BI:


🧰 Requisitos e Instalação

Instalar dependências:

pip install -r requirements.txt


Executar o pipeline completo:

# Ativar ambiente virtual
source .venv/Scripts/activate

# 1. Ingestão e transformação
python src/ingest_transform.py

# 2. Criação do banco
python src/to_sqlite.py

# 3. Upload para Azure
python src/upload_to_azure.py

🔐 Configuração do .env

Antes de rodar o upload, crie o arquivo .env na raiz do projeto com suas credenciais Azure:

AZURE_STORAGE_ACCOUNT=nomedaconta
AZURE_STORAGE_KEY=sua_chave_aqui
AZURE_CONTAINER_NAME=raw-data


⚠️ Importante: o arquivo .env está incluído no .gitignore, por isso não será enviado ao GitHub (segurança garantida).

📊 Power BI – Relatórios

Após carregar os dados no Power BI, foram criadas duas visualizações:

Gráfico 1 – Vendas por Produto

Gráfico 2 – Vendas por Estado

Esses gráficos demonstram o sucesso do pipeline completo, desde a ingestão até a visualização analítica.

📚 Objetivo Educacional

Este projeto foi desenvolvido com fins educacionais e demonstrativos, consolidando conceitos de:

ETL/ELT com Python

Transformação de dados

Criação de banco local

Integração com nuvem (Azure)

Visualização com Power BI

👨‍💻 Autor

Rafael Bueno
Projeto desenvolvido para estudo prático em Engenharia de Dados.