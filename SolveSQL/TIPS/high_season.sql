SELECT *
FROM tips
WHERE day in (
  SELECT day
  FROM tips
  GROUP BY day
  HAVING sum(total_bill) >= 1500
)