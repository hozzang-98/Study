WITH
  MENTEE as (
    SELECT
      employee_id as mentee_id,
      name as mentee_name,
      department
    FROM
      employees
    WHERE
      join_date >= date('2021-12-31', '-3 months')
  ),
  MENTOR AS (
    SELECT
      employee_id as mentor_id,
      name as mentor_name,
      department
    FROM
      employees
    WHERE
      join_date <= date('2021-12-31', '-2 years')
  )
SELECT
  mentee_id,
  mentee_name,
  mentor_id,
  mentor_name
FROM
  MENTEE T1
  LEFT JOIN MENTOR T2 ON T1.department != T2.department
ORDER BY
  mentee_id,
  mentor_id