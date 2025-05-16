SELECT
  T1.game_id,
  T1.name,
  CASE
    WHEN T1.critic_score is null THEN (
      SELECT
        round(avg(T2.critic_score), 3)
      FROM
        games T2
      WHERE
        t1.genre_id = t2.genre_id
    )
    ELSE T1.critic_score
  END AS critic_score,
  CASE
    WHEN T1.critic_count is null THEN (
      SELECT
        CEIL(avg(T2.critic_count))
      FROM
        games T2
      WHERE
        t1.genre_id = t2.genre_id
    )
    ELSE T1.critic_count
  END AS critic_count,
  CASE
    WHEN T1.user_score is null THEN (
      SELECT
        round(avg(T2.user_score), 3)
      FROM
        games T2
      WHERE
        t1.genre_id = t2.genre_id
    )
    ELSE T1.user_score
  END AS user_score,
  CASE
    WHEN T1.user_count is null THEN (
      SELECT
        CEIL(avg(T2.user_count))
      FROM
        games T2
      WHERE
        t1.genre_id = t2.genre_id
    )
    ELSE T1.user_count
  END AS user_count
FROM
  games T1
WHERE
  (
    T1.critic_score is null
    or T1.user_score is null
  )
  and T1.year >= 2015;

# 다른 풀이

  WITH genre_avg AS (
  SELECT
    genre_id,
    ROUND(AVG(critic_score), 3) AS avg_critic_score,
    CEIL(AVG(critic_count)) AS avg_critic_count,
    ROUND(AVG(user_score), 3) AS avg_user_score,
    CEIL(AVG(user_count)) AS avg_user_count
  FROM games
  GROUP BY genre_id
)

SELECT
  g.game_id,
  g.name,
  COALESCE(g.critic_score, ga.avg_critic_score) AS critic_score,
  COALESCE(g.critic_count, ga.avg_critic_count) AS critic_count,
  COALESCE(g.user_score, ga.avg_user_score) AS user_score,
  COALESCE(g.user_count, ga.avg_user_count) AS user_count
FROM games g
LEFT JOIN genre_avg ga ON g.genre_id = ga.genre_id
WHERE (g.critic_score IS NULL OR g.user_score IS NULL)
  AND g.year >= 2015;