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
  and T1.year >= 2015