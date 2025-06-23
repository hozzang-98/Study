SELECT
    T1.product_name,
    T2.year,
    T2.price
FROM Product T1
INNER JOIN Sales T2 ON T1.product_id = T2.product_id