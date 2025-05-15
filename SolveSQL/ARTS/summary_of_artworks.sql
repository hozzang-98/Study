SELECT 
  classification,
  COUNT(DISTINCT CASE WHEN strftime('%Y', acquisition_date) = '2014' THEN artwork_id ELSE Null END) '2014',
  COUNT(DISTINCT CASE WHEN strftime('%Y', acquisition_date) = '2015' THEN artwork_id ELSE Null END) '2015',
  COUNT(DISTINCT CASE WHEN strftime('%Y', acquisition_date) = '2016' THEN artwork_id ELSE Null END) '2016'
FROM artworks
GROUP BY classification
ORDER BY classification 