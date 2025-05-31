SELECT
    T.request_at as Day,
    ROUND(
        COUNT(CASE WHEN T.status LIKE 'cancelled%' THEN T.id END) 
        / 
        COUNT(T.id)
    ,2) as "Cancellation Rate"
FROM Trips T
INNER JOIN Users C ON T.client_id = C.users_id and C.banned = 'No'
INNER JOIN Users D ON T.driver_id = D.users_id and D.banned = 'No' 
WHERE T.request_at BETWEEN '2013-10-01' and '2013-10-03'
GROUP BY Day
ORDER BY Day ASC