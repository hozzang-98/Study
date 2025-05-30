WITH RANK_TABLE AS (
SELECT
    D.name as Department,
    E.name as Employee,
    E.salary as Salary,
    RANK() OVER (PARTITION BY D.name ORDER BY E.salary DESC) as RN
FROM Department D
INNER JOIN Employee E ON D.id = E.departmentId)

SELECT
    Department, Employee, Salary
FROM RANK_TABLE
WHERE RN = 1