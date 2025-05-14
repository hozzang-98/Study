SELECT * 
FROM tips
WHERE total_bill > 
      (SELECT avg(total_bill) 
       FROM tips);

WITH day_sales as (
  SELECT day, sum(total_bill) as day_sum
  FROM tips
  GROUP BY day)

SELECT round(avg(day_sum), 2) as avg_sales
FROM day_sales;