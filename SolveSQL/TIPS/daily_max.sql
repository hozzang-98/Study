WITH daily_sum as (
  SELECT day, round(sum(tip),2) as tip_daily
  FROM tips
  GROUP BY day)

SELECT day, max(tip_daily) as tip_daily
FROM daily_sum;