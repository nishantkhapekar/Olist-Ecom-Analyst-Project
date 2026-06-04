import pandas as pd

datasets = {
    "orders":
        "dataset/olist_orders_dataset.csv",

    "customers":
        "dataset/olist_customers_dataset.csv",

    "order_items":
        "dataset/olist_order_items_dataset.csv",

    "products":
        "dataset/olist_products_dataset.csv",

    "payments":
        "dataset/olist_order_payments_dataset.csv"
}

for name, file in datasets.items():

    df = pd.read_csv(file)

    print("\n" + "=" * 60)
    print(name.upper())

    print("\nShape:")
    print(df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicates:")
    print(df.duplicated().sum())

    print("\nData Types:")
    print(df.dtypes)