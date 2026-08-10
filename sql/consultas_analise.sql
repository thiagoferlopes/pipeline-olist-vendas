-- ================================================
-- Consultas de Análise de Negócio — Pipeline Olist
-- ================================================


-- 1. Faturamento total por mês

SELECT
    DATE_TRUNC('month', o.order_purchase_timestamp) AS mes,
    ROUND(SUM(p.payment_value)::numeric, 2) AS faturamento
FROM orders o
JOIN order_payments p ON o.order_id = p.order_id
GROUP BY mes
ORDER BY mes;


-- 2. Top 10 categorias de produto mais vendidas

SELECT
    pr.product_category_name,
    COUNT(*) AS total_vendido
FROM order_items oi
JOIN products pr ON oi.product_id = pr.product_id
GROUP BY pr.product_category_name
ORDER BY total_vendido DESC
LIMIT 10;


-- 3. Tempo médio de entrega por estado e a quantidade de pedidos

SELECT c.customer_state,
COUNT(*) AS quantidade_pedidos,
ROUND(AVG(EXTRACT(EPOCH FROM
(o.order_delivered_customer_date - o.order_purchase_timestamp)) / 86400)::numeric, 1)
AS tempo_medio_dias
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_delivered_customer_date IS NOT NULL
GROUP BY c.customer_state
ORDER BY tempo_medio_dias DESC;

-- 4. Média de avaliação dos pedidos por estado

SELECT c.customer_state,
COUNT(r.review_score) AS quantidade_avaliacoes,
ROUND(AVG(r.review_score)::numeric, 2) AS media_avaliacao
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_reviews r ON o.order_id = r.order_id
GROUP BY c.customer_state
ORDER BY media_avaliacao DESC;

-- 5. Ticket médio por pedido

SELECT
ROUND(AVG(valor_pedido)::numeric, 2) AS ticket_medio
FROM (
    SELECT o.order_id,
    SUM(p.payment_value) AS valor_pedido
    FROM orders o
    JOIN order_payments p ON o.order_id = p.order_id
    GROUP BY o.order_id
) pedidos;