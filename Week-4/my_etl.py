import argparse
import logging
import sqlite3
from datetime import date
from pathlib import Path

import pandas as pd

CURRENT_YEAR = date.today().year

VALID_RANGES = {
    "Area_SqFt": (100, 30_000),
    "Year_Built": (1900, CURRENT_YEAR),
    "Price_PKR": (500_000, 1_000_000_000),
}

NUMERIC_TEXT_COLS = list(VALID_RANGES)
COUNT_COLS = ["Bedrooms", "Bathrooms", "Floors", "Garage"]
YES_NO_COLS = ["Furnished", "Corner_Property", "Park_Facing"]
TEXT_COLS = ["City", "Location", "Condition", "Property_Type"]

ACRONYMS = {"Dha": "DHA", "Pechs": "PECHS", "Pwd": "PWD"}

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("etl")

def extract(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, dtype=str)
    log.info(f"[Extract] {len(df):,} rows, {df.shape[1]} columns read from {path.name}")
    return df

def parse_number(series: pd.Series) -> pd.Series:
    text = series.astype("string").str.replace(",", "", regex=False)
    return pd.to_numeric(text.str.extract(r"(-?\d+(?:\.\d+)?)")[0], errors="coerce")

def clean_text(series: pd.Series) -> pd.Series:
    text = series.astype("string").str.strip().str.replace(r"\s+", " ", regex=True)
    text = text.str.lower().str.split().str.join(" ")
    text = text.map(lambda s: s if pd.isna(s) else s.title().replace("'S", "'s"), na_action="ignore")
    for wrong, right in ACRONYMS.items():
        text = text.str.replace(rf"\b{wrong}\b", right, regex=True)
    return text

def to_flag(series: pd.Series) -> pd.Series:
    return series.astype("string").str.strip().str.lower().map({"yes": 1, "no": 0}).astype("Int8")

def fill_with_median(df: pd.DataFrame, col: str, group_by: list[str] | None = None) -> None:
    overall = df[col].median()
    if group_by:
        df[col] = df[col].fillna(df.groupby(group_by)[col].transform("median"))
    df[col] = df[col].fillna(overall)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    rows_in = len(df)

    for col in NUMERIC_TEXT_COLS + COUNT_COLS:
        df[col] = parse_number(df[col])

    for col, (low, high) in VALID_RANGES.items():
        invalid = df[col].notna() & ~df[col].between(low, high)
        if invalid.any():
            log.info(f"[Transform] {invalid.sum():>4} invalid {col} values set to missing")
        df.loc[invalid, col] = pd.NA

    for col in TEXT_COLS:
        df[col] = clean_text(df[col])
    for col in YES_NO_COLS:
        df[col] = to_flag(df[col])

    before = len(df)
    df = df.drop_duplicates().drop_duplicates(subset="ID", keep="first")
    log.info(f"[Transform] {before - len(df):>4} duplicate rows removed")

    before = len(df)
    df = df.dropna(subset=["Price_PKR"])
    log.info(f"[Transform] {before - len(df):>4} rows dropped (no valid price)")

    city_of_location = df.dropna(subset=["City"]).groupby("Location")["City"].agg(lambda s: s.mode()[0])
    missing_city = df["City"].isna()
    df.loc[missing_city, "City"] = df.loc[missing_city, "Location"].map(city_of_location)
    log.info(f"[Transform] {missing_city.sum() - df['City'].isna().sum():>4} missing cities recovered from Location")

    df["Price_Per_SqFt"] = (df["Price_PKR"] / df["Area_SqFt"]).round(2)
    df["Property_Age"] = CURRENT_YEAR - df["Year_Built"]

    fill_with_median(df, "Area_SqFt", group_by=["City", "Property_Type"])
    for col in ["Year_Built", *COUNT_COLS]:
        fill_with_median(df, col)

    df = df.dropna(subset=["City"])
    int_cols = ["ID", "Area_SqFt", "Year_Built", "Price_PKR", *COUNT_COLS]
    df[int_cols] = df[int_cols].round().astype("int64")
    df["Property_Age"] = df["Property_Age"].astype("Int64")
    df = df.sort_values("ID").reset_index(drop=True)

    log.info(f"[Transform] {rows_in:,} rows in -> {len(df):,} rows out")
    return df

def validate(df: pd.DataFrame) -> None:
    assert df["ID"].is_unique, "Duplicate IDs found"
    assert df["Price_PKR"].between(*VALID_RANGES["Price_PKR"]).all(), "Price out of range"
    assert df["Area_SqFt"].between(*VALID_RANGES["Area_SqFt"]).all(), "Area out of range"
    assert df[["City", "Location", "Condition", "Property_Type"]].notna().all().all(), "Missing text values"
    log.info("[Validate] all checks passed")

def load(df: pd.DataFrame, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = output_dir / "houses_clean.csv"
    df.to_csv(csv_path, index=False)

    db_path = output_dir / "houses.db"
    with sqlite3.connect(db_path) as conn:
        df.to_sql("houses", conn, if_exists="replace", index=False)

    log.info(f"[Load] {csv_path}")
    log.info(f"[Load] {db_path} (table: houses)")

def main() -> None:
    parser = argparse.ArgumentParser(description="ETL for the Pakistan house price dataset")
    here = Path(__file__).resolve().parent
    parser.add_argument("--input", type=Path,
                        default=here / "pakistan house prediction dataset.csv")
    parser.add_argument("--output-dir", type=Path, default=here / "output")
    args = parser.parse_args()

    raw = extract(args.input)
    clean = transform(raw)
    validate(clean)
    load(clean, args.output_dir)

    print("\nSample of the cleaned data:")
    print(clean.head().to_string(index=False))

if __name__ == "__main__":
    main()