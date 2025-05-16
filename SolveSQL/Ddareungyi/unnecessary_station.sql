SELECT local, count(name) as num_stations
FROM station
GROUP BY local
ORDER BY num_stations