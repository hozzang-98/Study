SELECT 
  datetime(measured_at, '+10 minutes') as end_at,
  ROUND(AVG(zone_quads) OVER(ORDER BY measured_at ROWS BETWEEN 5 PRECEDING and CURRENT ROW), 2) as zone_quads,
  ROUND(AVG(zone_smir) OVER(ORDER BY measured_at ROWS BETWEEN 5 PRECEDING and CURRENT ROW), 2) as zone_smir,
  ROUND(AVG(zone_boussafou) OVER(ORDER BY measured_at ROWS BETWEEN 5 PRECEDING and CURRENT ROW), 2) as zone_boussafou
FROM power_consumptions
WHERE measured_at BETWEEN '2017-01-01' and '2017-02-01'