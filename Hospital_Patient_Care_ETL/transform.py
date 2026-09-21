import pandas as pd
from config import NUMERIC_COLUMNS

def transform_data(df):
    """Clean and transform the extracted hospital dataset."""
    data = df.copy()

    # Remove exact duplicate records.
    before = len(data)
    data = data.drop_duplicates()
    print(f"[TRANSFORM] Removed {before - len(data)} duplicate rows.")

    # Convert numeric fields safely.
    for col in NUMERIC_COLUMNS:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")

    # Impute missing numeric values with the median.
    for col in NUMERIC_COLUMNS:
        if col in data.columns:
            data[col] = data[col].fillna(data[col].median())

    # Standardize categorical text.
    if "Gender" in data.columns:
        data["Gender"] = data["Gender"].astype(str).str.strip().str.title()
    if "Department" in data.columns:
        data["Department"] = data["Department"].astype(str).str.strip()

    # Add a useful operational feature.
    if "Waiting_Time_Min" in data.columns:
        data["Waiting_Time_Category"] = pd.cut(
            data["Waiting_Time_Min"],
            bins=[-1, 15, 30, 60, float("inf")],
            labels=["Short", "Moderate", "Long", "Very Long"]
        )

    print("[TRANSFORM] Missing values after cleaning:")
    print(data.isnull().sum())
    return data
