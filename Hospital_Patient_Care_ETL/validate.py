import pandas as pd
from config import TARGET_COLUMN, RISK_FEATURES

def validate_data(df):
    """Run basic data-quality checks before loading."""
    required = set(RISK_FEATURES + [TARGET_COLUMN, "Patient_ID", "Gender", "Department"])
    missing_columns = required - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    if df.empty:
        raise ValueError("Dataset is empty.")

    if df["Patient_ID"].duplicated().any():
        print("[VALIDATE] Warning: duplicate Patient_ID values detected.")

    missing_count = int(df.isnull().sum().sum())
    if missing_count > 0:
        raise ValueError(f"Validation failed: {missing_count} missing values remain.")

    if not df[TARGET_COLUMN].isin([0, 1]).all():
        raise ValueError("High_Risk must contain only 0 and 1.")

    print("[VALIDATE] All required columns are present.")
    print("[VALIDATE] No missing values remain.")
    print("[VALIDATE] Target values are valid.")
    print("[VALIDATE] Validation successful.")
    return True
