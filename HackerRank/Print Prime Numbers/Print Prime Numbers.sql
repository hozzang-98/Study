With Recursive NUMBERS as (
    SELECT 2 as N
    UNION ALL
    SELECT N+1
    FROM NUMBERS
    WHERE N < 1000
),

PRIMES as (
    SELECT N
    FROM NUMBERS N1
    WHERE NOT EXISTS (SELECT N2.N
                      FROM NUMBERS N2
                      WHERE N2.N > 1
                      AND N2.N <= SQRT(N1.N)
                      AND N1.N % N2.N = 0))
                      
SELECT GROUP_CONCAT(N SEPARATOR '&')
FROM PRIMES