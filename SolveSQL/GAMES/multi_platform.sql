WITH SUB_TABLE AS (
SELECT 
  g.name as game,
  CASE WHEN p.name in ('PS3','PS4', 'PSP', 'PSV') THEN 'Sony'
    WHEN p.name in ('Wii', 'WiiU', 'DS', '3DS') THEN 'Nintendo'
    WHEN p.name in ('X360', 'XONE') THEN 'Microsoft'
    ELSE 'ANOTHER'
    END AS platform
FROM games g
INNER JOIN platforms p on g.platform_id = p.platform_id
WHERE g.year >= 2012)

SELECT game as name
FROM SUB_TABLE
WHERE platform != 'ANOTHER'
GROUP BY game
HAVING COUNT(DISTINCT platform) >= 2