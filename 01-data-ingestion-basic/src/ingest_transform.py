# %%

import pandas as pd
import sqlite3

def load_data():
    df = pd.read_csv("../datasets/sample_sales.csv")
    df["date"] = pd.to_datetime(df["date"])

    return df
df = load_data()

def clean_transform(df):
    df = df.dropna(subset = "order_id")
    df["revenue"] = df["price"] * df["quantity"] 
    df["product"] = df["product"].str.strip().str.title()
    return df
df = clean_transform(df)

def save_output(df):
    output_path = "../outputs/cleaned_sales.csv"
    df.to_csv(output_path, index=False)
    print(f"Arquivo salva com sucesso em: {output_path}")
    return df
df = save_output(df)
df