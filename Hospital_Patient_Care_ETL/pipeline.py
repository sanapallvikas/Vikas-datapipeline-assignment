from extract import extract_data
from transform import transform_data
from validate import validate_data
from load import load_data

def run_pipeline():
    print("=" * 60)
    print("HOSPITAL PATIENT CARE ANALYTICS - ETL PIPELINE")
    print("=" * 60)

    # E - Extract
    raw_data = extract_data()

    # T - Transform
    transformed_data = transform_data(raw_data)

    # Validate
    validate_data(transformed_data)

    # L - Load
    output_path = load_data(transformed_data)

    print("=" * 60)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)
    return transformed_data, output_path

if __name__ == "__main__":
    run_pipeline()
