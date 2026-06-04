import pandas as pd

files = [
    "olist_orders_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_products_dataset.csv",
    "olist_customers_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv"
]

for file in files:

    print("\n" + "=" * 50)
    print(file)

    df = pd.read_csv(
        f"dataset/{file}"
    )

    print(df.shape)

    print(df.columns.tolist())

    print(df.head())