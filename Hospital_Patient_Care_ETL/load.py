from pathlib import Path
from config import OUTPUT_DIR, CLEAN_DATA

def load_data(df, path=CLEAN_DATA):
    """Load the transformed data to a CSV output."""
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"[LOAD] Saved cleaned data to: {path}")
    return path

if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data
    from validate import validate_data

    raw = extract_data()
    clean = transform_data(raw)
    validate_data(clean)
    load_data(clean)
