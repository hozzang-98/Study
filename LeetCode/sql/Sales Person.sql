WITH RED_SALES_MAN AS (
SELECT
    O.sales_id
FROM Orders O
INNER JOIN Company C
ON O.com_id = C.com_id
WHERE C.name = "RED")

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (SELECT sales_id FROM RED_SALES_MAN)