WITH
  sales as (
    SELECT
      c.name as developer,
      p.name as platform,
      sum(
        g.sales_na + g.sales_eu + g.sales_jp + g.sales_other
      ) as sales
    FROM
      games g
      INNER JOIN companies c on g.developer_id = c.company_id
      INNER JOIN platforms p on g.platform_id = p.platform_id
    GROUP BY
      c.name,
      p.name
  ),
  main_platform as (
    SELECT
      developer,
      platform,
      sales,
      rank() over (
        PARTITION BY
          developer
        ORDER BY
          sales desc
      ) as RN
    FROM
      sales
  )
SELECT
  developer,
  platform,
  sales
FROM
  main_platform
WHERE
  RN = 1