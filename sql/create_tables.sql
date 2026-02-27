PRAGMA foreign_keys = ON;

-- =========================
-- Drop tables (orden correcto)
-- =========================

DROP TABLE IF EXISTS fact_applications;
DROP TABLE IF EXISTS dim_candidate;
DROP TABLE IF EXISTS dim_country;
DROP TABLE IF EXISTS dim_technology;
DROP TABLE IF EXISTS dim_seniority;
DROP TABLE IF EXISTS dim_date;

-- =========================
-- Dimension Tables
-- =========================

CREATE TABLE dim_candidate (
    candidate_key INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    yoe INTEGER NOT NULL
);

CREATE TABLE dim_country (
    country_key INTEGER PRIMARY KEY,
    country TEXT NOT NULL
);

CREATE TABLE dim_technology (
    technology_key INTEGER PRIMARY KEY,
    technology TEXT NOT NULL
);

CREATE TABLE dim_seniority (
    seniority_key INTEGER PRIMARY KEY,
    seniority TEXT NOT NULL
);

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY,
    full_date TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    month_name TEXT NOT NULL,
    quarter INTEGER NOT NULL
);

-- =========================
-- Fact Table
-- =========================

CREATE TABLE fact_applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    candidate_key INTEGER NOT NULL,
    country_key INTEGER NOT NULL,
    technology_key INTEGER NOT NULL,
    seniority_key INTEGER NOT NULL,
    date_key INTEGER NOT NULL,

    code_challenge_score INTEGER NOT NULL,
    technical_interview_score INTEGER NOT NULL,
    hired_flag INTEGER NOT NULL,

    FOREIGN KEY (candidate_key) REFERENCES dim_candidate(candidate_key),
    FOREIGN KEY (country_key) REFERENCES dim_country(country_key),
    FOREIGN KEY (technology_key) REFERENCES dim_technology(technology_key),
    FOREIGN KEY (seniority_key) REFERENCES dim_seniority(seniority_key),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
);