"""
Assignment 4 - Pandas: Series, DataFrames, cleaning, correlation, plotting.

Each topic is a function. By default only the original active steps run:
print the DataFrame and draw the histogram (see STEPS_TO_RUN).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
# data.csv lives in Week-3 (and later weeks); use a local copy first if present
CSV_FILE = next((p for p in (HERE / "data.csv", HERE.parent / "Week-3" / "data.csv") if p.exists()),
                HERE / "data.csv")


def load():
    return pd.read_csv(CSV_FILE)


# --------------------------- Series & DataFrames ---------------------------

def series_demo():
    print(pd.Series([1, 7, 2]))
    print(pd.Series([1, 7, 2], index=["x", "y", "z"]))
    calories = {"day1": 420, "day2": 380, "day3": 390}
    print(pd.Series(calories))
    print(pd.Series(calories, index=["day1", "day2"]))


def dataframe_demo():
    data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
    df = pd.DataFrame(data)
    print(df)
    print(df.loc[0])
    print(df.loc[[0, 1]])
    named = pd.DataFrame(data, index=["day1", "day2", "day3"])
    print(named)
    print(named.loc["day2"])


def show_data():
    print(load())


# ------------------------------- Cleaning --------------------------------

def cleaning_demo():
    df = load()
    print(df.dropna().to_string())
    df["Calories"] = df["Calories"].fillna(df["Calories"].mean())     # or .median() / .mode()[0]
    print(df.to_string())


# --------------------- Correlation & plotting ---------------------------

def correlation_demo():
    print(load().corr())


def scatter_demo():
    load().plot(kind="scatter", x="Duration", y="Calories")
    plt.show()


def histogram():
    load().plot(kind="hist", x="Duration", y="Maxpulse")
    plt.show()


STEPS_TO_RUN = [show_data, histogram]

if __name__ == "__main__":
    for step in STEPS_TO_RUN:
        step()
