SELECT CONCAT(Name, "(", LEFT(Occupation, 1), ")") as name_ocp
FROM OCCUPATIONS
ORDER BY name_ocp;

SELECT CONCAT("There are a total of ", count(Occupation), " ",lower(Occupation),"s.") as descrp
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY descrp