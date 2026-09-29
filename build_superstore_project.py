"""Starter script for the Python / Pandas phase of the project.

This script does not complete the full project. It only gives a quick, valid
starting point for the actual analysis phase.
"""

from pathlib import Path

import pandas as pd

raw_path = Path(r"e:\endtoend\Sample - Superstore.csv")

if not raw_path.exists():
    raise FileNotFoundError(f"Raw dataset not found: {raw_path}")

# Only load the raw data at the Python phase.
df = pd.read_csv(raw_path, encoding="cp1252")

print("Head:")
print(df.head())
print("\nShape:", df.shape)
print("\nColumns:", list(df.columns))
print("\nInfo:")
df.info()
print("\nDescribe:")
print(df.describe(include="all").T)
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:", int(df.duplicated().sum()))

print("\nUse this notebook/script to continue with:")
print("- data type validation")
print("- missing-value checks")
print("- duplicate review")
print("- monthly, category, region, segment, product, customer analysis")
print("- discount vs profit analysis")
print("- shipping analysis")
