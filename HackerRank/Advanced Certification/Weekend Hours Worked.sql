WITH in_out as (
SELECT
    emp_id,
    DATE(timestamp) AS work_date,
    MIN(timestamp) AS clock_in,
    MAX(timestamp) AS clock_out
FROM attendance
WHERE DAYOFWEEK(timestamp) IN (1, 7)
GROUP BY emp_id, work_date)

SELECT
    emp_id,
    SUM(FLOOR(TIMESTAMPDIFF(MINUTE, clock_in, clock_out)/60) ) as work_hours
FROM in_out
GROUP BY emp_id
ORDER BY work_hours DESC