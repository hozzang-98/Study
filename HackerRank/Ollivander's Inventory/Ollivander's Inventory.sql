WITH RankedWands AS (
  SELECT 
    W.id, 
    P.age, 
    W.coins_needed, 
    W.power,
    ROW_NUMBER() OVER (
      PARTITION BY W.power, P.age 
      ORDER BY W.coins_needed ASC
    ) AS RN
  FROM Wands W
  JOIN Wands_Property P ON W.code = P.code
  WHERE P.is_evil = 0
)

SELECT id, age, coins_needed, power
FROM RankedWands
WHERE RN = 1
ORDER BY power DESC, age DESC;