# Data Preprocessing
# import seaborn as sns
# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import StandardScaler, MinMaxScaler


# df = pd.DataFrame({'name':['Ali', 'Sara', 'Ali'],
#                    'marks':[85, 92, 85]})

# print(df.duplicated())
# print(df.drop_duplicates())


# df = pd.DataFrame({'name':['Ahmad', 'Sara', 'Ahmad'],
#                    'marks':[60, 92, 60]})

# print(df.duplicated())
# print(df.drop_duplicates())

# df = pd.DataFrame({[1, 2, 3, 4, 5, 6, 7, 8, 99]})
# print

# Data Tranforming

# prices = pd.Series([100, 500, 100, 50000])

# log_price = np.log(prices)
# print(log_price)


# prices = pd.Series([10, 1000, 50000, 1000000, 900000000])
# log_price = np.log(prices)
# print(log_price)

# Encoding Categorical Variable

sizes = ['City', 'BMW', 'Tesla', 'BMW']

# le = LabelEncoder()
# print(le.fit_transform(sizes))


# Feature Scaling(Standerd & MinMax

# vals = np.array([[10],[20],[30],[40],[50]])
# print(StandardScaler().fit_transform(vals).flatten())

# print(MinMaxScaler().fit_transform(vals).flatten())

# vals = np.array([[80],[40],[70],[20],[90]])

# print(StandardScaler().fit_transform(vals).flatten())

# print(MinMaxScaler().fit_transform(vals).flatten())


# The Dataset

# df = pd.read_csv('Books_Data_Clean.csv')

# # 1
# print("Rows", df.shape[0])
# print("Column", df.shape[1])

# # 2

# print(df.isnull().sum())

# # 3
# print(df['Book_average_rating'].mean())

# # 4
# total_gross = df['gross sales'].sum()
# print('Total Gross Sales: ', total_gross)

# # 5
# most_common_genre = df['genre'].value_counts().idxmax()
# genre_count = df['genre']. value_counts().max()

# print('Most Frequent Genre: ', most_common_genre)
# print('Number of Books: ', genre_count)


# # 6
# publisher_units = df.groupby("Publisher ")["units sold"].sum()

# top_publisher = publisher_units.idxmax()
# top_units = publisher_units.max()

# print("\nPublisher with Highest Units Sold:", top_publisher)
# print("Total Units Sold:", top_units)

# # 7
# correlation = df["gross sales"].corr(df["publisher revenue"])

# print("\nCorrelation:", correlation)

# if correlation > 0.7:
#     print("Relationship: Strong Positive Correlation")
# elif correlation > 0.3:
#     print("Relationship: Moderate Positive Correlation")
# elif correlation > -0.3:
#     print("Relationship: Weak/No Correlation")
# elif correlation > -0.7:
#     print("Relationship: Moderate Negative Correlation")
# else:
#     print("Relationship: Strong Negative Correlation")

# Next

# Load dataset
# df = pd.read_csv("Books_Data_Clean.csv")

# # Check column names
# print(df.columns)

# # Sort by Publishing Year (replace column name if different)
# sorted_df = df.sort_values(by="Publishing Year", ascending=True)

# # Display first 10 rows after sorting
# print("\nFirst 10 rows after sorting:")
# print(sorted_df.head(10))

# # Find the smallest publishing year
# min_year = sorted_df["Publishing Year"].min()
# print("\nSmallest Publishing Year:", min_year)

# # Investigate all rows with the smallest year
# oldest_books = df[df["Publishing Year"] == min_year]

# print("\nBooks with the smallest publishing year:")
# print(oldest_books)


# Clean


# Sure. Here is the **simple Python code** for the questions visible in your image:

'''
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("books.csv")

# Q2: One-Hot Encoding for Genre
df = pd.get_dummies(df, columns=["Genre"], dtype=int)

# Q3: Ordinal Encoding for Author_Rating
rating_order = {
    "Moderate": 1,
    "Intermediate": 2,
    "Excellent": 3,
    "Famous": 4
}

df["Author_Rating"] = df["Author_Rating"].map(rating_order)

# Q4: Check skewness of Gross_Sales
skewness = df["Gross_Sales"].skew()

print("Gross Sales Skewness:", skewness)

# Apply log transformation if positively skewed
if skewness > 0.5:
    df["Gross_Sales"] = np.log1p(df["Gross_Sales"])
    print("Log transformation applied.")

# Q5: StandardScaler on Units_Sold
scaler = StandardScaler()

df["Units_Sold"] = scaler.fit_transform(
    df[["Units_Sold"]]
)

# Check transformed mean
print("Mean of Units_Sold:", df["Units_Sold"].mean())

# Display final data
print(df.head())
# ```

# If your dataset uses **lowercase column names** such as `genre`, `author_rating`, `gross_sales`, and `units_sold`, use those exact names instead.
'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler

# Load your dataset
df = pd.read_csv("Books_Data_Clean.csv")

# ============================================================
# Q1 — Handle Missing Values
# ============================================================

df["Book Name"] = df["Book Name"].fillna("Unknown")

df["language_code"] = df["language_code"].fillna(
    df["language_code"].mode()[0]
)

df["Publishing Year"] = df["Publishing Year"].fillna(
    df["Publishing Year"].median()
)

print("Missing values after cleaning:")
print(df[["Book Name", "language_code", "Publishing Year"]].isnull().sum())


# ============================================================
# Q3 — Label Encoding for 'Author_Rating'
# ============================================================


rating_order = {
    "Novice": 0,
    "Intermediate": 1,
    "Excellent": 2,
    "Famous": 3
}

df["Author_Rating_Encoded"] = df["Author_Rating"].map(rating_order)

print("\nLabel Encoded Author_Rating:")
print(df[["Author_Rating", "Author_Rating_Encoded"]])

# ============================================================
# Q4 — Check and Reduce Skewness of 'gross sales'
# ============================================================


original_skewness = df["gross sales"].skew()

print("\nOriginal gross sales skewness:", original_skewness)


df["gross_sales_log"] = np.log1p(df["gross sales"])


new_skewness = df["gross_sales_log"].skew()

print("Skewness after log transformation:", new_skewness)

if abs(new_skewness) < abs(original_skewness):
    print("Yes, the skewness improved.")
else:
    print("No, the skewness did not improve.")

# ============================================================
# Q5 — StandardScaler on 'units sold'
# ============================================================

scaler = StandardScaler()

df["units_sold_scaled"] = scaler.fit_transform(
    df[["units sold"]]
)


scaled_mean = df["units_sold_scaled"].mean()

print("\nMean after StandardScaler:", scaled_mean)
print("Mean is approximately 0:", np.isclose(scaled_mean, 0))


print("\nFinal DataFrame:")
print(df)