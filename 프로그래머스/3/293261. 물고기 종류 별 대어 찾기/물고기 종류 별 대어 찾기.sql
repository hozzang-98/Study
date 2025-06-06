-- 코드를 작성해주세요
SELECT 
    T1.ID as ID, 
    T2.FISH_NAME as FISH_NAME, 
    LENGTH
FROM FISH_INFO T1
INNER JOIN FISH_NAME_INFO T2 ON T1.FISH_TYPE = T2.FISH_TYPE
WHERE LENGTH = (
    SELECT MAX(T1_SUB.LENGTH) 
    FROM FISH_INFO T1_SUB
    INNER JOIN FISH_NAME_INFO T2_SUB ON T1_SUB.FISH_TYPE = T2_SUB.FISH_TYPE 
    WHERE T2.FISH_NAME = T2_SUB.FISH_NAME
    GROUP BY T2_SUB.FISH_NAME)