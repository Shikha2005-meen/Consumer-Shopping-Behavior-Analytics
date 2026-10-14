#step 5 

import pandas as pd
from pathlib import Path

# ==========================================
# 1. LOAD CLEANED DATASET
# ==========================================

project_folder = Path(__file__).resolve().parent.parent

file_path = (
    project_folder
    / "data"
    / "processed"
    / "customer_shopping_behavior_cleaned.csv"
)

df = pd.read_csv(file_path)


# ==========================================
# 2. DATASET OVERVIEW
# ==========================================

print("=" * 60)
print("CONSUMER SHOPPING BEHAVIOR - EXPLORATORY DATA ANALYSIS")
print("=" * 60)

print("\n--- DATASET OVERVIEW ---")

print("Total Customers/Records:", len(df))
print("Total Columns:", len(df.columns))


# ==========================================
# 3. CUSTOMER DEMOGRAPHICS
# ==========================================

print("\n--- CUSTOMER DEMOGRAPHICS ---")

print("\nGender Distribution:")
print(df["Gender"].value_counts())

print("\nGender Percentage:")
print(
    (df["Gender"].value_counts(normalize=True) * 100)
    .round(2)
)

print("\nAge Statistics:")
print(df["Age"].describe())

print("\nAge Groups:")

age_bins = [0, 19, 29, 39, 49, 59, 120]
age_labels = [
    "Under 20",
    "20-29",
    "30-39",
    "40-49",
    "50-59",
    "60+"
]

df["Age Group"] = pd.cut(
    df["Age"],
    bins=age_bins,
    labels=age_labels,
    right=True
)

print(df["Age Group"].value_counts().sort_index())


# ==========================================
# 4. PRODUCT CATEGORY ANALYSIS
# ==========================================

print("\n--- PRODUCT CATEGORY ANALYSIS ---")

print("\nPurchase Count by Category:")
print(df["Category"].value_counts())

print("\nAverage Purchase Amount by Category:")
print(
    df.groupby("Category")["Purchase Amount (USD)"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

print("\nTotal Purchase Amount by Category:")
print(
    df.groupby("Category")["Purchase Amount (USD)"]
    .sum()
    .sort_values(ascending=False)
)


# ==========================================
# 5. PURCHASE AMOUNT ANALYSIS
# ==========================================

print("\n--- PURCHASE AMOUNT ANALYSIS ---")

print("\nPurchase Amount Statistics:")
print(df["Purchase Amount (USD)"].describe())

print("\nAverage Purchase Amount by Gender:")
print(
    df.groupby("Gender")["Purchase Amount (USD)"]
    .mean()
    .round(2)
)

print("\nAverage Purchase Amount by Age Group:")
print(
    df.groupby("Age Group", observed=False)["Purchase Amount (USD)"]
    .mean()
    .round(2)
)


# ==========================================
# 6. SEASONAL SHOPPING ANALYSIS
# ==========================================

print("\n--- SEASONAL SHOPPING ANALYSIS ---")

print("\nPurchase Count by Season:")
print(df["Season"].value_counts())

print("\nAverage Purchase Amount by Season:")
print(
    df.groupby("Season")["Purchase Amount (USD)"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

print("\nTotal Purchase Amount by Season:")
print(
    df.groupby("Season")["Purchase Amount (USD)"]
    .sum()
    .sort_values(ascending=False)
)


# ==========================================
# 7. DISCOUNT AND PROMO ANALYSIS
# ==========================================

print("\n--- DISCOUNT AND PROMO ANALYSIS ---")

print("\nDiscount Applied:")
print(df["Discount Applied"].value_counts())

print("\nPromo Code Used:")
print(df["Promo Code Used"].value_counts())

print("\nAverage Purchase Amount by Discount Status:")
print(
    df.groupby("Discount Applied")["Purchase Amount (USD)"]
    .mean()
    .round(2)
)

print("\nAverage Purchase Amount by Promo Code Status:")
print(
    df.groupby("Promo Code Used")["Purchase Amount (USD)"]
    .mean()
    .round(2)
)


# ==========================================
# 8. CUSTOMER ENGAGEMENT ANALYSIS
# ==========================================

print("\n--- CUSTOMER ENGAGEMENT ANALYSIS ---")

print("\nSubscription Status:")
print(df["Subscription Status"].value_counts())

print("\nAverage Purchase Amount by Subscription Status:")
print(
    df.groupby("Subscription Status")["Purchase Amount (USD)"]
    .mean()
    .round(2)
)

print("\nAverage Review Rating by Subscription Status:")
print(
    df.groupby("Subscription Status")["Review Rating"]
    .mean()
    .round(2)
)


# ==========================================
# 9. PAYMENT AND SHIPPING ANALYSIS
# ==========================================

print("\n--- PAYMENT AND SHIPPING ANALYSIS ---")

print("\nPayment Method Distribution:")
print(df["Payment Method"].value_counts())

print("\nShipping Type Distribution:")
print(df["Shipping Type"].value_counts())


# ==========================================
# 10. CUSTOMER PURCHASE HISTORY
# ==========================================

print("\n--- CUSTOMER PURCHASE HISTORY ---")

print("\nPrevious Purchases Statistics:")
print(df["Previous Purchases"].describe())

print("\nPurchase Frequency Distribution:")
print(df["Frequency of Purchases"].value_counts())


# ==========================================
# 11. SAVE EDA SUMMARY
# ==========================================

summary_folder = project_folder / "reports"
summary_folder.mkdir(parents=True, exist_ok=True)

summary_file = summary_folder / "eda_summary.txt"

with open(summary_file, "w", encoding="utf-8") as file:
    file.write("CONSUMER SHOPPING BEHAVIOR - EDA SUMMARY\n")
    file.write("=" * 50 + "\n\n")

    file.write("Dataset Shape:\n")
    file.write(f"Rows: {df.shape[0]}\n")
    file.write(f"Columns: {df.shape[1]}\n\n")

    file.write("Gender Distribution:\n")
    file.write(df["Gender"].value_counts().to_string() + "\n\n")

    file.write("Category Purchase Count:\n")
    file.write(df["Category"].value_counts().to_string() + "\n\n")

    file.write("Seasonal Purchase Count:\n")
    file.write(df["Season"].value_counts().to_string() + "\n\n")

    file.write("Payment Method Distribution:\n")
    file.write(df["Payment Method"].value_counts().to_string() + "\n\n")

print("\nEDA ANALYSIS COMPLETED!")
print("Summary saved to:", summary_file)