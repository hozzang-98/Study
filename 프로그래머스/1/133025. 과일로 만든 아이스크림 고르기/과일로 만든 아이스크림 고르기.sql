SELECT FH.FLAVOR
FROM FIRST_HALF FH
INNER JOIN ICECREAM_INFO II
ON FH.FLAVOR = II.FLAVOR
WHERE II.INGREDIENT_TYPE = 'fruit_based' and FH.TOTAL_ORDER > 3000
ORDER BY FH.TOTAL_ORDER desc