# 🧠 Projeto 01 – Ingestão de Dados Básico (ETL com Azure e Power BI)

---

## 📘 Visão Geral

Este projeto demonstra um processo completo de **aquisição, transformação e carregamento de dados (ETL/ELT)**, utilizando **Python**, **SQLite**, **Azure Blob Storage** e **Power BI** para visualização.

O objetivo é construir um **pipeline simples, porém funcional**, que realize todas as etapas principais da **Engenharia de Dados**:

1. Leitura de dados brutos  
2. Limpeza e transformação  
3. Armazenamento em banco de dados  
4. Upload para a nuvem (Azure Blob Storage)  
5. Visualização dos resultados (Power BI)

Os dados utilizados são pequenos (apenas **6 vendas de 3 produtos**) e servem para demonstrar o fluxo completo de **ETL**.

---

## 🗂 Estrutura do Projeto

```bash
DATA-ENGINEERING-PORTFOLIO/
│
├── .venv/                     # Ambiente virtual Python
│
├── .vscode/                   # Configurações do VSCode
│
├── 01-data-ingestion-basic/   # Diretório principal do projeto
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
│   ├── requirements.txt       # Bibliotecas utilizadas
│   └── README.md              # Documentação do projeto
```
---

⚙️ Tecnologias e Ferramentas

Python 3.13+

Pandas → leitura e tratamento dos dados
SQLite3 → banco de dados local
Azure CLI → upload para o Azure Blob Storage
Power BI → visualização e dashboards
VSCode → ambiente de desenvolvimento
Ambiente Virtual (.venv) → isolamento de dependências

---

🧩 Etapas do Processo ETL

1️⃣ Ingestão e Transformação (ingest_transform.py)

Lê o arquivo datasets/sample_sales.csv
Converte colunas de datas
Calcula novas colunas (revenue = price * quantity)
Remove valores nulos e padroniza nomes de produtos
Exporta os dados tratados para outputs/cleaned_sales.csv

2️⃣ Armazenamento no Banco (to_sqlite.py)

Conecta ao SQLite3
Cria o banco sales.db em outputs/
Cria e insere dados na tabela sales
Executa uma query para sumarizar vendas por produto


3️⃣ Upload para Azure (upload_to_azure.py)

Lê variáveis do arquivo .env:
AZURE_STORAGE_ACCOUNT
AZURE_STORAGE_KEY
AZURE_CONTAINER_NAME

Utiliza o Azure CLI (az storage blob upload)
Envia os arquivos cleaned_sales.csv e sales.db para o Blob Storage


4️⃣ Visualização no Power BI

Após o upload, os dados são consumidos diretamente do Azure e visualizados no Power BI, gerando insights como:
Vendas por produto
Vendas por estado

📊 Gráficos criados no Power BI:

![Gráfico 1](01-data-ingestion-basic/GraficoColunas-Projeto01.png)
![Gráfico 2](01-data-ingestion-basic/GraficoLinhas-Projeto01.png)

---

🧰 Requisitos e Instalação
Instalar dependências

pip install -r requirements.txt

Executar o pipeline completo

Ativar ambiente virtual
source .venv/Scripts/activate

1. Ingestão e transformação
python src/ingest_transform.py

2. Criação e inserção no banco
python src/to_sqlite.py

3. Upload para Azure
python src/upload_to_azure.py

---

🔐 Configuração do .env

Antes de executar o upload, crie o arquivo .env na raiz do projeto com suas credenciais do Azure:

AZURE_STORAGE_ACCOUNT=nomedaconta
AZURE_STORAGE_KEY=sua_chave_aqui
AZURE_CONTAINER_NAME=raw-data

---

📚 Objetivo Educacional

Este projeto foi desenvolvido com fins educacionais e demonstrativos, consolidando os principais conceitos de:

- ETL/ELT com Python

- Transformação e limpeza de dados

- Criação e manipulação de bancos locais (SQLite)

- Integração com serviços de nuvem (Azure)

- Visualização de dados com Power BI

---

👨‍💻 Autor

Rafael Bueno
Projeto desenvolvido para estudo prático em Engenharia de Dados.
