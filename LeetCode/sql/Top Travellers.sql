SELECT
    T1.name,
    IFNULL(SUM(T2.distance), 0) as travelled_distance
FROM Users T1
LEFT JOIN Rides T2 ON T1.id = T2.user_id
GROUP BY T1.id, T1.name
ORDER BY 2 desc, 1 asc