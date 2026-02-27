-- ============================================
-- KPI 1: Hires by Technology
-- ============================================

SELECT 
    dt.technology,
    COUNT(*) AS total_hires
FROM fact_applications fa
JOIN dim_technology dt 
    ON fa.technology_key = dt.technology_key
WHERE fa.hired_flag = 1
GROUP BY dt.technology
ORDER BY total_hires DESC;



-- ============================================
-- KPI 2: Hires by Year
-- ============================================

SELECT 
    dd.year,
    COUNT(*) AS total_hires
FROM fact_applications fa
JOIN dim_date dd
    ON fa.date_key = dd.date_key
WHERE fa.hired_flag = 1
GROUP BY dd.year
ORDER BY dd.year;



-- ============================================
-- KPI 3: Hires by Seniority
-- ============================================

SELECT 
    ds.seniority,
    COUNT(*) AS total_hires
FROM fact_applications fa
JOIN dim_seniority ds
    ON fa.seniority_key = ds.seniority_key
WHERE fa.hired_flag = 1
GROUP BY ds.seniority
ORDER BY total_hires DESC;



-- ============================================
-- KPI 4: Hires by Country over Years
-- (USA, Brazil, Colombia, Ecuador)
-- ============================================

SELECT 
    dc.country,
    dd.year,
    COUNT(*) AS total_hires
FROM fact_applications fa
JOIN dim_country dc
    ON fa.country_key = dc.country_key
JOIN dim_date dd
    ON fa.date_key = dd.date_key
WHERE fa.hired_flag = 1
  AND dc.country IN ('United States', 'Brazil', 'Colombia', 'Ecuador')
GROUP BY dc.country, dd.year
ORDER BY dc.country, dd.year;



-- ============================================
-- KPI 5: Hire Rate (%)
-- ============================================

SELECT 
    ROUND(
        SUM(CASE WHEN hired_flag = 1 THEN 1 ELSE 0 END) * 100.0 
        / COUNT(*), 
    2) AS hire_rate_percentage
FROM fact_applications;



-- ============================================
-- KPI 6: Average Scores by Technology
-- ============================================

SELECT 
    dt.technology,
    ROUND(AVG(fa.code_challenge_score), 2) AS avg_code_score,
    ROUND(AVG(fa.technical_interview_score), 2) AS avg_interview_score
FROM fact_applications fa
JOIN dim_technology dt
    ON fa.technology_key = dt.technology_key
GROUP BY dt.technology
ORDER BY avg_code_score DESC;