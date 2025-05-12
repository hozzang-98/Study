SELECT
  region as Region,
  COUNT(DISTINCT CASE WHEN category = 'Furniture' THEN order_id ELSE null END) 'Furniture',
  COUNT(DISTINCT CASE WHEN category = 'Office Supplies' THEN order_id ELSE null END) 'Office Supplies',
  COUNT(DISTINCT CASE WHEN category = 'Technology' THEN order_id ELSE null END) 'Technology'
FROM records
GROUP BY region