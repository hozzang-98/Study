SELECT 
    employee_id, 
    CASE WHEN (LEFT(name, 1) != 'M') AND (employee_id % 2 = 1) 
        THEN salary ELSE 0 END as bonus 
FROM employees
ORDER BY employee_id