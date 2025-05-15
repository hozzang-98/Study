WITH
  MAX_TABLE AS (
    SELECT
      id,
      max(x)
    FROM
      points
    UNION ALL
    SELECT
      id,
      max(y)
    FROM
      points
  )

SELECT id
FROM MAX_TABLE
ORDER BY id