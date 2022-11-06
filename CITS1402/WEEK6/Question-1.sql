SELECT premiered AS year, COUNT(*)AS "number of movies"
FROM titles 
GROUP BY premiered;