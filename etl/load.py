# src/load.py

import sqlite3


def load_to_dw(tables_dict, db_path="data/warehouse/data_warehouse.db"):

    print("Starting Load phase...")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # =========================
    # 1️⃣ Create Tables
    # =========================

    cursor.executescript("""
    
    PRAGMA foreign_keys = ON;

    DROP TABLE IF EXISTS fact_applications;
    DROP TABLE IF EXISTS dim_candidate;
    DROP TABLE IF EXISTS dim_country;
    DROP TABLE IF EXISTS dim_technology;
    DROP TABLE IF EXISTS dim_seniority;
    DROP TABLE IF EXISTS dim_date;

    CREATE TABLE dim_candidate (
        candidate_key INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        yoe INTEGER
    );

    CREATE TABLE dim_country (
        country_key INTEGER PRIMARY KEY,
        country TEXT
    );

    CREATE TABLE dim_technology (
        technology_key INTEGER PRIMARY KEY,
        technology TEXT
    );

    CREATE TABLE dim_seniority (
        seniority_key INTEGER PRIMARY KEY,
        seniority TEXT
    );

    CREATE TABLE dim_date (
        date_key INTEGER PRIMARY KEY,
        full_date TEXT,
        year INTEGER,
        month INTEGER,
        month_name TEXT,
        quarter INTEGER
    );

    CREATE TABLE fact_applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        candidate_key INTEGER,
        country_key INTEGER,
        technology_key INTEGER,
        seniority_key INTEGER,
        date_key INTEGER,
        code_challenge_score INTEGER,
        technical_interview_score INTEGER,
        hired_flag INTEGER,

        FOREIGN KEY(candidate_key) REFERENCES dim_candidate(candidate_key),
        FOREIGN KEY(country_key) REFERENCES dim_country(country_key),
        FOREIGN KEY(technology_key) REFERENCES dim_technology(technology_key),
        FOREIGN KEY(seniority_key) REFERENCES dim_seniority(seniority_key),
        FOREIGN KEY(date_key) REFERENCES dim_date(date_key)
    );

    """)

    print("Tables created successfully.")

    # =========================
    # 2️⃣ Insert Dimensions
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

    print("Dimensions loaded.")

    # =========================
    # 3️⃣ Insert Fact Table
    # =========================

    tables_dict["fact_applications"].rename(columns={
        "Code Challenge Score": "code_challenge_score",
        "Technical Interview Score": "technical_interview_score"
    }).to_sql("fact_applications", conn, if_exists="append", index=False)

    print("Fact table loaded.")

    conn.commit()
    conn.close()

    print("Load phase completed successfully.")