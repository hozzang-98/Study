WITH CUM_WEIGHT AS (
SELECT
    turn,
    person_name,
    weight,
    sum(weight) over (ORDER BY turn) as Total_Weight
FROM Queue)

SELECT person_name
FROM CUM_WEIGHT
WHERE Total_Weight <= 1000
ORDER BY Total_Weight DESC
LIMIT 1