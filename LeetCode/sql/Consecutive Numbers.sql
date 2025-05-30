WITH TMP AS (
SELECT 
    num,
    lag(num) OVER (ORDER BY id asc) as one,
    lag(num, 2) OVER (ORDER BY id asc) as two
FROM Logs)

SELECT
    DISTINCT(num) as ConsecutiveNums
FROM TMP
WHERE num = one and one = two