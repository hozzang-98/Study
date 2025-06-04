WITH TMP AS (
SELECT
    requester_id as id,
    COUNT(accepter_id) as num
FROM RequestAccepted
GROUP BY requester_id
UNION ALL
SELECT
    accepter_id as id,
    COUNT(requester_id) as num
FROM RequestAccepted
GROUP BY accepter_id)

SELECT
    id,
    SUM(num) as num
FROM TMP
GROUP BY id
ORDER BY SUM(num) DESC
LIMIT 1