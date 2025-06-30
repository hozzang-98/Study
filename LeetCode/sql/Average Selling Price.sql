SELECT
    T1.product_id,
    IFNULL(ROUND(SUM(T1.price * T2.units) / SUM(T2.units), 2),0) as average_price
FROM Prices T1
LEFT JOIN UnitsSold T2
ON T1.product_id = T2.product_id
and T2.purchase_date BETWEEN T1.start_date and T1.end_date
GROUP BY 1