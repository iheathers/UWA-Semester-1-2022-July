SELECT category, COUNT(DISTINCT person_id)
FROM crewmembers 
GROUP BY category;
