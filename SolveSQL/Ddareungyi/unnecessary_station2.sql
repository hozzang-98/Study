WITH
  SUB_TABLE AS (
    SELECT
      s.station_id,
      s.name,
      count(s_near.station_id) as cnt
    FROM
      station s
      LEFT JOIN station s_near ON s.station_id != s_near.station_id
      and s.updated_at < s_near.updated_at
      and 2 * 6356 * ASIN(
        SQRT(
          POWER(SIN(RADIANS((s_near.lat - s.lat) / 2)), 2) + COS(RADIANS(s.lat)) * COS(RADIANS(s_near.lat)) * POWER(SIN(RADIANS((s_near.lng - s.lng) / 2)), 2)
        )
      ) <= 0.3
    GROUP BY
      s.station_id
  )
SELECT
  station_id,
  name
FROM
  SUB_TABLE
WHERE
  cnt >= 5