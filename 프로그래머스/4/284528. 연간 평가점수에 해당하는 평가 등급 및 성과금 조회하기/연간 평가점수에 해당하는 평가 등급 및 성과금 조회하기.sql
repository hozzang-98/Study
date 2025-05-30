WITH AVG_TABLE AS (
SELECT 
    EMP_NO,
    AVG(SCORE) as AVG_SCORE
FROM HR_GRADE
GROUP BY EMP_NO),

GRADE_TABLE AS (
SELECT
    EMP_NO,
    CASE WHEN AVG_SCORE >= 96 THEN 'S'
         WHEN AVG_SCORE < 96 and AVG_SCORE >= 90 THEN 'A'
         WHEN AVG_SCORE < 90 and AVG_SCORE >= 80 THEN 'B'
        ELSE 'C' END AS GRADE
FROM AVG_TABLE)

SELECT
    T1.EMP_NO,
    T2.EMP_NAME,
    T1.GRADE,
    T2.SAL * (CASE WHEN GRADE = 'S' THEN 0.2
                  WHEN GRADE = 'A' THEN 0.15
                  WHEN GRADE = 'B' THEN 0.1
                  ELSE 0 END) AS BONUS
FROM GRADE_TABLE T1
INNER JOIN HR_EMPLOYEES T2 ON T1.EMP_NO = T2.EMP_NO
ORDER BY T1.EMP_NO ASC
        