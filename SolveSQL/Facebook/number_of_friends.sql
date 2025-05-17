WITH
  FOR_A AS (
    SELECT
      user_id,
      count(user_b_id) b_cnt
    FROM users u
    LEFT JOIN edges e1 ON u.user_id = e1.user_a_id
    GROUP BY user_id
  ),
  FOR_B AS (
    SELECT
      user_id,
      count(user_a_id) a_cnt
    FROM users u
    LEFT JOIN edges e2 ON u.user_id = e2.user_b_id
    GROUP BY user_id
  )

SELECT
  A.user_id,
  a_cnt + b_cnt num_friends
FROM FOR_A A
INNER JOIN FOR_B B ON A.user_id = B.user_id
ORDER BY num_friends DESC, A.user_id asc;