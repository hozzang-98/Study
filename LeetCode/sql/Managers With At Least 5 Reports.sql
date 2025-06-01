SELECT name
FROM Employee E
WHERE id in (SELECT managerId
            FROM Employee 
            GROUP BY managerId 
            HAVING COUNT(id) >= 5)