SELECT c.name
FROM games g
INNER JOIN companies c on g.publisher_id = c.company_id
GROUP BY g.publisher_id
HAVING COUNT(g.game_id) >= 10