import requests
import pandas as pd
from sqlalchemy import create_engine


# ==========================================
# 1. EXTRACT
# ==========================================

api_url = "https://dummyjson.com/products"

response = requests.get(api_url)

if response.status_code == 200:

    data = response.json()

    df = pd.DataFrame(data["products"])

    print("Data Extracted Successfully")
    print("Original Shape:", df.shape)
    print(df.head())

else:
    print("API Error:", response.status_code)
    exit()


# 2. TRANSFORM

# Select required columns
df = df[
    [
        "id",
        "title",
        "category",
        "price",
        "discountPercentage",
        "rating",
        "stock",
        "brand",
        "sku"
    ]
]

# Remove duplicate records
df = df.drop_duplicates()

# Rename columns
df = df.rename(
    columns={
        "id": "product_id",
        "title": "product_name",
        "discountPercentage": "discount_percentage"
    }
)

# Clean text columns
text_columns = [
    "product_name",
    "category",
    "brand",
    "sku"
]

for column in text_columns:
    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
        .str.lower()
    )

# Convert numeric columns
numeric_columns = [
    "price",
    "discount_percentage",
    "rating",
    "stock"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

# Handle missing values
for column in numeric_columns:
    df[column] = df[column].fillna(
        df[column].median()
    )

for column in text_columns:
    df[column] = df[column].fillna("unknown")

# Feature Engineering
df["discounted_price"] = (
    df["price"]
    - (
        df["price"]
        * df["discount_percentage"]
        / 100
    )
)

# Round values
df["price"] = df["price"].round(2)
df["discount_percentage"] = df["discount_percentage"].round(2)
df["rating"] = df["rating"].round(2)
df["discounted_price"] = df["discounted_price"].round(2)

# Remove invalid values
df = df[df["price"] >= 0]

df = df[
    df["discount_percentage"].between(0, 100)
]

df = df[df["stock"] >= 0]

print("\nTransformed Data:")
print(df.head())

print("\nFinal Shape:", df.shape)


# 3. LOAD


username = "root"
password = "root"
host = "localhost"
port = 3306
database = "etl_database"

connection_string = (
    f"mysql+pymysql://{username}:{password}"
    f"@{host}:{port}/{database}"
)

engine = create_engine(connection_string)


# Load data into MySQL
df.to_sql(
    "products",
    con=engine,
    if_exists="replace",
    index=False
)


print("\nData Loaded Successfully into MySQL!")
print("Database:", database)
print("Table: products")