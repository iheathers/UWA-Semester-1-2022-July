SELECT
    title, COUNT(person_id) AS "num of crew members"
FROM 
    titles 
LEFT JOIN crewmembers 
    USING(title_id)
GROUP BY title_id;
