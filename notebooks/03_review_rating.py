#step 3

import pandas as pd
from pathlib import Path

# Load the dataset
file_path = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "raw"
    / "customer_shopping_behavior.csv"
)

df = pd.read_csv(file_path)

print("--- REVIEW RATING ANALYSIS ---")

# Summary statistics
print(df["Review Rating"].describe())

# Average rating
print("\nAverage Review Rating:", df["Review Rating"].mean())

# Median rating
print("Median Review Rating:", df["Review Rating"].median())

# Most frequent rating
print(
    "Most Frequent Review Rating:",
    df["Review Rating"].mode().tolist()
)