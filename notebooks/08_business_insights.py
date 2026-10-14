#step 8

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

reports_folder = project_folder / "reports"
reports_folder.mkdir(parents=True, exist_ok=True)

report_file = reports_folder / "business_insights.txt"

amount_col = "Purchase Amount (USD)"

insights = []

insights.append("CONSUMER SHOPPING BEHAVIOR ANALYTICS")
insights.append("BUSINESS INSIGHTS AND RECOMMENDATIONS")
insights.append("=" * 55)

# ==========================================
# 2. OVERALL BUSINESS SUMMARY
# ==========================================

total_records = len(df)
average_amount = df[amount_col].mean()
total_purchase_amount = df[amount_col].sum()
average_rating = df["Review Rating"].mean()

insights.append("\n1. OVERALL DATASET SUMMARY")
insights.append(f"Total records: {total_records}")
insights.append(f"Total recorded purchase amount: ${total_purchase_amount:,.2f}")
insights.append(f"Average purchase amount: ${average_amount:.2f}")
insights.append(f"Average review rating: {average_rating:.2f}")

# ==========================================
# 3. PRODUCT CATEGORY INSIGHTS
# ==========================================

category_summary = (
    df.groupby("Category")
    .agg(
        purchase_records=(amount_col, "count"),
        total_amount=(amount_col, "sum"),
        average_amount=(amount_col, "mean")
    )
    .sort_values("total_amount", ascending=False)
)

top_category = category_summary.index[0]
top_category_amount = category_summary.iloc[0]["total_amount"]

lowest_avg_category = (
    category_summary["average_amount"].idxmin()
)

insights.append("\n2. PRODUCT CATEGORY INSIGHTS")
insights.append(
    f"Category with the highest total recorded purchase amount: "
    f"{top_category} (${top_category_amount:,.2f})"
)
insights.append(
    f"Category with the lowest average purchase amount: "
    f"{lowest_avg_category} "
    f"(${category_summary.loc[lowest_avg_category, 'average_amount']:.2f})"
)

insights.append("\nCategory performance:")
insights.append(category_summary.round(2).to_string())

# ==========================================
# 4. CUSTOMER DEMOGRAPHICS
# ==========================================

gender_counts = df["Gender"].value_counts()
age_summary = (
    df.groupby("Age")
    .size()
    .sort_values(ascending=False)
)

insights.append("\n3. CUSTOMER DEMOGRAPHICS")

insights.append(
    f"Most represented gender category: {gender_counts.index[0]} "
    f"({gender_counts.iloc[0]} records)"
)

insights.append(
    f"Most frequently represented age in the dataset: "
    f"{age_summary.index[0]} ({age_summary.iloc[0]} records)"
)

# ==========================================
# 5. SEASONAL INSIGHTS
# ==========================================

season_summary = (
    df.groupby("Season")
    .agg(
        purchase_records=(amount_col, "count"),
        total_amount=(amount_col, "sum"),
        average_amount=(amount_col, "mean")
    )
    .sort_values("total_amount", ascending=False)
)

best_season = season_summary.index[0]

insights.append("\n4. SEASONAL SHOPPING INSIGHTS")
insights.append(
    f"Season with the highest total recorded purchase amount: "
    f"{best_season} "
    f"(${season_summary.iloc[0]['total_amount']:,.2f})"
)
insights.append(season_summary.round(2).to_string())

# ==========================================
# 6. DISCOUNT ANALYSIS
# ==========================================

discount_summary = (
    df.groupby("Discount Applied")[amount_col]
    .agg(["count", "mean", "median"])
    .round(2)
)

insights.append("\n5. DISCOUNT ANALYSIS")
insights.append(discount_summary.to_string())

# ==========================================
# 7. SUBSCRIPTION ANALYSIS
# ==========================================

subscription_summary = (
    df.groupby("Subscription Status")
    .agg(
        records=(amount_col, "count"),
        average_amount=(amount_col, "mean"),
        average_rating=("Review Rating", "mean")
    )
    .round(2)
)

insights.append("\n6. SUBSCRIPTION ANALYSIS")
insights.append(subscription_summary.to_string())

# ==========================================
# 8. PAYMENT METHOD ANALYSIS
# ==========================================

payment_counts = df["Payment Method"].value_counts()

insights.append("\n7. PAYMENT METHOD INSIGHTS")
insights.append(
    f"Most frequently recorded payment method: "
    f"{payment_counts.index[0]} "
    f"({payment_counts.iloc[0]} records)"
)
insights.append(payment_counts.to_string())

# ==========================================
# 9. BUSINESS RECOMMENDATIONS
# ==========================================

insights.append("\n8. POTENTIAL BUSINESS RECOMMENDATIONS")

insights.append(
    "1. Product strategy: Review category-level purchase amounts "
    "and record counts before deciding inventory or marketing priorities."
)

insights.append(
    "2. Seasonal planning: Compare seasonal patterns when planning "
    "campaigns, but validate them with additional time-based data."
)

insights.append(
    "3. Promotions: Compare discount groups, while avoiding claims "
    "that discounts caused higher spending."
)

insights.append(
    "4. Customer engagement: Compare subscription groups and investigate "
    "whether observed differences are meaningful."
)

insights.append(
    "5. Customer experience: Review rating distributions and investigate "
    "the reasons behind low ratings before proposing improvements."
)

insights.append(
    "\nImportant limitation: These are observational dataset findings. "
    "Purchase amount is not profit, and group differences do not establish "
    "causation. Recommendations require validation before implementation."
)

# ==========================================
# 10. SAVE REPORT
# ==========================================

report_text = "\n".join(insights)

with open(report_file, "w", encoding="utf-8") as file:
    file.write(report_text)

print(report_text)

print("\n" + "=" * 55)
print("BUSINESS INSIGHTS REPORT GENERATED SUCCESSFULLY!")
print("Saved at:", report_file)
