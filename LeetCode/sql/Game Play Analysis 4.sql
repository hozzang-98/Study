WITH FIRST_LOGIN AS (
SELECT
    player_id,
    MIN(event_date) as first_login
FROM Activity
GROUP BY player_id), 
CONSECUTIVE_TABLE AS (
SELECT 
    T1.player_id,
    T1.first_login,
    T2.event_date
FROM FIRST_LOGIN T1
LEFT JOIN Activity T2 
ON T1.player_id = T2.player_id
and DATEDIFF(T2.event_date, T1.first_login) = 1)

SELECT 
    ROUND(
    COUNT(CASE WHEN event_date IS NOT NULL THEN player_id END)
    /
    COUNT(player_id)
    , 2) as fraction
FROM CONSECUTIVE_TABLE