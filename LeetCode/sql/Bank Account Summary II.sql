WITH TMP AS (
SELECT 
    T1.account,
    T1.name as NAME,
    sum(T2.amount) as BALANCE
FROM Users T1
INNER JOIN Transactions T2 ON T1.account = T2.account
GROUP BY 1, 2) 

SELECT NAME, BALANCE
FROM TMP
WHERE BALANCE > 10000