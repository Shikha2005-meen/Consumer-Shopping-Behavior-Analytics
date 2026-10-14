#step 6


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# Create output folder
charts_folder = project_folder / "reports" / "charts"
charts_folder.mkdir(parents=True, exist_ok=True)

# Professional chart settings
sns.set_theme(style="whitegrid")

print("Dataset loaded successfully!")
print("Creating visualizations...")


# ==========================================
# 2. CHART 1: PURCHASES BY CATEGORY
# ==========================================

category_counts = df["Category"].value_counts()

plt.figure(figsize=(10, 6))

sns.barplot(
    x=category_counts.index,
    y=category_counts.values
)

plt.title("Number of Purchases by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Number of Records")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()

plt.savefig(
    charts_folder / "01_purchases_by_category.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ==========================================
# 3. CHART 2: PURCHASE AMOUNT DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Purchase Amount (USD)",
    bins=20,
    kde=True
)

plt.title("Distribution of Purchase Amounts")
plt.xlabel("Purchase Amount (USD)")
plt.ylabel("Number of Records")
plt.tight_layout()

plt.savefig(
    charts_folder / "02_purchase_amount_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ==========================================
# 4. CHART 3: AVERAGE AMOUNT BY CATEGORY
# ==========================================

category_amount = (
    df.groupby("Category")["Purchase Amount (USD)"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=category_amount.index,
    y=category_amount.values
)

plt.title("Average Purchase Amount by Category")
plt.xlabel("Product Category")
plt.ylabel("Average Purchase Amount (USD)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()

plt.savefig(
    charts_folder / "03_average_amount_by_category.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ==========================================
# 5. CHART 4: REVIEW RATING DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Review Rating",
    bins=15,
    kde=True
)

plt.title("Distribution of Customer Review Ratings")
plt.xlabel("Review Rating")
plt.ylabel("Number of Records")
plt.tight_layout()

plt.savefig(
    charts_folder / "04_review_rating_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ==========================================
# 6. CHART 5: PURCHASE AMOUNT BY SEASON
# ==========================================

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="Season",
    y="Purchase Amount (USD)"
)

plt.title("Purchase Amount Distribution by Season")
plt.xlabel("Season")
plt.ylabel("Purchase Amount (USD)")
plt.tight_layout()

plt.savefig(
    charts_folder / "05_purchase_amount_by_season.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ==========================================
# 7. FINISH
# ==========================================

print("\nAll 5 visualizations created successfully!")

print("Charts saved in:")
print(charts_folder)

print("\nGenerated files:")
for chart_file in sorted(charts_folder.glob("*.png")):
    print("-", chart_file.name)