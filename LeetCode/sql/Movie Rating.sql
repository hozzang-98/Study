WITH many_user AS(
    SELECT
        mr.user_id,
        name,
        COUNT(*) AS cnt
    FROM MovieRating mr
    INNER JOIN Users u ON mr.user_id = u.user_id
    GROUP BY mr.user_id
    ORDER BY cnt DESC, name
    LIMIT 1
),
many_rating AS(
    SELECT
        mr.movie_id,
        title,
        AVG(rating) AS avg_rating
    FROM MovieRating mr 
    INNER JOIN Movies m ON mr.movie_id = m.movie_id
    WHERE 1=1
        AND created_at LIKE'2020-02%'
    GROUP BY mr.movie_id
    ORDER BY avg_rating DESC, title
    LIMIT 1
)
SELECT name AS results  
FROM many_user

UNION ALL

SELECT title
FROM many_rating