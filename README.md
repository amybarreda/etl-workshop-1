# 🚀 ETL Workshop 1 – Data Engineering Project

> End-to-end ETL pipeline with Dimensional Modeling and Analytical KPIs using SQLite.

This project utilized AI and LLM

primarily to make the README more visually appealing and understandable
---

## 📌 Project Objective

This project implements a complete **ETL pipeline** for a recruitment dataset containing **50,000 candidate applications**.

It simulates a real-world Data Engineering challenge involving:

- ⭐ Dimensional Data Modeling (Star Schema)
- 🔄 ETL implementation in Python
- 🗄️ Data Warehouse loading (SQLite)
- 📊 Analytical KPI generation from the DW
- 📈 Data visualization using SQL-driven queries

The goal is to demonstrate strong data modeling decisions, ETL architecture design, and analytical reasoning.

---

# 🏗️ Dimensional Data Model (Star Schema)

## ⭐ Fact Table: `fact_applications`

The fact table stores measurable recruitment events.

### 📍 Grain Definition

> One row represents one candidate application evaluated for a specific technology on a specific date.

### Measures

- `code_challenge_score`
- `technical_interview_score`
- `hired_flag`

### Foreign Keys

- `candidate_key`
- `country_key`
- `technology_key`
- `seniority_key`
- `date_key`

---

## 📦 Dimension Tables

| Dimension | Description |
|------------|-------------|
| `dim_candidate` | Candidate personal & experience data |
| `dim_country` | Country information |
| `dim_technology` | Applied technology |
| `dim_seniority` | Seniority level |
| `dim_date` | Time attributes (year, month, quarter) |

All dimensions use **surrogate keys**, following Data Warehouse best practices.

Natural keys from the CSV (e.g., email) were NOT used as primary keys.

---

# 🧠 Design Decisions

### ✔ Business Rule Implementation

A candidate is considered **HIRED** if:

```

Code Challenge Score ≥ 7 AND Technical Interview Score ≥ 7

```

This logic is applied during the **Transform phase**.

### ✔ Architectural Decisions

- Clear separation of Extract, Transform, and Load
- Surrogate keys for scalability
- Dedicated `dim_date` for time analysis
- All KPIs generated from the Data Warehouse (never from CSV)

---

# 🔄 ETL Pipeline

## 1️⃣ Extract

- Load CSV file
- Validate file structure
- Validate expected columns
- Inspect data types

## 2️⃣ Transform

- Correct data types
- Apply business rule (`hired_flag`)
- Create dimension tables
- Generate surrogate keys
- Build fact table aligned with defined grain

## 3️⃣ Load

- Execute `create_tables.sql`
- Insert dimension tables
- Insert fact table
- Enforce referential integrity

---

# 📊 KPIs & Visualizations

All KPIs are generated using SQL queries executed directly against the SQLite Data Warehouse.

## Implemented KPIs

1. Hires by Technology
2. Hires by Year
3. Hires by Seniority
4. Hires by Country over Years (USA, Brazil, Colombia, Ecuador)
5. Overall Hire Rate (%)
6. Average Code Challenge Score by Technology

Visualizations are implemented in:

```

visualization/kpi_dashboard.py

```

All charts are based strictly on DW queries.

---

# 📁 Project Structure

```

etl-workshop-1/
│
├── data/
│   ├── raw/
│   │   └── candidates.csv
│   └── warehouse/
│       └── data_warehouse.db
│
├── notebooks/
│   └── eda.ipynb
│
├── sql/
│   ├── create_tables.sql
│   └── queries.sql
│
├── diagrams/
│   └── star_schema.png
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── visualization/
│   └── kpi_dashboard.py
│
├── requirements.txt
├── .gitignore
└── README.md

````

---

# ▶️ How to Run the Project

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
````

## 2️⃣ Run ETL Pipeline

```bash
python -m etl.main
```

This will create:

```
data/warehouse/data_warehouse.db
```

## 3️⃣ Generate Visualizations

```bash
python visualization/kpi_dashboard.py
```

---

# 🔍 Data Quality Assumptions

* Each row represents one candidate application.
* Email uniquely identifies candidates in source data.
* No duplicate application events exist for the same candidate + technology + date.
* Scores are numeric and within valid ranges.
* Missing values were minimal and did not require imputation.

---

# 📈 Example Insights

* Hiring rate indicates a selective recruitment process.
* Technology hiring distribution reveals demand concentration.
* Seniority analysis shows which levels are most successfully hired.
* Yearly trend analysis highlights recruitment growth patterns.

---

# 🎓 Key Learnings

* Grain definition drives dimensional model correctness.
* Proper separation of ETL stages improves maintainability.
* Surrogate keys are critical in scalable DW systems.
* Visualization design significantly affects interpretability.
* Analytical value must come from the Data Warehouse, not raw data.

---

# 👩‍💻 Author

**Amy B**
Data Engineering & Artificial Intelligence Student
