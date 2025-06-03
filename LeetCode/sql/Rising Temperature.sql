WITH COMPARE_TABLE AS (
SELECT
    id,
    recordDate,
    temperature,
    lag(recordDate) OVER(ORDER BY recordDate) as prev_date,
    lag(temperature) OVER(ORDER BY recordDate) as prev_temperature
FROM Weather)

SELECT id
FROM COMPARE_TABLE
WHERE temperature > prev_temperature and DATEDIFF(recordDate, prev_date) = 1