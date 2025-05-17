SELECT  order_date,
        count(DISTINCT CASE WHEN category = 'Furniture' THEN order_id ELSE NULL END) furniture,
        round(count(DISTINCT CASE WHEN category = 'Furniture' THEN order_id ELSE NULL END) * 100.0 / count(distinct order_id), 2) furniture_pct
FROM records
GROUP BY order_date
HAVING count(DISTINCT order_id) >= 10
AND furniture_pct >= 40
ORDER BY 3 DESC, 1;