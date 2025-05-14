SELECT event_date_kst as dt, COUNT(distinct user_pseudo_id) as users
FROM ga
GROUP BY event_date_kst
HAVING event_date_kst between '2021-08-02' and '2021-08-09'
ORDER BY event_date_kst