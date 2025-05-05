SELECT 
    ct.contest_id, 
    ct.hacker_id, 
    ct.name, 
    SUM(ss.total_submissions) as total_submissions, 
    SUM(ss.total_accepted_submissions) as total_accepted_submissions,
    SUM(vs.total_views) as total_views,
    SUM(vs.total_unique_views) as total_unique_views    
FROM Contests ct
LEFT JOIN Colleges clg on ct.contest_id = clg.contest_id
LEFT JOIN Challenges chg on clg.college_id = chg.college_id
LEFT JOIN 
    (SELECT challenge_id,
            SUM(total_views) as total_views,
            SUM(total_unique_views) as total_unique_views
     FROM View_Stats
     GROUP BY challenge_id) vs on chg.challenge_id = vs.challenge_id
LEFT JOIN
    (SELECT challenge_id,
            SUM(total_submissions) as total_submissions,
            SUM(total_accepted_submissions) as total_accepted_submissions
     FROM Submission_Stats
     GROUP BY challenge_id) ss on chg.challenge_id = ss.challenge_id
     
GROUP BY ct.contest_id, ct.hacker_id, ct.name
HAVING 
    total_submissions IS NOT NULL OR
    total_accepted_submissions IS NOT NULL OR
    total_views IS NOT NULL OR
    total_unique_views IS NOT NULL
ORDER BY ct.contest_id