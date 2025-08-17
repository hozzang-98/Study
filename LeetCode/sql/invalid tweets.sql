SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15
   OR content REGEXP '[^a-zA-Z0-9! ]';