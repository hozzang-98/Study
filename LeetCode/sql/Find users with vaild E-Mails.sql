SELECT 
    user_id,
    name,
    mail
FROm Users 
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$';