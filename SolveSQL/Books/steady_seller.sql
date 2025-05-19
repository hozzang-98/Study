WITH
  FICTION_BOOKS as (
    SELECT DISTINCT
      author,
      year
    FROM
      books
    WHERE
      genre = 'Fiction'
  ),
  LAG_TABLE as (
    SELECT
      author,
      year,
      lag(year, 1) OVER (
        PARTITION BY
          author
        ORDER BY
          year
      ) prev_year
    FROM
      FICTION_BOOKS
  ),
  GROUPING_TABLE as (
    SELECT
      author,
      year,
      prev_year,
      sum(
        CASE
          WHEN year - prev_year = 1 THEN 0
          ELSE 1
        END
      ) OVER (
        PARTITION BY
          author
        ORDER BY
          year
      ) as grouping
    FROM
      LAG_TABLE
  )
SELECT
  author,
  MAX(year) AS year,
  COUNT(*) AS depth
FROM
  GROUPING_TABLE
GROUP BY
  author,
  grouping
HAVING
  depth >= 5