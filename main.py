from pathlib import Path

import pandas as pd

from src1.cleaning import clean_data
from src1.analysis import (
    calculate_profit,
    monthly_profit,
    category_summary
)


base_dir = Path(__file__).resolve().parent

csv_path = (
    base_dir
    / "Data"
    / "Finance2025 - Dados 2025.csv"
)


# Load data
df = pd.read_csv(csv_path)


# Cleaning
df = clean_data(df)


# Analysis

profit = calculate_profit(df)

monthly = monthly_profit(df)

summary = category_summary(df)


print("--------------------")
print(f"Total Profit: R$ {profit:.2f}")


print("\nMonthly Profit")
print(monthly)


print("\nCategory Summary")
print(summary)

monthly.to_csv(
    "outputs/monthly_profit.csv"
)


summary.to_csv(
    "outputs/financial_summary.csv"
)