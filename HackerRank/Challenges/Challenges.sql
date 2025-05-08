With 
group_table as (SELECT h.hacker_id, h.name, count(c.challenge_id) as challenge_cnt
                FROM Hackers h
                INNER JOIN Challenges c ON h.hacker_id = c.hacker_id
                GROUP BY h.hacker_id, h.name),
count_table as (SELECT challenge_cnt, count(*) as freq FROM group_table GROUP BY challenge_cnt),
max_table as (SELECT MAX(challenge_cnt) as max_cnt FROM group_table)


SELECT t1.hacker_id, t1.name, t1.challenge_cnt
FROM group_table t1
INNER JOIN max_table t2 on 1=1
INNER JOIN count_table t3 on t1.challenge_cnt = t3.challenge_cnt
WHERE t1.challenge_cnt = t2.max_cnt or t3.freq = 1
ORDER BY t1.challenge_cnt desc, t1.hacker_id