SELECT
    EMP.name as Employee
FROM Employee EMP
LEFT JOIN Employee MNG
ON EMP.managerId = MNG.id
WHERE EMP.salary >= MNG.salary