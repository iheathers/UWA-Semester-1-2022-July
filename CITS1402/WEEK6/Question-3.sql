SELECT yr AS year, COUNT(*)AS "number of matches" 
FROM WTAResult 
GROUP BY yr, winnerCountry
HAVING winnerCountry="AUS";