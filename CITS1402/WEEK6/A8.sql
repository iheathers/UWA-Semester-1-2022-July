SELECT yr AS year, winnerName AS "player name", COUNT(*) AS "number of matches won"
FROM WTAResult 
GROUP BY yr, winnerName
HAVING winnerCountry="AUS";