"""
Assignment 5 - House Price Prediction (Pakistan) - Linear Regression + Gradient Descent

Printed output follows the original assignment step by step. Behind the scenes
the model is more accurate: log(price) target, log(area), one-hot categories,
City recovered from Location and messy text (case / spaces) normalised.
"""

import numpy as np
import pandas as pd

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

SQFT_PER_MARLA = 272.25
CATEGORICAL = ["City", "Location", "Condition", "Property_Type"]
YES_NO = ["Furnished", "Corner_Property", "Park_Facing"]
NUMERIC_FILL = ["Bedrooms", "Bathrooms", "Floors", "Year_Built", "Garage"]


def banner(title):
    print("\n================================")
    print(title)
    print("================================")


def to_number(series, pattern=r"(\d+\.?\d*)"):
    cleaned = series.astype(str).str.replace(",", "", regex=False)
    return cleaned.str.extract(pattern)[0].astype(float)


# 1. LOAD DATASET
df = pd.read_csv("pakistan house prediction dataset.csv")

print("Dataset Shape:")
print(df.shape)
print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

# 2. EDA
print("\nStatistical Summary:")
print(df.describe())
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 3. NUMERIC COLUMNS + MARLA (1 Marla = 272.25 Sq Ft)
df["Area_SqFt"] = to_number(df["Area_SqFt"])
df["Price_PKR"] = to_number(df["Price_PKR"])
df["Year_Built"] = to_number(df["Year_Built"], r"(\d{4})")
df["marla"] = df["Area_SqFt"] / SQFT_PER_MARLA

# 4. DUPLICATES, MISSING AREA / PRICE, INVALID & EXTREME VALUES
df = df.drop_duplicates().dropna(subset=["Area_SqFt", "Price_PKR"])
df = df[(df["Area_SqFt"] > 0) & df["Price_PKR"].between(1_000_000, 300_000_000)]

# 5. MISSING VALUES
df[NUMERIC_FILL] = df[NUMERIC_FILL].fillna(df[NUMERIC_FILL].median())
for col in CATEGORICAL + YES_NO:
    df[col] = df[col].fillna("Unknown").astype(str).str.strip()
df["Property_Type"] = df["Property_Type"].str.title()
for col in YES_NO:
    df[col] = df[col].str.lower()

# 6. LABEL ENCODING (kept for the selection menus and the cleaned-data report)
encoders = {col: LabelEncoder().fit(df[col]) for col in CATEGORICAL + YES_NO}
for col, enc in encoders.items():
    df[col + "_encoded"] = enc.transform(df[col])

banner("AFTER PREPROCESSING")
print("Cleaned Dataset Shape:")
print(df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# 7. FEATURES FOR THE MODEL
clean = {col: df[col].str.lower() for col in CATEGORICAL}          # case-insensitive groups
clean["City"] = clean["City"].replace("unknown", np.nan)
city_of = clean["City"].groupby(clean["Location"]).agg(lambda s: s.mode()[0] if s.notna().any() else "unknown")
clean["City"] = clean["City"].fillna(clean["Location"].map(city_of)).fillna("unknown")


def make_features(frame, cats):
    """Numeric + yes/no columns, log(area) and one-hot categories -> model matrix."""
    feats = frame[NUMERIC_FILL].copy()
    feats["marla"] = np.log(frame["marla"])
    for col in YES_NO:
        feats[col] = (frame[col] == "yes").astype(float)
    for col in CATEGORICAL:
        feats[col] = cats[col]
    return feats


all_feats = make_features(df, clean)
keep = df["Area_SqFt"].between(200, 15000)                         # drop extreme areas for training
X = pd.get_dummies(all_feats[keep], columns=CATEGORICAL, drop_first=True, dtype=float)
y = np.log(df.loc[keep, "Price_PKR"]).to_numpy()

# 8. TRAIN TEST SPLIT + SCALING + BIAS
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = np.c_[np.ones(len(X_train)), scaler.fit_transform(X_train)]
X_test = np.c_[np.ones(len(X_test)), scaler.transform(X_test)]

# 9. GRADIENT DESCENT
weights = np.zeros(X_train.shape[1])
learning_rate, iterations = 0.1, 3000
for _ in range(iterations):
    error = X_train @ weights - y_train
    weights -= learning_rate * (X_train.T @ error) / len(y_train)

# 10. TEST PREDICTION + EVALUATION (in real PKR)
y_pred, y_true = np.exp(X_test @ weights), np.exp(y_test)
mse = mean_squared_error(y_true, y_pred)
mae = mean_absolute_error(y_true, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_true, y_pred)

banner("MODEL EVALUATION")
print("MSE  :", mse)
print("MAE  :", mae)
print("RMSE :", rmse)
print("R2   :", r2)


# 11. USER INPUT
def choose(plural, singular, column):
    options = list(encoders[column].classes_)
    print(f"\nAvailable {plural}:")
    for i, value in enumerate(options):
        print(i, "-", value)
    return options[int(input(f"Select {singular} Number: "))]


def yes_no(title):
    print(f"\n{title}:")
    print("0 - no")
    print("1 - yes")
    return "yes" if int(input(f"Select {title}: ")) == 1 else "no"


banner("HOUSE PRICE PREDICTION")
marla = float(input("Enter Area in Marla: "))
bedrooms = float(input("Enter Bedrooms: "))
bathrooms = float(input("Enter Bathrooms: "))
floors = float(input("Enter Floors: "))
year_built = float(input("Enter Year Built: "))
garage = float(input("Enter Garage: "))

city = choose("Cities", "City", "City")
location = choose("Locations", "Location", "Location")
condition = choose("Conditions", "Condition", "Condition")
property_type = choose("Property Types", "Property Type", "Property_Type")
furnished = yes_no("Furnished")
corner_property = yes_no("Corner Property")
park_facing = yes_no("Park Facing")

# 12. BUILD NEW HOUSE, SCALE, PREDICT
location_key = location.lower()
city_key = city.lower()
if city_key == "unknown":
    city_key = city_of.get(location_key, "unknown")

new_house = pd.DataFrame([{
    "Bedrooms": bedrooms, "Bathrooms": bathrooms, "Floors": floors,
    "Year_Built": year_built, "Garage": garage, "marla": marla,
    "Furnished": furnished, "Corner_Property": corner_property, "Park_Facing": park_facing,
}])
new_cats = {"City": city_key, "Location": location_key,
            "Condition": condition.lower(), "Property_Type": property_type.lower()}
new_feats = make_features(new_house, {col: pd.Series([val]) for col, val in new_cats.items()})
new_X = pd.get_dummies(new_feats, columns=CATEGORICAL, dtype=float).reindex(columns=X.columns, fill_value=0.0)

new_scaled = np.c_[np.ones(1), scaler.transform(new_X)]
predicted_price = np.exp(new_scaled @ weights)

banner("PREDICTED HOUSE PRICE")
print("Predicted Price:", round(predicted_price[0], 2), "PKR")
