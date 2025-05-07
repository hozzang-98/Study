SELECT IF(t2.Grade < 8, null, t1.Name), 
					t2.Grade, 
					t1.Marks
FROM Students t1
INNER JOIN Grades t2
ON t1.Marks BETWEEN t2.Min_Mark and t2.Max_Mark
ORDER BY t2.Grade desc, 
				 t1.Name asc,
				 t1.Marks desc