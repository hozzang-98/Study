SELECT H.hacker_id, H.name, sum(MT.max_score) as score
FROM (SELECT hacker_id, challenge_id, MAX(score) AS max_score
      FROM Submissions
      GROUP BY hacker_id, challenge_id) as MT
INNER JOIN Hackers H ON MT.hacker_id = H.hacker_id
GROUP BY H.hacker_id, H.name
HAVING sum(MT.max_score) != 0
ORDER BY score desc, H.hacker_id asc