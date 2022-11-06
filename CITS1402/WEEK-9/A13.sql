SELECT 
    * 
FROM 
    people 
WHERE 
    name IN (SELECT 
                name
            FROM 
                people
            GROUP BY 
                name
            HAVING 
                COUNT(*) > 1
    );