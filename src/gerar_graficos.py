import sys
sys.path.append("src")

import os
import matplotlib.pyplot as plt
import pandas as pd
from db_connection import obter_engine

engine = obter_engine()
os.makedirs("docs/images", exist_ok=True)

df1 = pd.read_sql("""
    SELECT DATE_TRUNC('month', o.order_purchase_timestamp) AS mes,
           ROUND(SUM(p.payment_value)::numeric, 2) AS faturamento
    FROM orders o
    JOIN order_payments p ON o.order_id = p.order_id
    GROUP BY mes ORDER BY mes;""", engine)

plt.figure(figsize=(12, 6))
plt.plot(df1["mes"], df1['faturamento'], marker='o')
plt.title('Faturamento por mês')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('docs/images/faturamento_mensal.png', dpi=150)
plt.close()

df2 = pd.read_sql("""
    SELECT pr.product_category_name, COUNT(*) AS total_vendido
    FROM order_items oi
    JOIN products pr ON oi.product_id = pr.product_id
    GROUP BY pr.product_category_name
    ORDER BY total_vendido DESC LIMIT 10;""", engine)

plt.figure(figsize=(10, 6))
plt.barh(df2['product_category_name'], df2['total_vendido'])
plt.title('Top 10 categorias mais vendidas')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('docs/images/top_categorias.png', dpi=150)
plt.close()

df3 = pd.read_sql("""
    SELECT c.customer_state,
           ROUND(AVG(EXTRACT(EPOCH FROM (o.order_delivered_customer_date - o.order_purchase_timestamp)) / 86400)::numeric, 1) AS tempo_medio_dias
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    WHERE o.order_delivered_customer_date IS NOT NULL
    GROUP BY c.customer_state ORDER BY tempo_medio_dias DESC;""", engine)

plt.figure(figsize=(10, 8))
plt.barh(df3['customer_state'], df3['tempo_medio_dias'])
plt.title('Tempo médio de entrega por estado (dias)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('docs/images/tempo_entrega_estado.png', dpi=150)
plt.close()

df4 = pd.read_sql("""
    SELECT c.customer_state, ROUND(AVG(r.review_score)::numeric, 2) AS media_avaliacao
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN order_reviews r ON o.order_id = r.order_id
    GROUP BY c.customer_state ORDER BY media_avaliacao DESC;""", engine)

plt.figure(figsize=(10, 8))
plt.barh(df4['customer_state'], df4['media_avaliacao'])
plt.title('Nota média de avaliação por estado')
plt.xlim(0, 5)
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('docs/images/avaliacao_por_estado.png', dpi=150)
plt.close()

print('Gráficos gerados em docs/images/')