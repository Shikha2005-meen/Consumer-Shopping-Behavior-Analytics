#step 7 

import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats

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

print("=" * 60)
print("CONSUMER SHOPPING BEHAVIOR")
print("STATISTICAL ANALYSIS")
print("=" * 60)


# ==========================================
# 2. DESCRIPTIVE STATISTICS
# ==========================================

print("\n--- 1. DESCRIPTIVE STATISTICS ---")

amount = df["Purchase Amount (USD)"]

print("Mean:", round(amount.mean(), 2))
print("Median:", round(amount.median(), 2))
print("Standard Deviation:", round(amount.std(), 2))
print("Minimum:", amount.min())
print("Maximum:", amount.max())
print("25th Percentile:", amount.quantile(0.25))
print("75th Percentile:", amount.quantile(0.75))


# ==========================================
# 3. CATEGORY-WISE AMOUNT SUMMARY
# ==========================================

print("\n--- 2. CATEGORY-WISE STATISTICS ---")

category_summary = (
    df.groupby("Category")["Purchase Amount (USD)"]
    .agg(["count", "mean", "median", "std"])
    .round(2)
    .sort_values("mean", ascending=False)
)

print(category_summary)


# ==========================================
# 4. CORRELATION ANALYSIS
# ==========================================

print("\n--- 3. CORRELATION ANALYSIS ---")

correlation = df[
    ["Age", "Purchase Amount (USD)", "Review Rating",
     "Previous Purchases"]
].corr()

print(correlation.round(3))

rating_correlation = df[
    ["Purchase Amount (USD)", "Review Rating"]
].corr().iloc[0, 1]

print(
    "\nPurchase Amount vs Review Rating Correlation:",
    round(rating_correlation, 3)
)


# ==========================================
# 5. DISCOUNT GROUP COMPARISON
# ==========================================

print("\n--- 4. DISCOUNT GROUP COMPARISON ---")

discount_groups = df.groupby("Discount Applied")[
    "Purchase Amount (USD)"
]

print(discount_groups.agg(["count", "mean", "median", "std"]).round(2))

groups = [
    group["Purchase Amount (USD)"].dropna().to_numpy()
    for _, group in df.groupby("Discount Applied")
]

if len(groups) == 2:
    test_result = stats.ttest_ind(
        groups[0],
        groups[1],
        equal_var=False
    )

    print("Welch t-test statistic:", round(test_result.statistic, 4))
    print("Welch t-test p-value:", round(test_result.pvalue, 4))


# ==========================================
# 6. SUBSCRIPTION GROUP COMPARISON
# ==========================================

print("\n--- 5. SUBSCRIPTION GROUP COMPARISON ---")

subscription_summary = (
    df.groupby("Subscription Status")["Purchase Amount (USD)"]
    .agg(["count", "mean", "median", "std"])
    .round(2)
)

print(subscription_summary)

subscription_groups = [
    group["Purchase Amount (USD)"].dropna().to_numpy()
    for _, group in df.groupby("Subscription Status")
]

if len(subscription_groups) == 2:
    subscription_test = stats.ttest_ind(
        subscription_groups[0],
        subscription_groups[1],
        equal_var=False
    )

    print(
        "Welch t-test statistic:",
        round(subscription_test.statistic, 4)
    )
    print(
        "Welch t-test p-value:",
        round(subscription_test.pvalue, 4)
    )


# ==========================================
# 7. CATEGORY DIFFERENCES: ONE-WAY ANOVA
# ==========================================

print("\n--- 6. CATEGORY-WISE ANOVA ---")

category_groups = [
    group["Purchase Amount (USD)"].dropna().to_numpy()
    for _, group in df.groupby("Category")
]

if len(category_groups) >= 2:
    anova_result = stats.f_oneway(*category_groups)

    print("ANOVA F-statistic:", round(anova_result.statistic, 4))
    print("ANOVA p-value:", round(anova_result.pvalue, 4))


# ==========================================
# 8. SAVE RESULTS
# ==========================================

reports_folder = project_folder / "reports"
reports_folder.mkdir(parents=True, exist_ok=True)

output_file = reports_folder / "statistical_analysis.txt"

with open(output_file, "w", encoding="utf-8") as file:
    file.write("STATISTICAL ANALYSIS SUMMARY\n")
    file.write("=" * 40 + "\n\n")

    file.write("Descriptive Statistics:\n")
    file.write(amount.describe().to_string() + "\n\n")

    file.write("Category Summary:\n")
    file.write(category_summary.to_string() + "\n\n")

    file.write("Correlation Matrix:\n")
    file.write(correlation.round(3).to_string() + "\n\n")

    file.write("Subscription Summary:\n")
    file.write(subscription_summary.to_string() + "\n")

print("\nStatistical analysis completed!")
print("Report saved to:", output_file)