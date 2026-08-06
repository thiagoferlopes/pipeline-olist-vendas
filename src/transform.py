import pandas as pd

def limpar_pedidos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    colunas_data = [
        'order_purchase_timestamp',
        'order_delivered_customer_date',
        'order_estimated_delivery_date',
    ]

    for col in colunas_data:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    df = df.drop_duplicates(subset='order_id')
    df['order_status'] = df['order_status'].str.lower().str.strip()
    return df
