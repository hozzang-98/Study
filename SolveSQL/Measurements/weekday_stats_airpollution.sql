WITH SUB_TABLE AS (SELECT
  STRFTIME('%u', measured_at) AS weekday_num,
  CASE STRFTIME('%u', measured_at)
    WHEN '1' THEN '월요일'
    WHEN '2' THEN '화요일'
    WHEN '3' THEN '수요일'
    WHEN '4' THEN '목요일'
    WHEN '5' THEN '금요일'
    WHEN '6' THEN '토요일'
    ELSE '일요일'
  END AS weekday_name,
  ROUND(AVG(no2), 4) AS no2,
  ROUND(AVG(o3), 4) AS o3,
  ROUND(AVG(co), 4) AS co,
  ROUND(AVG(so2), 4) AS so2,
  ROUND(AVG(pm10), 4) AS pm10,
  ROUND(AVG(pm2_5), 4) AS pm2_5
FROM measurements
GROUP BY weekday_num)

SELECT weekday_name as weekday, no2, o3, co, so2, pm10, pm2_5
FROM SUB_TABLE
ORDER BY weekday_num