# etl/load.py

import sqlite3
import os


def load_to_dw(tables_dict, db_path="data/warehouse/data_warehouse.db"):

    print("Starting Load phase...")

    # 1️⃣ Ensure warehouse directory exists
    os.makedirs("data/warehouse", exist_ok=True)

    # 2️⃣ Connect to SQLite DW
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 3️⃣ Execute physical model from SQL file
    with open("sql/create_tables.sql", "r", encoding="utf-8") as f:
        cursor.executescript(f.read())

    print("Tables created successfully from SQL script.")

    # =========================
    # 4️⃣ Insert Dimension Tables
    # =========================

    tables_dict["dim_candidate"].rename(columns={
        "First Name": "first_name",
        "Last Name": "last_name"
    }).to_sql("dim_candidate", conn, if_exists="append", index=False)

    tables_dict["dim_country"].rename(columns={
        "Country": "country"
    }).to_sql("dim_country", conn, if_exists="append", index=False)

    tables_dict["dim_technology"].rename(columns={
        "Technology": "technology"
    }).to_sql("dim_technology", conn, if_exists="append", index=False)

    tables_dict["dim_seniority"].rename(columns={
        "Seniority": "seniority"
    }).to_sql("dim_seniority", conn, if_exists="append", index=False)

    tables_dict["dim_date"].to_sql("dim_date", conn, if_exists="append", index=False)

    print("Dimensions loaded successfully.")

    # =========================
    # 5️⃣ Insert Fact Table
    # =========================

    tables_dict["fact_applications"].rename(columns={
        "Code Challenge Score": "code_challenge_score",
        "Technical Interview Score": "technical_interview_score"
    }).to_sql("fact_applications", conn, if_exists="append", index=False)

    print("Fact table loaded successfully.")

    conn.commit()
    conn.close()

    print("Load phase completed successfully.")