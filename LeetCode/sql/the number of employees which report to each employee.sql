SELECT 
    T1.reports_to as employee_id,
    T2.name,
    COUNT(T1.employee_id) as reports_count,
    ROUND(avg(T1.age), 0) as average_age
FROM Employees T1
INNER JOIN Employees T2 ON T1.reports_to = T2.employee_id
GROUP BY 1,2
ORDER BY 1