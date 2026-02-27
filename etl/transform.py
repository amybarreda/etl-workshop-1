# src/transform.py

import pandas as pd


def transform_candidates(df: pd.DataFrame):

    print("Starting transformation phase...")

    #Data Type Corrections
    df["Application Date"] = pd.to_datetime(df["Application Date"])
    df["YOE"] = df["YOE"].astype(int)
    df["Code Challenge Score"] = df["Code Challenge Score"].astype(int)
    df["Technical Interview Score"] = df["Technical Interview Score"].astype(int)

    #Apply HIRED rule
    df["hired_flag"] = (
        (df["Code Challenge Score"] >= 7) &
        (df["Technical Interview Score"] >= 7)
    ).astype(int)

    #Create dim_candidate
    dim_candidate = (
        df[["First Name", "Last Name", "Email", "YOE"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    dim_candidate["candidate_key"] = dim_candidate.index + 1

    #Create dim_country

    dim_country = (
        df[["Country"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    dim_country["country_key"] = dim_country.index + 1

    #Create dim_technology

    dim_technology = (
        df[["Technology"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    dim_technology["technology_key"] = dim_technology.index + 1

    #Create dim_seniority

    dim_seniority = (
        df[["Seniority"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )
    dim_seniority["seniority_key"] = dim_seniority.index + 1

    #Create dim_date

    dim_date = pd.DataFrame()
    dim_date["full_date"] = df["Application Date"].drop_duplicates().sort_values()
    dim_date = dim_date.reset_index(drop=True)

    dim_date["date_key"] = dim_date["full_date"].dt.strftime("%Y%m%d").astype(int)
    dim_date["year"] = dim_date["full_date"].dt.year
    dim_date["month"] = dim_date["full_date"].dt.month
    dim_date["month_name"] = dim_date["full_date"].dt.month_name()
    dim_date["quarter"] = dim_date["full_date"].dt.quarter

    #Build Fact Table
    
    # Merge candidate
    fact = df.merge(dim_candidate, on=["First Name", "Last Name", "Email", "YOE"])
    
    # Merge country
    fact = fact.merge(dim_country, on="Country")
    
    # Merge technology
    fact = fact.merge(dim_technology, on="Technology")
    
    # Merge seniority
    fact = fact.merge(dim_seniority, on="Seniority")
    
    # Merge date
    fact = fact.merge(dim_date, left_on="Application Date", right_on="full_date")

    fact_applications = fact[[
        "candidate_key",
        "country_key",
        "technology_key",
        "seniority_key",
        "date_key",
        "Code Challenge Score",
        "Technical Interview Score",
        "hired_flag"
    ]]

    print("Transformation completed successfully.")

    return {
        "dim_candidate": dim_candidate,
        "dim_country": dim_country,
        "dim_technology": dim_technology,
        "dim_seniority": dim_seniority,
        "dim_date": dim_date,
        "fact_applications": fact_applications
    }