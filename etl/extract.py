#extract.py

import pandas as pd
import os


def extract_candidates(file_path: str) -> pd.DataFrame:
    
    # 1️⃣ Validar que el archivo exista
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    print("File found. Reading CSV...")
    
    # 2️⃣ Leer el CSV (sabemos que usa ;)
    df = pd.read_csv(file_path, sep=';')
    
    print("CSV loaded successfully.")
    
    # 3️⃣ Validar columnas esperadas
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
    
    if list(df.columns) != expected_columns:
        raise ValueError("Unexpected column structure in CSV.")
    
    print("Column structure validated.")
    
    # 4️⃣ Validación básica de tipos (sin transformar aún)
    print("\nInitial Data Types:")
    print(df.dtypes)
    
    print("\nTotal rows extracted:", len(df))
    
    return df