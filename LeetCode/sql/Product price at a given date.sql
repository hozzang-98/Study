WITH product_list AS (
    SELECT DISTINCT product_id
    FROM Products)

SELECT
    T1.product_id,
    COALESCE(T2.price, 10) as price
FROM product_list T1
LEFT JOIN (
    SELECT
        product_id,
        new_price as price,
        change_date,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) as new_date
    FROM Products
    WHERE change_date <= '2019-08-16') AS T2
ON T1.product_id = T2.product_id
WHERE new_date = 1 or new_date IS NULL