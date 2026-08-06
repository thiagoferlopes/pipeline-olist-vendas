from db_connection import obter_engine

def carregar_dataframe(df,nome_tabela: str):
    engine = obter_engine()
    df.to_sql(nome_tabela, engine, if_exists='append', index=False)
    print(f'{nome_tabela}: {len(df)} linhas carregadas.')