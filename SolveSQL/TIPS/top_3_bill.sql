WITH
  rank_table as (
    SELECT
      day,
      time,
      sex,
      total_bill,
      DENSE_RANK() over (
        PARTITION BY
          day
        ORDER BY
          total_bill desc
      ) as rn
    FROM
      tips
  )
SELECT
  day, time, sex, total_bill
FROM
  rank_table
WHERE
  rn <= 3