SELECT
    T1.contest_id,
    ROUND(
        COUNT(T1.user_id)
        /
        (SELECT COUNT(*)
        FROM Users)
        * 100.0
        , 2) as percentage
FROM Register T1
GROUP BY T1.contest_id
ORDER BY 2 desc, 1 asc