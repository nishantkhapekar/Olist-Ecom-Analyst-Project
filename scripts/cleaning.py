import pandas as pd
master = pd.read_parquet("cleaned_data/master_sales.parquet")

# Remove Duplicates
master.drop_duplicates(inplace=True)


# : Convert Dates


date_cols = [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]
for col in date_cols:
    master[[col]] = pd.to_datetime(master[col], errors="coerce")


# Revenue Column
master["revenue"] = master["price"] * master["order_item_id"]


KPI --> key performance indicator


# Extract Year
master["order_year"] = master["order_purchase_timestamp"].dt.year

# Extract Month
master["month"] = (
    master["order_purchase_timestamp"]
    .dt.month
)


## Review columns mein negative reviews 
master = master[master["review_score"] >= 2]


master.to_parquet(
    "cleaned_data/final_product_analytics.parquet",
    index=False
)