```markdown
# ETL Workshop 1 – Data Engineering Project

## 📌 Project Objective

The objective of this project is to design and implement a complete ETL pipeline for a recruitment dataset containing 50,000 candidate applications.

The project simulates a real-world Data Engineering challenge, including:

- Designing a Dimensional Data Model (Star Schema)
- Implementing an ETL process in Python
- Loading the transformed data into a Data Warehouse (SQLite)
- Generating analytical KPIs directly from the Data Warehouse
- Creating visualizations based exclusively on DW queries

This project demonstrates data modeling decisions, ETL logic, analytical thinking, and professional documentation practices.

---

## 🏗️ Star Schema Design

### ⭐ Fact Table: `fact_applications`

The fact table stores measurable recruitment events.

**Grain Definition:**

> One row represents one candidate application evaluated for a specific technology on a specific date.

Each record contains:

- `candidate_key`
- `country_key`
- `technology_key`
- `seniority_key`
- `date_key`
- `code_challenge_score`
- `technical_interview_score`
- `hired_flag`

---

### 📦 Dimension Tables

The following dimension tables were designed:

- `dim_candidate`
- `dim_country`
- `dim_technology`
- `dim_seniority`
- `dim_date`

Each dimension uses surrogate keys (not natural keys from the CSV), ensuring proper Data Warehouse design principles.

The `dim_date` table enables time-based analysis such as yearly hiring trends.

---

## 🧠 Design Decisions

- Surrogate keys were generated for all dimensions.
- Natural keys (e.g., email) were NOT used as primary keys in the Data Warehouse.
- The business rule for hiring was implemented during the Transform phase:
  
```

A candidate is HIRED if:
Code Challenge Score ≥ 7 AND Technical Interview Score ≥ 7

```

- All transformations were performed in Python before loading into the DW.
- All analytical queries were executed from the Data Warehouse (not from the CSV).

---

## 🔄 ETL Process

The ETL pipeline is structured into three main stages:

### 1️⃣ Extract
- Load CSV file
- Validate file existence
- Validate column structure
- Perform initial data inspection

### 2️⃣ Transform
- Correct data types
- Apply business rule (`hired_flag`)
- Create dimension tables
- Generate surrogate keys
- Build the fact table aligned with the defined grain

### 3️⃣ Load
- Create tables in SQLite using `create_tables.sql`
- Insert dimension tables
- Insert fact table
- Ensure referential integrity

---

## 📊 KPIs & Visualizations

All KPIs were generated using SQL queries executed directly against the Data Warehouse.

The following KPIs were implemented:

1. Hires by Technology
2. Hires by Year
3. Hires by Seniority
4. Hires by Country over Years (USA, Brazil, Colombia, Ecuador)
5. Overall Hire Rate (%)
6. Average Code Challenge Score by Technology

Visualizations were implemented using Python (matplotlib) and are available in:

```

visualization/kpi_dashboard.py

```

All charts are generated from DW queries, ensuring proper ETL workflow compliance.

---

## 📁 Project Structure

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
├── README.md
├── requirements.txt
└── .gitignore

````

---

## ▶️ How to Run the Project

### 1° Install dependencies

```bash
pip install -r requirements.txt
````

### 2° Run the ETL pipeline

```bash
python -m etl.main
```

This will:

* Extract data
* Transform data
* Load into SQLite Data Warehouse

The DW will be created at:

```
data/warehouse/data_warehouse.db
```

### 3° Generate Visualizations

```bash
python visualization/kpi_dashboard.py
```

---

## 🔍 Data Quality Assumptions

* The dataset contains one row per candidate application.
* Email uniquely identifies a candidate in the source data.
* No duplicate applications exist for the same candidate, technology, and date combination.
* Missing values were assumed to be minimal and did not require complex imputation.
* Scores are numeric and valid within expected ranges.

---

## 📈 Example Outputs

Example generated visualizations include:

* Top 10 Technologies by Hires
* Hiring Trends by Year
* Seniority Distribution of Hires
* Country Hiring Trends Over Time
* Overall Hire Rate KPI
* Average Code Challenge Score by Technology

These outputs demonstrate the analytical capabilities enabled by the dimensional model.

---

##  Key Learnings

* Proper grain definition is critical for dimensional modeling.
* Separation of Extract, Transform, and Load ensures clean architecture.
* Surrogate keys improve DW scalability.
* Analytical queries must always run against the Data Warehouse.
* Visualization design significantly impacts interpretability.

---

## 👩‍💻 Author

Amy B
Data Engineering & Artificial Intelligence Student

```