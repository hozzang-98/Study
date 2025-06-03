SELECT
    E.name as name,
    B.bonus as bonus
FROM Employee E
LEFT JOIN Bonus B ON E.empId = B.empId
WHERE B.bonus < 1000 or B.bonus IS NULL