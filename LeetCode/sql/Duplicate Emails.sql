SELECT
    email as Email
FROM Person
GROUP BY email
HAVING COUNT(id) >= 2