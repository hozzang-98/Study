WITH TMP AS (SELECT 
    id,
    visit_date,
    people,
    lag(people, 2) OVER (ORDER BY visit_date asc) as before_two,
    lag(people) OVER (ORDER BY visit_date asc) as before_one,
    lead(people) OVER (ORDER BY visit_date asc) as after_one,
    lead(people, 2) OVER (ORDER BY visit_date asc) as after_two
FROM Stadium)

SELECT id, visit_date, people
FROM TMP
WHERE (before_two >= 100 and before_one >= 100 and people >= 100)
or (before_one >= 100 and people >= 100 and after_one >= 100)
or (people >= 100 and after_one >= 100 and after_two >= 100)