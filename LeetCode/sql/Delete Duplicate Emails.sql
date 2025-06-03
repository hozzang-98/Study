DELETE FROM person
WHERE id NOT IN ( SELECT s.min_id
			   	  FROM ( SELECT email, MIN(id) min_id
					     FROM person
					     GROUP BY email ) s )