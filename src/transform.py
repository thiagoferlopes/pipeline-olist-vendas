import pandas as pd


def limpar_pedidos(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    colunas_data = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
    ]
    for col in colunas_data:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    df = df.drop_duplicates(subset="order_id")
    df["order_status"] = df["order_status"].str.lower().str.strip()

    return df


def limpar_customers(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates(subset="customer_id")
    df["customer_city"] = df["customer_city"].str.lower().str.strip()
    df["customer_state"] = df["customer_state"].str.upper().str.strip()
    return df


def limpar_sellers(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates(subset="seller_id")
    df["seller_city"] = df["seller_city"].str.lower().str.strip()
    df["seller_state"] = df["seller_state"].str.upper().str.strip()
    return df


def limpar_products(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates(subset="product_id")
    df["product_category_name"] = df["product_category_name"].str.lower().str.strip()

    colunas_numericas = [
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ]
    for col in colunas_numericas:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def limpar_order_items(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates(subset=["order_id", "order_item_id"])
    df["shipping_limit_date"] = pd.to_datetime(df["shipping_limit_date"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["freight_value"] = pd.to_numeric(df["freight_value"], errors="coerce")
    return df


def limpar_order_payments(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates(subset=["order_id", "payment_sequential"])
    df["payment_type"] = df["payment_type"].str.lower().str.strip()
    df["payment_value"] = pd.to_numeric(df["payment_value"], errors="coerce")
    return df


def limpar_order_reviews(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates(subset="review_id")

    colunas_data = ["review_creation_date", "review_answer_timestamp"]
    for col in colunas_data:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    df["review_score"] = pd.to_numeric(df["review_score"], errors="coerce")
    return df