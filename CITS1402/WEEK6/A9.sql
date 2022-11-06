SELECT orderNumber AS "order number", COUNT(*) AS "number of line items", ROUND(SUM(priceEach * quantityOrdered), 2) AS "total cost" 
FROM orderdetails
GROUP BY orderNumber
ORDER BY "total cost" DESC;