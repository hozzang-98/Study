SELECT
    T2.unique_id,
    T1.name
FROM Employees T1
LEFT JOIN EmployeeUNI T2 ON T1.id = T2.id