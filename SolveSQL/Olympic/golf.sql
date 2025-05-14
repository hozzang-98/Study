SELECT
  DISTINCT r.athlete_id
FROM
  events e
  INNER JOIN records r on e.id = r.event_id
WHERE e.sport = 'Golf'