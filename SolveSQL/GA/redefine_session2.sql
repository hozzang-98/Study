WITH
  TMP1 as (
    SELECT
      user_pseudo_id,
      event_timestamp_kst,
      event_name,
      ga_session_id,
      lag(event_timestamp_kst) OVER (
        ORDER BY
          event_timestamp_kst
      ) as before_time
    FROM
      ga
    WHERE
      user_pseudo_id = 'a8Xu9GO6TB'
  ),

TMP2 as (SELECT
  user_pseudo_id,
  event_timestamp_kst,
  event_name,
  ga_session_id,
  before_time,
  CASE
    WHEN (julianday(event_timestamp_kst) - julianday(before_time)) * 24 * 60 * 60 >= 600 THEN 1
    ELSE 0
  END AS session
FROM
  TMP1)

SELECT user_pseudo_id, event_timestamp_kst, event_name, ga_session_id, sum(session) OVER (ORDER BY event_timestamp_kst) + 1 as new_session_id 
FROM TMP2