SELECT 
    premiered AS year, 
    COUNT(*) AS "number of movies"
FROM 
    titles
GROUP BY 
    premiered
ORDER BY 
    "number of movies" DESC,
    year DESC;