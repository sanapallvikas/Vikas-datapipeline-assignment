from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
RAW_DATA = BASE_DIR / "hospital_patient_analytics_dataset.csv"
OUTPUT_DIR = BASE_DIR / "output"
CLEAN_DATA = OUTPUT_DIR / "cleaned_hospital_patient_data.csv"
MODEL_RESULTS = OUTPUT_DIR / "model_results.csv"

TARGET_COLUMN = "High_Risk"

NUMERIC_COLUMNS = [
    "Age",
    "Heart_Rate",
    "Systolic_BP",
    "Diastolic_BP",
    "SpO2",
    "Glucose",
    "Previous_Admissions",
    "Previous_Visits",
    "Abnormal_Lab_Count",
    "Waiting_Time_Min",
]

RISK_FEATURES = [
    "Age",
    "Heart_Rate",
    "Systolic_BP",
    "Diastolic_BP",
    "SpO2",
    "Glucose",
    "Previous_Admissions",
    "Previous_Visits",
    "Abnormal_Lab_Count",
]
