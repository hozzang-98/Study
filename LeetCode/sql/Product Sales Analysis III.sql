WITH EARLY_YEAR AS (SELECT 
    product_id,
    min(year) as first_year
FROM Sales
GROUP BY product_id)

SELECT 
    T1.product_id,
    T1.first_year,
    T2.quantity,
    T2.price
FROM EARLY_YEAR T1
INNER JOIN Sales T2
ON T1.product_id = T2.product_id
and T1.first_year = T2.year