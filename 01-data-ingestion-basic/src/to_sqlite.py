#%%
import pandas as pd
import sqlite3
from pathlib import Path

# O Path(__file__).resolve().parents[1] nesse caso seria o mesmo que 
# Path(".../Desktop/data-engineering-portfolio/01-data-ingestion-basic")
BASE_DIR = Path(__file__).resolve().parents[1] 
DATA_OUT = BASE_DIR / "outputs" / "cleaned_sales.csv"
DB_PATH = BASE_DIR / "outputs" / "sales.db"

df = pd.read_csv(DATA_OUT, parse_dates=["date"])

conn = sqlite3.connect(DB_PATH)

df.to_sql("sales", conn, if_exists="replace", index=False)

""" df.to_sql(
name = "sales" (Da o nome da tabela no banco), 
con = conn (É a conexão com o conn -> conn = sqlite3.connect(DB_PATH) ),
if_exists = "replace" (o que fazer se a tabela já existir ('fail', 'replace', 'append')), 
index = False (se deve enviar o índice do DataFrame como coluna extra (geralmente False)))"""

query = """
SELECT
    product,
    SUM(revenue) AS total_revenue,
    SUM(quantity) AS total_quantity
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;
"""

# Caso a "query" nao tivesse sido contruida antes
# teriamos que colocar ele e depois a conexao
# ficaria assim: pd.read_sql_query("SELECT ... FROM sales", conn)

result = pd.read_sql_query(query, conn)
print(f"Esse é o resultado da consulta: \n\n{result}")

conn.close()
print("\n A conexão foi encerrada!")