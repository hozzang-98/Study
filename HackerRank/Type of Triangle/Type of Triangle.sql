SELECT CASE WHEN (A =  B AND B = C AND C = A) THEN 'Equilateral'
            WHEN (A + B <= C) OR (A + C <= B) OR (B + C <= A) THEN 'Not A Triangle' 
            WHEN (A = B) or (B = C) or (C = A) THEN 'Isosceles'
            WHEN (A != B AND B != C AND C != A) THEN 'Scalene'
            END AS types
FROM TRIANGLES
            