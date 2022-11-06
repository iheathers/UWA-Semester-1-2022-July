SELECT DISTINCT title FROM titles JOIN castmembers USING (title_id) 
WHERE title_id NOT IN (
SELECT 
    title_id
FROM 
    people 
    JOIN castmembers USING(person_id)  
WHERE people.died IS NOT NULL);