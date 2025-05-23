SELECT *
FROM points
WHERE quartet = 'I';

SELECT 
  quartet, 
  round(avg(x), 2) as x_mean, 
  round(variance(x), 2) as x_var,
  round(avg(y), 2) as y_mean, 
  round(variance(y), 2) as y_var
FROM points
GROUP BY quartet