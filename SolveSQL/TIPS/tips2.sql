SELECT *
FROM tips
WHERE size % 2 = 1;

WITH daily_sum as (
  SELECT day, round(sum(tip),2) as tip_daily
  FROM tips
  GROUP BY day)

SELECT day, max(tip_daily) as tip_daily
FROM daily_sum;

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