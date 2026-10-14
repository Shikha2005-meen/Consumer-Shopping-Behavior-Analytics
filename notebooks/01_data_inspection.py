#step 1

import pandas as pd

# Load the raw dataset
#file_path = "C:\\Users\\shikha\\OneDrive\\Desktop\\consumer-shopping-behavior-analytics\\data\\raw\\customer_shopping_behavior.csv"

from pathlib import Path

file_path = Path(__file__).resolve().parent.parent / "data" / "raw" / "customer_shopping_behavior.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")

print(df.head())


#step 2

print("\n--- DATASET OVERVIEW ---")

# Total rows and columns
print("Dataset Shape:", df.shape)

# All column names
print("\nColumn Names:")
print(df.columns.tolist())

# Dataset information
print("\nDataset Information:")
df.info()

#step 3

print("\n--- MISSING VALUES ANALYSIS ---")

# Count missing values in each column
print(df.isnull().sum())

# Total missing values in the complete dataset
print("\nTotal Missing Values:", df.isnull().sum().sum())


print("\n--- DUPLICATE RECORDS ANALYSIS ---")

# Count completely duplicated rows
print("Total Duplicate Rows:", df.duplicated().sum())


print("\n--- MISSING VALUE PERCENTAGE ---")

# Calculate percentage of missing values per column
missing_percentage = (df.isnull().sum() / len(df)) * 100

print(missing_percentage.sort_values(ascending=False))