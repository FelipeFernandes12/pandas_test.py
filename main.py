from pathlib import Path

import pandas as pd

from src1.cleaning import clean_data
from src1.analysis import calculate_profit


base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "Data" / "Finance2025 - Dados 2025.csv"


df = pd.read_csv(csv_path)
df = clean_data(df)

profit = calculate_profit(df)

print(f"Lucro total: {profit:.2f}")