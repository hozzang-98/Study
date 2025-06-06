SELECT 
  CASE WHEN measured_at between '2022-03-01' and '2022-05-31' THEN 'spring'
   WHEN measured_at between '2022-06-01' and '2022-08-31' THEN 'summer'
   WHEN measured_at between '2022-09-01' and '2022-11-30' THEN 'autumn'
   ELSE 'winter'
  END AS season,
  median(pm10) as pm10_median,
  round(AVG(pm10), 2) as pm10_average
FROM measurements
GROUP BY season