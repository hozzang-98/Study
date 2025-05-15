WITH multiple_medalist as (
SELECT a.name, COUNT(DISTINCT r.team_id) as cnt
FROM records r
INNER JOIN games g on r.game_id = g.id
INNER JOIN athletes a on r.athlete_id = a.id
WHERE g.year >= 2000
and r.medal is not NULL
GROUP BY r.athlete_id
HAVING cnt >= 2)

SELECT name
FROM multiple_medalist
ORDER BY name;