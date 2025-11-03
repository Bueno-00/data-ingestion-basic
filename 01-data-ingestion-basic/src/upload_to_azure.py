# %%

# src/upload_to_azure.py
from pathlib import Path
import os
from dotenv import load_dotenv
import subprocess
import shutil
import sys

load_dotenv()

account_name = os.getenv("AZURE_STORAGE_ACCOUNT")
account_key = os.getenv("AZURE_STORAGE_KEY")
container_name = os.getenv("AZURE_CONTAINER_NAME", "raw-data")

# determina BASE_DIR de forma robusta
if "__file__" in globals():
    BASE_DIR = Path(__file__).resolve().parents[1]
else:
    BASE_DIR = Path.cwd()

file_path = BASE_DIR / "outputs" / "cleaned_sales.csv"
blob_name = "cleaned_sales.csv"

print("DEBUG: BASE_DIR =", BASE_DIR)
print("DEBUG: file_path =", file_path)
print("DEBUG: file exists?", file_path.exists())

if not file_path.exists():
    print("❌ Arquivo cleaned_sales.csv não encontrado. Pare.")
    sys.exit(1)

# tenta localizar 'az' no PATH do Python
az_path = shutil.which("az")
print("DEBUG: shutil.which('az') ->", az_path)

# monta comando como string (apenas para debug/fallback)
cmd_str = (
    f'az storage blob upload --account-name "{account_name}" '
    f'--account-key "{account_key}" '
    f'--container-name "{container_name}" '
    f'--file "{file_path}" --name "{blob_name}" --overwrite'
)

try:
    if az_path:
        # executa usando o caminho retornado por shutil.which (é C:\...\az.CMD no Windows)
        cmd = [
            az_path,
            "storage", "blob", "upload",
            "--account-name", account_name,
            "--account-key", account_key,
            "--container-name", container_name,
            "--file", str(file_path),
            "--name", blob_name,
            "--overwrite"
        ]
        print("Executando (via lista):", cmd)
        subprocess.run(cmd, check=True)
    else:
        # fallback: executa via shell (menos seguro, mas simples)
        print("az não encontrado via shutil.which(); tentando shell.")
        print("Comando:", cmd_str)
        subprocess.run(cmd_str, shell=True, check=True)

    print("✅ Upload concluído com sucesso!")
except subprocess.CalledProcessError as e:
    print("❌ Erro no subprocess (retorno não-zero):")
    print(e)
except FileNotFoundError as e:
    print("❌ FileNotFoundError:", e)
    print("Tente rodar no terminal: where az")