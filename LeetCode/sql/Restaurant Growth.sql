WITH cte_sum AS(
        SELECT visited_on
                , SUM(amount) as sum_amount
        FROM customer
        GROUP BY visited_on
)
, cte_all AS(
        SELECT visited_on
                , SUM(sum_amount) OVER w AS amount
                , ROUND(SUM(sum_amount) OVER w / 7, 2) AS average_amount
        FROM cte_sum
        WINDOW w AS (ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW)          
)
SELECT visited_on, amount, average_amount
FROM cte_all
WHERE visited_on >= (SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY)
                     FROM customer)
ORDER BY visited_on