# extract.py

import pandas as pd
import os


def extract_candidates(file_path: str) -> pd.DataFrame:
    
    # 1️⃣ Validate file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    print("File found. Reading CSV...")
    
    # 2️⃣ Read CSV (correct separator ;)
    try:
        df = pd.read_csv(file_path, sep=';')
    except Exception as e:
        raise RuntimeError(f"Error reading CSV: {e}")
    
    print("CSV loaded successfully.")
    
    # 3️⃣ Validate expected columns (order-independent)
    expected_columns = [
        "First Name",
        "Last Name",
        "Email",
        "Country",
        "Application Date",
        "YOE",
        "Seniority",
        "Technology",
        "Code Challenge Score",
        "Technical Interview Score"
    ]
    
    missing_cols = set(expected_columns) - set(df.columns)
    
    if missing_cols:
        print("Columns found in CSV:", list(df.columns))
        raise ValueError(f"Missing columns in CSV: {missing_cols}")
    
    print("Column structure validated.")
    
    # 4️⃣ Basic validation info (no transformations here)
    print("\nInitial Data Types:")
    print(df.dtypes)
    
    print("\nTotal rows extracted:", len(df))
    
    return df