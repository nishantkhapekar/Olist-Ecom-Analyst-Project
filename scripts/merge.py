import pandas as pd
import os

os.makedirs(
    "cleaned_data",
    exist_ok=True
)


print("Loading datasets...")

orders = pd.read_csv(
    "dataset/olist_orders_dataset.csv"
)

customers = pd.read_csv(
    "dataset/olist_customers_dataset.csv"
)

order_items = pd.read_csv(
    "dataset/olist_order_items_dataset.csv"
)

products = pd.read_csv(
    "dataset/olist_products_dataset.csv"
)

payments = pd.read_csv(
    "dataset/olist_order_payments_dataset.csv"
)


#### ORDERS + CUSTOMERS
master = orders.merge(
    customers,
    on="customer_id",
    how="left"
)

print(
    "After customers join:",
    master.shape
)

# Add Order Items
# ==================================

master = master.merge(
    order_items,
    on="order_id",
    how="left"
)

print(
    "After order_items join:",
    master.shape
)


# Add Products
# ==================================

master = master.merge(
    products,
    on="product_id",
    how="left"
)

print(
    "After products join:",
    master.shape
)


# ==================================
# Add Payments
# ==================================

master = master.merge(
    payments,
    on="order_id",
    how="left"
)

print(
    "After payments join:",
    master.shape
)


master.to_parquet(
    "cleaned_data/master_sales.parquet",
    index=False
)

print("Master dataset created!")
print(master.shape)


# master_table  = pd.read_csv()
# revenue 
# orders
# customers
# Repeat Reat
# Product Revenue
