SELECT 
    id,
    movie,
    description,
    rating
FROM Cinema
WHERE description != 'boring'
and id % 2 != 0
ORDER BY rating desc