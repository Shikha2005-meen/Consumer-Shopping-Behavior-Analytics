#step 4

import pandas as pd
from pathlib import Path

# ==========================================
# 1. DEFINE FILE PATHS
# ==========================================

project_folder = Path(__file__).resolve().parent.parent

raw_file = (
    project_folder
    / "data"
    / "raw"
    / "customer_shopping_behavior.csv"
)

processed_folder = project_folder / "data" / "processed"
processed_folder.mkdir(parents=True, exist_ok=True)

cleaned_file = (
    processed_folder
    / "customer_shopping_behavior_cleaned.csv"
)


# ==========================================
# 2. LOAD ORIGINAL DATASET
# ==========================================

df = pd.read_csv(raw_file)

print("=" * 50)
print("CONSUMER SHOPPING BEHAVIOR ANALYTICS")
print("DATA CLEANING REPORT")
print("=" * 50)

print("\n--- ORIGINAL DATASET ---")

print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])
print("Total Missing Values:", df.isnull().sum().sum())
print("Total Duplicate Rows:", df.duplicated().sum())


# ==========================================
# 3. INSPECT DATA TYPES
# ==========================================

print("\n--- DATA TYPES BEFORE CLEANING ---")

print(df.dtypes)


# ==========================================
# 4. HANDLE MISSING REVIEW RATINGS
# ==========================================

print("\n--- MISSING VALUE TREATMENT ---")

missing_before = df["Review Rating"].isnull().sum()

print("Missing Ratings Before Cleaning:", missing_before)

rating_median = df["Review Rating"].median()

print("Median Review Rating:", rating_median)

df["Review Rating"] = (
    df["Review Rating"].fillna(rating_median)
)

missing_after = df["Review Rating"].isnull().sum()

print("Missing Ratings After Cleaning:", missing_after)


# ==========================================
# 5. CHECK DUPLICATE RECORDS
# ==========================================

print("\n--- DUPLICATE CHECK ---")

duplicate_count = df.duplicated().sum()

print("Duplicate Rows Found:", duplicate_count)

# Remove exact duplicate rows if any exist.
# Original raw CSV remains unchanged.
if duplicate_count > 0:
    df = df.drop_duplicates()

print("Rows After Duplicate Check:", df.shape[0])


# ==========================================
# 6. CHECK DATA QUALITY
# ==========================================

print("\n--- DATA QUALITY CHECKS ---")

print("\nMissing Values Per Column:")
print(df.isnull().sum())

print("\nData Types After Cleaning:")
print(df.dtypes)

print("\nPurchase Amount Summary:")
print(df["Purchase Amount (USD)"].describe())

print("\nReview Rating Summary:")
print(df["Review Rating"].describe())


# ==========================================
# 7. SAVE CLEANED DATASET
# ==========================================

df.to_csv(cleaned_file, index=False)

print("\n--- CLEANING COMPLETED ---")

print("Final Rows:", df.shape[0])
print("Final Columns:", df.shape[1])
print("Final Missing Values:", df.isnull().sum().sum())

print("\nCleaned dataset saved successfully at:")
print(cleaned_file)