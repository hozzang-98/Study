SELECT s1.submission_date -- first column

        , (SELECT COUNT(DISTINCT s2.hacker_id) -- second column
        FROM submissions s2
        WHERE s2.submission_date = s1.submission_date
        AND (SELECT COUNT(DISTINCT s3.submission_date) 
            FROM submissions s3 
            WHERE s3.hacker_id = s2.hacker_id
            AND s3.submission_date < s1.submission_date) = DATEDIFF(s1.submission_date, '2016-03-01'))
            
     , (SELECT s2.hacker_id -- third column
        FROM submissions s2
        WHERE s2.submission_date = s1.submission_date
        GROUP BY hacker_id
        ORDER BY COUNT(submission_id) DESC, hacker_id
        LIMIT 1) AS hackerid
        
    , (SELECT name FROM hackers WHERE hacker_id = hackerid) -- fourth column
    
FROM (SELECT DISTINCT submission_date FROM submissions) s1