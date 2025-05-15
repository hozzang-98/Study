SELECT DISTINCT(page_location)
FROM ga
WHERE page_location not like '%\_%' ESCAPE '\'
ORDER BY page_location