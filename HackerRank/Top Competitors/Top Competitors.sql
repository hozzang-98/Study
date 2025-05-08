SELECT H.hacker_id, H.name
FROM Submissions S
INNER JOIN Challenges C on S.challenge_id = C.challenge_id
INNER JOIN Difficulty D on D.difficulty_level = C.difficulty_level
INNER JOIN Hackers H on H.hacker_id = S.hacker_id
WHERE D.score = S.score
GROUP BY H.hacker_id, H.name
HAVING COUNT(H.hacker_id) >= 2
ORDER BY COUNT(H.hacker_id) desc, H.hacker_id asc