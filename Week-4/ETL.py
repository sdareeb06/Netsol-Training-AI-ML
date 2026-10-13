import numpy as np
import pandas as pd

# 1. EXTRACT

df = pd.read_csv("pakistan house prediction dataset.csv")

print("Original Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# 2. TRANSFORM

df = df.drop_duplicates()

df = df.drop(columns="ID")



# ----- Area Cleaning -----

df["Area_SqFt"] = (
    df["Area_SqFt"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.extract(r"(\d+\.?\d*)")[0]
    .astype(float)
)



# ----- Price Cleaning -----

df["Price_PKR"] = (
    df["Price_PKR"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.extract(r"(\d+\.?\d*)")[0]
    .astype(float)
)



df["Year_Built"] = (
    df["Year_Built"]
    .astype(str)
    .str.extract(r"(\d{4})")[0]
)

df["Year_Built"] = pd.to_numeric(
    df["Year_Built"],
    errors="coerce"
)




df["City"] = df["City"].astype(str).str.strip().str.lower()

df["Location"] = (
    df["Location"]
    .astype(str)
    .str.strip()
    .str.lower()
)


df["Condition"] = (
    df["Condition"]
    .astype(str)
    .str.strip()
    .str.lower()
)

df["Property_Type"] = (
    df["Property_Type"]
    .astype(str)
    .str.strip()
    .str.lower()
)




df["Furnished"] = (
    df["Furnished"]
    .astype(str)
    .str.strip()
    .str.lower()
)

df["Corner_Property"] = (
    df["Corner_Property"]
    .astype(str)
    .str.strip()
    .str.lower()
)

df["Park_Facing"] = (
    df["Park_Facing"]
    .astype(str)
    .str.strip()
    .str.lower()
)


# ----- Missing Values -----

df["Area_SqFt"] = df["Area_SqFt"].fillna(
    df["Area_SqFt"].median()
)

df["Year_Built"] = df["Year_Built"].fillna(
    df["Year_Built"].median()
)


df["Price_PKR"] = df["Price_PKR"].fillna(
    df["Price_PKR"].median()
)


df["Bedrooms"] = df["Bedrooms"].fillna(
    df["Bedrooms"].median()
)

df["Bathrooms"] = df["Bathrooms"].fillna(
    df["Bathrooms"].median()
)

df["Floors"] = df["Floors"].fillna(
    df["Floors"].median()
)

df["Garage"] = df["Garage"].fillna(
    df["Garage"].median()
)



df["City"] = df["City"].fillna("unknown")

df["Location"] = df["Location"].fillna("unknown")

df["Condition"] = df["Condition"].fillna("unknown")

df["Property_Type"] = df["Property_Type"].fillna("unknown")

df["Furnished"] = df["Furnished"].fillna("unknown")

df["Corner_Property"] = df["Corner_Property"].fillna("unknown")

df["Park_Facing"] = df["Park_Facing"].fillna("unknown")



df["Area_Marla"] = df["Area_SqFt"] / 272.25


# Price per Marla
df["Price_Per_Marla"] = (
    df["Price_PKR"] / df["Area_Marla"]
)
print(df.head(20))

# 3. LOAD

df.to_csv(
    "cleaned_pakistan_house_dataset.csv",
    index=False
)


# FINAL CHECK

print("\nCleaned Shape:")
print(df.shape)

print("\nCleaned Data:")
print(df.head())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nETL completed successfully!")