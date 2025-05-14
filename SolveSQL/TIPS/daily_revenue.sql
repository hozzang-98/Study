SELECT day, sum(total_bill) as revenue_daily
FROM tips
GROUP BY day
Having revenue_daily > 1000
ORDER BY revenue_daily desc