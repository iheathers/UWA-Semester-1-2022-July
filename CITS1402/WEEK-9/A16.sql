SELECT  
    ((titles.premiered/ 10) || "0s") AS decade,
    title, 
    rating 
FROM titles 
    JOIN ratings USING(title_id) 
WHERE 
    (titles.premiered/10, ratings.rating) 
    IN (
        SELECT 
            titles.premiered/10 AS year_group,
            MAX(ratings.rating) 
        FROM 
            titles 
        JOIN ratings USING(title_id) 
        GROUP BY 
            year_group
      )
ORDER BY decade;


