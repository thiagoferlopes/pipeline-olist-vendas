import sys
sys.path.append('src')

from extract import extrair_csv
from transform import limpar_pedidos
from load import carregar_dataframe

df_pedidos = extrair_csv('olist_orders_dataset.csv')
df_pedidos_limpo = limpar_pedidos(df_pedidos)
carregar_dataframe(df_pedidos_limpo, 'orders')