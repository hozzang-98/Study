SELECT sum(t1.POPULATION)
FROM CITY t1
INNER JOIN COUNTRY t2
on t1.COUNTRYCODE = t2.CODE
WHERE t2.CONTINENT = 'Asia'