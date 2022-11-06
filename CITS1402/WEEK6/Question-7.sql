SELECT yr AS year, ROUND(COUNT(*) * 100.0 / 127 , 2) AS "percentage of matches"
FROM ATPResult WHERE winnerAge < loserAge
GROUP BY yr;
