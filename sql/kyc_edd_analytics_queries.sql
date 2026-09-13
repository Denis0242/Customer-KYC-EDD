
-- Financial Crime Customer Risk & KYC/EDD Analytics

-- 1. Risk tier distribution
SELECT risk_level, COUNT(*) AS customers
FROM customer_risk_analytics
GROUP BY risk_level
ORDER BY customers DESC;

-- 2. EDD population and drivers
SELECT primary_risk_driver, COUNT(*) AS edd_customers
FROM customer_risk_analytics
WHERE edd_required = 1
GROUP BY primary_risk_driver
ORDER BY edd_customers DESC;

-- 3. KYC remediation candidates
SELECT customer_id, customer_type, country, kyc_complete_pct, risk_score, risk_level
FROM customer_risk_analytics
WHERE kyc_complete_pct < 100
ORDER BY risk_score DESC, kyc_complete_pct ASC;

-- 4. High-risk / critical customers
SELECT customer_id, country, risk_score, risk_level, primary_risk_driver
FROM customer_risk_analytics
WHERE risk_level IN ('High','Critical')
ORDER BY risk_score DESC;

-- 5. PEP population
SELECT customer_id, country, risk_score, risk_level, customer_status
FROM customer_risk_analytics
WHERE pep_flag = 1
ORDER BY risk_score DESC;

-- 6. Sanctions potential matches
SELECT customer_id, country, risk_score, customer_status
FROM customer_risk_analytics
WHERE sanctions_hit = 1
ORDER BY risk_score DESC;

-- 7. Adverse media cases
SELECT customer_id, country, risk_score, risk_level
FROM customer_risk_analytics
WHERE adverse_media_flag = 1
ORDER BY risk_score DESC;

-- 8. KYC completeness by customer type
SELECT customer_type,
       AVG(kyc_complete_pct) AS avg_kyc_completeness
FROM customer_risk_analytics
GROUP BY customer_type;

-- 9. Review aging
SELECT
    CASE
      WHEN age_days <= 30 THEN '0-30'
      WHEN age_days <= 60 THEN '31-60'
      WHEN age_days <= 90 THEN '61-90'
      ELSE '90+'
    END AS aging_band,
    COUNT(*) AS cases
FROM kyc_review_cases
WHERE case_status <> 'Closed'
GROUP BY aging_band;

-- 10. Escalated cases
SELECT case_id, customer_id, review_reason, age_days, risk_score, priority
FROM kyc_review_cases
WHERE case_status = 'Escalated'
ORDER BY risk_score DESC, age_days DESC;

-- 11. Business UBO exposure
SELECT customer_id,
       COUNT(*) AS owners,
       SUM(CASE WHEN ubo_25pct_flag=1 THEN 1 ELSE 0 END) AS owners_at_or_above_25pct
FROM beneficial_owners
GROUP BY customer_id
ORDER BY owners_at_or_above_25pct DESC;

-- 12. Country concentration of high-risk customers
SELECT country, COUNT(*) AS high_risk_customers
FROM customer_risk_analytics
WHERE risk_level IN ('High','Critical')
GROUP BY country
ORDER BY high_risk_customers DESC;
