SELECT
    T2.product_name,
    sum(T1.unit) as unit
FROM Orders T1
INNER JOIN Products T2 ON T1.product_id = T2.product_id
WHERE DATE_FORMAT(order_date, '%Y-%m') = '2020-02'
GROUP BY T2.product_name
HAVING sum(T1.unit) >= 100