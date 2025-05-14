SELECT title
FROM film
WHERE rating in ('R', 'NC-17')
and SUBSTR(TITLE,-1,1) not in ('A', 'E', 'I', 'O', 'U')