SELECT 
    c.company_code, 
    c.founder, 
    count(distinct(lm.lead_manager_code)), 
    count(distinct(sm.senior_manager_code)),
    count(distinct(m.manager_code)),
    count(distinct(e.employee_code))
FROM Company c
LEFT JOIN Lead_Manager lm on c.company_code = lm.company_code
LEFT JOIN Senior_Manager sm on lm.lead_manager_code = sm.lead_manager_code
LEFT JOIN Manager m on sm.senior_manager_code = m.senior_manager_code
LEFT JOIN Employee e on m.manager_code = e.manager_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code