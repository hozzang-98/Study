WITH LAG_TABLE as (
SELECT user_pseudo_id, event_timestamp_kst, lag(event_timestamp_kst) OVER (ORDER BY event_timestamp_kst) as before_time
FROM ga
WHERE user_pseudo_id = 'S3WDQCqLpK'),

PART_TABLE as (SELECT
 user_pseudo_id,
 event_timestamp_kst,
 before_time,
 CASE WHEN before_time is null THEN 1
      WHEN (julianday(event_timestamp_kst) - julianday(before_time)) * 24 >= 1 THEN 1
      ELSE 0
      END AS session
FROM LAG_TABLE),

SID_TABLE as (SELECT
 user_pseudo_id, 
 event_timestamp_kst, 
 before_time,
 sum(session) OVER (ORDER BY event_timestamp_kst) as session_id
FROM PART_TABLE)

SELECT user_pseudo_id, min(event_timestamp_kst) as session_start, max(event_timestamp_kst) as session_end
FROM SID_TABLE
GROUP BY session_id
ORDER BY session_start asc