SELECT winnerName AS name, COUNT(*) AS "number of matches", ROUND(AVG(minutes),2) AS "average length"
FROM ATPResult  
GROUP BY winnerName
HAVING "number of matches" >= 10
ORDER BY "average length" ASC;
