SELECT
    MONTH(record_date) as "month",
    MAX(data_value) as "max",
    MIN(data_value) as "min",
    ROUND(AVG(CASE WHEN data_type = 'avg' THEN data_value END),0) as "avg"
FROM temperature_records
GROUP BY MONTH(record_date)