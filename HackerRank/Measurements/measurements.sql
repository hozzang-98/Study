SELECT t1.measured_at as today, 
      t2.measured_at as next_day,
      t1.pm10 as pm10,
      t2.pm10 as next_pm10
FROM measurements as t1
INNER JOIN measurements as t2
ON t1.measured_at = DATE(t2.measured_at, '-1 day')
WHERE t1.pm10 < t2.pm10