import sys
sys.path.append("src")

from extract import extrair_csv
from transform import (
    limpar_pedidos,
    limpar_customers,
    limpar_sellers,
    limpar_products,
    limpar_order_items,
    limpar_order_payments,
    limpar_order_reviews,
)
from load import carregar_dataframe

print("== Carregando customers ==")
df = extrair_csv("olist_customers_dataset.csv")
df = limpar_customers(df)
carregar_dataframe(df, "customers")

print("== Carregando sellers ==")
df = extrair_csv("olist_sellers_dataset.csv")
df = limpar_sellers(df)
carregar_dataframe(df, "sellers")

print("== Carregando products ==")
df = extrair_csv("olist_products_dataset.csv")
df = limpar_products(df)
carregar_dataframe(df, "products")

print("== Carregando orders ==")
df = extrair_csv("olist_orders_dataset.csv")
df = limpar_pedidos(df)
carregar_dataframe(df, "orders")

print("== Carregando order_items ==")
df = extrair_csv("olist_order_items_dataset.csv")
df = limpar_order_items(df)
carregar_dataframe(df, "order_items")

print("== Carregando order_payments ==")
df = extrair_csv("olist_order_payments_dataset.csv")
df = limpar_order_payments(df)
carregar_dataframe(df, "order_payments")

print("== Carregando order_reviews ==")
df = extrair_csv("olist_order_reviews_dataset.csv")
df = limpar_order_reviews(df)
carregar_dataframe(df, "order_reviews")

print("Pipeline concluído com sucesso!")