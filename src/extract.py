import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path('data/raw')

def extrair_csv(nome_arquivo: str) -> pd.DataFrame:
    caminho = RAW_DATA_PATH / nome_arquivo
    df = pd.read_csv(caminho)
    print(f'{nome_arquivo}: {df.shape[0]} linhas, {df.shape[1]} colunas')
    return df