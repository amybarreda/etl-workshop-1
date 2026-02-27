# visualization/kpi_dashboard.py

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# ===============================
# Connect to Data Warehouse
# ===============================

conn = sqlite3.connect("data/warehouse/data_warehouse.db")


# ============================================
# KPI 1: Hires by Technology (Top 10 - Improved)
# ============================================

query_1 = """
SELECT dt.technology, COUNT(*) AS total_hires
FROM fact_applications fa
JOIN dim_technology dt 
    ON fa.technology_key = dt.technology_key
WHERE fa.hired_flag = 1
GROUP BY dt.technology
ORDER BY total_hires DESC
LIMIT 10
"""

df1 = pd.read_sql(query_1, conn)

plt.figure(figsize=(10, 6))
plt.barh(df1["technology"], df1["total_hires"])
plt.gca().invert_yaxis()  # Highest at top
plt.title("Top 10 Technologies by Hires")
plt.xlabel("Total Hires")
plt.ylabel("Technology")
plt.tight_layout()
plt.show()


# ============================================
# KPI 2: Hires by Year
# ============================================

query_2 = """
SELECT dd.year, COUNT(*) AS total_hires
FROM fact_applications fa
JOIN dim_date dd
    ON fa.date_key = dd.date_key
WHERE fa.hired_flag = 1
GROUP BY dd.year
ORDER BY dd.year
"""

df2 = pd.read_sql(query_2, conn)

plt.figure()
plt.plot(df2["year"], df2["total_hires"])
plt.title("Hires by Year")
plt.xlabel("Year")
plt.ylabel("Total Hires")
plt.tight_layout()
plt.show()


# ============================================
# KPI 3: Hires by Seniority
# ============================================

query_3 = """
SELECT ds.seniority, COUNT(*) AS total_hires
FROM fact_applications fa
JOIN dim_seniority ds
    ON fa.seniority_key = ds.seniority_key
WHERE fa.hired_flag = 1
GROUP BY ds.seniority
ORDER BY total_hires DESC
"""

df3 = pd.read_sql(query_3, conn)

plt.figure()
plt.bar(df3["seniority"], df3["total_hires"])
plt.title("Hires by Seniority")
plt.xlabel("Seniority Level")
plt.ylabel("Total Hires")
plt.tight_layout()
plt.show()


# ============================================
# KPI 4: Hires by Country over Years
# ============================================

query_4 = """
SELECT dc.country, dd.year, COUNT(*) AS total_hires
FROM fact_applications fa
JOIN dim_country dc
    ON fa.country_key = dc.country_key
JOIN dim_date dd
    ON fa.date_key = dd.date_key
WHERE fa.hired_flag = 1
  AND dc.country IN ('United States', 'Brazil', 'Colombia', 'Ecuador')
GROUP BY dc.country, dd.year
ORDER BY dc.country, dd.year
"""

df4 = pd.read_sql(query_4, conn)

plt.figure()

for country in df4["country"].unique():
    subset = df4[df4["country"] == country]
    plt.plot(subset["year"], subset["total_hires"], label=country)

plt.title("Hires by Country over Years")
plt.xlabel("Year")
plt.ylabel("Total Hires")
plt.legend()
plt.tight_layout()
plt.show()


# ============================================
# KPI 5: Hire Rate (%) - Improved
# ============================================

query_5 = """
SELECT 
    SUM(CASE WHEN hired_flag = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) 
    AS hire_rate_percentage
FROM fact_applications
"""

df5 = pd.read_sql(query_5, conn)

hire_rate = round(df5["hire_rate_percentage"][0], 2)

plt.figure(figsize=(6, 4))
plt.text(0.5, 0.6, f"{hire_rate}%", 
         fontsize=40,
         horizontalalignment='center')

plt.text(0.5, 0.4, "Overall Hire Rate",
         fontsize=12,
         horizontalalignment='center')

plt.xticks([])
plt.yticks([])
plt.box(False)
plt.tight_layout()
plt.show()


# ============================================
# KPI 6: Average Code Score by Technology (Top 10 - Improved)
# ============================================

query_6 = """
SELECT 
    dt.technology,
    AVG(fa.code_challenge_score) AS avg_code_score
FROM fact_applications fa
JOIN dim_technology dt
    ON fa.technology_key = dt.technology_key
GROUP BY dt.technology
ORDER BY avg_code_score DESC
LIMIT 10
"""

df6 = pd.read_sql(query_6, conn)

plt.figure(figsize=(10, 6))
plt.barh(df6["technology"], df6["avg_code_score"])
plt.gca().invert_yaxis()
plt.title("Top 10 Technologies by Average Code Score")
plt.xlabel("Average Code Challenge Score")
plt.ylabel("Technology")
plt.tight_layout()
plt.show()


# Close connection
conn.close()