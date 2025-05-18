WITH
  friends_LEFT AS (
    SELECT
      user_a_id friend_id
    FROM edges
    WHERE user_b_id = 3820
  ),
  friends_RIGHT AS (
    SELECT
      user_b_id friend_id
    FROM edges
    WHERE user_a_id = 3820
  )

SELECT
  user_a_id,
  user_b_id,
  3820 user_c_id
FROM edges
WHERE
  user_a_id IN (SELECT * FROM friends_LEFT)
  AND user_b_id IN (SELECT * FROM friends_LEFT)

UNION ALL

SELECT
  user_a_id,
  3820 user_b_id,
  user_b_id user_c_id
FROM edges
WHERE
  user_a_id IN (SELECT * FROM friends_LEFT)
  AND user_b_id IN (SELECT * FROM friends_RIGHT)

UNION ALL

SELECT
  3820 user_a_id,
  user_a_id user_b_id,
  user_b_id user_c_id
FROM edges
WHERE
  user_a_id IN (SELECT * FROM friends_RIGHT)
  AND user_b_id IN (SELECT * FROM friends_RIGHT);