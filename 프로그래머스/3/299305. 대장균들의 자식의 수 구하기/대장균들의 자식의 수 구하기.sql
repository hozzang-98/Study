SELECT CHILD.ID, COUNT(PARENT.ID) as CHILD_COUNT
FROM ECOLI_DATA CHILD 
LEFT JOIN ECOLI_DATA PARENT
ON CHILD.ID = PARENT.PARENT_ID
GROUP BY 1
ORDER BY 1