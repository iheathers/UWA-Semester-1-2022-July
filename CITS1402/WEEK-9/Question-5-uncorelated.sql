SELECT  person_id, name, category
    FROM 
        people 
    JOIN crewmembers USING(person_id)
    GROUP BY
         person_id, category
 
     
                