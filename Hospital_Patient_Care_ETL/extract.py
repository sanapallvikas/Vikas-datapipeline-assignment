import pandas as pd
from config import RAW_DATA

def extract_data(path=RAW_DATA):
    """Extract hospital patient data from CSV."""
    df = pd.read_csv(path)
    print(f"[EXTRACT] Loaded {len(df)} rows and {len(df.columns)} columns.")
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())
