WITH NUMBERED AS (
  SELECT *, ROW_NUMBER() OVER (ORDER BY Start_Date) AS rn
  FROM Projects),
  
GROUPED AS (
  SELECT *, DATE_SUB(Start_Date, INTERVAL rn DAY) AS GRP
  FROM NUMBERED)
  
SELECT MIN(Start_Date) AS project_start, MAX(End_Date) AS project_end
FROM NUMBERED
GROUP BY GRP
ORDER BY project_end - project_start  ASC, project_start;