WITH
  usage_table as (
    SELECT
      station_id,
      sum(
        CASE
          WHEN strftime ('%Y', rental_time) = '2018' THEN 1
          ELSE NULL
        END
      ) as usage_2018,
      sum(
        CASE
          WHEN strftime ('%Y', rental_time) = '2019' THEN 1
          ELSE NULL
        END
      ) as usage_2019
    FROM
      (
        SELECT
          rent_at rental_time,
          rent_station_id station_id
        FROM
          rental_history
        WHERE
          strftime ('%Y-%m', rent_at) in ('2018-10', '2019-10')
        UNION ALL
        SELECT
          return_at rental_time,
          return_station_id station_id
        FROM
          rental_history
        WHERE
          strftime ('%Y-%m', rent_at) in ('2018-10', '2019-10')
      )
    GROUP BY
      station_id
  )
SELECT
  UT.station_id,
  S.name,
  local,
  round(100.0 * UT.usage_2019 / UT.usage_2018, 2) usage_pct
FROM
  usage_table UT
  INNER JOIN station S ON UT.station_id = S.station_id
WHERE
  usage_pct <= 50